import cv2
import numpy
from colorthief import ColorThief
import colorsys

from ultralytics import YOLO

sensitivity = 15
background_size = 2500
path_image = 'images'
path_background = 'image/background.jpg'
path_human = 'image/human.jpg'


def color_rgb(red, green, blue):
    return blue, green, red


COLOR_RED = color_rgb(255, 0, 0)
COLOR_GREEN = color_rgb(0, 255, 0)
COLOR_LIGHT_BLUE = color_rgb(129, 231, 255)
COLOR_BLUE = color_rgb(2, 70, 205)


def main_color_hsv(filename):
    color_thief = ColorThief(filename)
    color = color_thief.get_color(quality=1)
    color_hsv = colorsys.rgb_to_hsv(color[0] / 255, color[1] / 255, color[2] / 255)
    return int(color_hsv[0] * 179), int(color_hsv[1] * 255), int(color_hsv[2] * 255)


def find_mask_background(dominate_color_hsv, image_hsv):
    lower_color = numpy.array(
        (dominate_color_hsv[0] - sensitivity, dominate_color_hsv[1] - sensitivity, dominate_color_hsv[2] - sensitivity))
    upper_color = numpy.array(
        (dominate_color_hsv[0] + sensitivity, dominate_color_hsv[1] + sensitivity, dominate_color_hsv[2] + sensitivity))
    return cv2.inRange(image_hsv, lower_color, upper_color)


def find_background_pixel_size():
    upper = background.shape[0]
    lower = 0
    background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    ret, background_thresh = cv2.threshold(background_gray, 100, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(background_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for value in contours:
        x, y, w, h = cv2.boundingRect(value)
        if y > lower:
            lower = y
        if y < upper:
            upper = y

    cv2.line(background, (0, upper), (background.shape[1], upper), COLOR_RED)
    cv2.line(background, (0, lower), (background.shape[1], lower), COLOR_RED)

    return lower - upper


def yolov8_detect():
    height, width, channels = image.shape
    model = YOLO("yolov8-seg.pt")

    results = model(image)
    result = results[0]
    segmentation_contours_idx = []
    for seg in result.masks.segments:
        seg[:, 0] *= width
        seg[:, 1] *= height
        segment = numpy.array(seg, dtype=numpy.int32)
        segmentation_contours_idx.append(segment)

    boxes = numpy.array(result.boxes.xyxy)
    class_ids = numpy.array(result.boxes.cls)
    return boxes, class_ids, segmentation_contours_idx


def find_height_human(human_pixel_size, background_pixel_size):
    return human_pixel_size * background_size / background_pixel_size


def detect_image(image, path_image2):
    human_pixel_size = 0
    dominate_color_hsv = main_color_hsv(path_image2)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask_background = find_mask_background(dominate_color_hsv, image_hsv)
    background = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_background)
    background = cv2.cvtColor(background, cv2.COLOR_HSV2BGR)

    background_pixel_size = find_background_pixel_size()

    human = numpy.zeros((image.shape[0], image.shape[1], 3), numpy.uint8)
    human[:, :] = COLOR_LIGHT_BLUE
    boxes, classes, segmentations = yolov8_detect()
    for box, class_id, seg in zip(boxes, classes, segmentations):
        (x, y, x2, y2) = box
        if class_id == 0:
            human_pixel_size = y2 - y
            cv2.polylines(human, [seg], True, COLOR_BLUE, 4)

    return find_height_human(human_pixel_size, background_pixel_size)


if __name__ == '__main__':
    image = cv2.imread(path_image)

    human, background, height = detect_image(image)

    print(height)
    cv2.imwrite(path_human, human)
    cv2.imwrite(path_background, background)

from django.db import models


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.title), filename])


def nameFileUserPhoto(instance, filename):
    return '/'.join(['users/after', str(instance.name), str(instance.surname), filename])


def nameFileUserConturPhoto(instance, filename):
    return '/'.join(['users/before',  str(instance.name), str(instance.surname), filename])


class Users(models.Model):
    name = models.CharField(max_length=511)
    surname = models.CharField(max_length=511)
    second_name = models.CharField(max_length=511, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    height = models.DecimalField(max_digits=5, decimal_places=1, default=0, blank=True)
    userPhoto = models.ImageField(upload_to=nameFileUserPhoto, blank=True)
    userConturPhoto = models.ImageField(upload_to=nameFileUserConturPhoto, blank=True)

    def __str__(self):
        return self.surname


class Mattress(models.Model):
    title = models.CharField(max_length=511)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    min_height = models.DecimalField(max_digits=4, decimal_places=1, default=0, blank=True)
    max_height = models.DecimalField(max_digits=4, decimal_places=1, default=300, blank=True)
    min_weight = models.DecimalField(max_digits=4, decimal_places=1, default=0, blank=True)
    max_weight = models.DecimalField(max_digits=4, decimal_places=1, default=300, blank=True)
    photo = models.ImageField(upload_to=nameFile, blank=True)
    is_curvature = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title


class Pillow(models.Model):
    title = models.CharField(max_length=511)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    min_height = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    max_height = models.DecimalField(max_digits=4, decimal_places=1, default=300)
    min_weight = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    max_weight = models.DecimalField(max_digits=4, decimal_places=1, default=300)
    photo = models.ImageField(upload_to=nameFile, blank=True)
    is_curvature = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
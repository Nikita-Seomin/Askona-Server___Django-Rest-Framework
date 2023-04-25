from rest_framework import serializers
from .models import Mattress, Pillow


class MattressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mattress
        fields = ('title', 'min_height', 'max_height', 'min_weight', 'max_weight', 'photo')

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)



class MattressPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mattress
        fields = ('photo',)

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)


class PillowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pillow
        fields = ('title', 'min_height', 'max_height', 'min_weight', 'max_weight', 'photo')



from abc import ABC

from rest_framework import serializers
from .models import Mattress, Pillow


class MattressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mattress
        fields = ('title', 'min_height', 'max_height', 'min_weight', 'max_weight', 'photo')


class MattressSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = Mattress
        
        fields = ('photo',)


class PillowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pillow
        fields = ('title', 'min_height', 'max_height', 'min_weight', 'max_weight', 'photo')



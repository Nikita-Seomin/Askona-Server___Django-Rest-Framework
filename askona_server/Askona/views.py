from wsgiref.util import FileWrapper

from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Mattress, Pillow
from .serializers import MattressSerializer, MattressSerializerImage, PillowSerializer


class ImageUploadView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializerImage


class MattressAPIList(generics.ListAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer


class MattressAPICreate(generics.CreateAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer


class MattressAPIUpdate(generics.UpdateAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer


class MattressAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer



class PillowAPIList(generics.ListAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer


class PillowAPIUpdate(generics.UpdateAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer


class PillowAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer



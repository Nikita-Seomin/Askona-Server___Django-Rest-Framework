from wsgiref.util import FileWrapper

from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Mattress
from .render import PNGRenderer
from .serializers import MattressSerializer, MattressSerializerImage


class ImageUploadView(generics.RetrieveUpdateDestroyAPIView):
    # renderer_classes = [PNGRenderer]
    # parser_classes = [FileUploadParser]
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializerImage




class MattressAPIList(generics.ListAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer


class MattressAPIUpdate(generics.UpdateAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer


class MattressAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer



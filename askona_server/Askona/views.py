from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework import generics, viewsets, serializers
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Mattress, Pillow
from .renders import JPEGRenderer, PNGRenderer
from .serializers import MattressSerializer, PillowSerializer, MattressPhotoSerializer


class MattressViewSet(viewsets.ModelViewSet):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer

    def get(self, request, format=None):
        queryset = Mattress.objects.all()
        serializer = serializers.MattressSerializer(queryset, context={"request": request}, many=True)
        return Response(serializer.data)


class MattressAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    # renderer_classes = [JPEGRenderer, PNGRenderer]

    queryset = Mattress.objects.all()
    serializer_class = MattressPhotoSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(FileWrapper(Mattress.objects.get(id=serializer.data['id'])['image'].open()))
#             # You can also specify the content_type in your response
#         return Response(data={"detail": "Serializer Error"})

# @api_view(['GET'])

# # @detail_route(methods=['get'], renderer_classes=(PDFRenderer,))
# class MattressAPICRUD(APIView):
#
#     @renderer_classes([JSONRenderer])
#     def get(self, request, *args, **kwargs):
#         with open('../images/2021-11-30.png', 'rb') as report:
#             return Response(
#                 report.read(),
#                 headers={'Content-Disposition': 'attachment; filename=2021-11-30.png'},
#                 content_type='application/png')
    # @renderer_classes([JSONRenderer])

    # def get(self, request, pk):
    #     m = Mattress.objects.all()
    #     return HttpResponse(content='<img src="{{MattressPhotoSerializer(m).data.get(\'photo\')}}" />')
    #     # return Response(MattressPhotoSerializer(m).data.get('photo') , content_type='image/png')


class PillowAPIList(generics.ListAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer



class PillowAPIUpdate(generics.UpdateAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer


class PillowAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer



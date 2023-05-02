from rest_framework import generics, viewsets, serializers
from rest_framework.response import Response

from .models import Mattress, Pillow
from .serializers import MattressSerializer, PillowSerializer, MattressPhotoSerializer


# ----------------------users------------------------------------





#----------------------------------------------------------------------


# ----------------------Mattress------------------------------------

class MattressViewSet(viewsets.ModelViewSet):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer

    def get(self, request, format=None):
        queryset = Mattress.objects.all()
        serializer = serializers.MattressSerializer(queryset, context={"request": request}, many=True)
        return Response(serializer.data)


class MattressAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mattress.objects.all()
    serializer_class = MattressPhotoSerializer


# -------------------------------------------------------------------------------

class PillowAPIList(generics.ListAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer


class PillowAPIUpdate(generics.UpdateAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer


class PillowAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pillow.objects.all()
    serializer_class = PillowSerializer

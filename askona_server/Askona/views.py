from rest_framework import generics, viewsets


from .models import Mattress, Pillow
from .serializers import MattressSerializer, PillowSerializer


class MattressViewSet(viewsets.ModelViewSet):
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



from django.forms import model_to_dict
from rest_framework import generics, viewsets, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mattress, Pillow, Users
from .photoAnalizer import detect_image
from .serializers import MattressSerializer, PillowSerializer, MattressPhotoSerializer, UserSerializer


# ----------------------users------------------------------------
class UserAPIView(APIView):

    def get(self, request):
        users = Users.objects.all().values()
        return Response({'posts': list(users)})

    def post(self, request):
        # serializer = UserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        userHeight = detect_image(request.data['userConturPhoto'])
        post_new = Users.objects.create(
            name=request.data['name'],
            surname=request.data['surname'],
            height=userHeight
        )
        return Response({'posts': model_to_dict(post_new)})

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

from django.contrib import admin
from django.urls import path, include
from Askona.views import *

from rest_framework import routers

matressRouter = routers.SimpleRouter()
matressRouter.register(r'mattress', MattressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(matressRouter.urls)),

    path('api/v1/pillowlist/', PillowAPIList.as_view()),
    path('api/v1/pillowlist/<int:pk>/', PillowAPICRUD.as_view())
]

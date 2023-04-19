from django.contrib import admin
from django.urls import path
from Askona.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/mattresslist/', MattressAPIList.as_view()),
    path('api/v1/mattresslist/', MattressAPICreate.as_view()),
    path('api/v1/mattresslist/<int:pk>/', MattressAPIUpdate.as_view()),
    path('api/v1/pillowlist/', PillowAPIList.as_view()),
    path('api/v1/pillowlist/<int:pk>/', PillowAPICRUD.as_view()),
]

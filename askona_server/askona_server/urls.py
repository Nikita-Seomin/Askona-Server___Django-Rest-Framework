from django.contrib import admin
from django.urls import path
from Askona.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/mattresslist/', MattressViewSet.as_view({'get': 'list','post':'create'})),
    path('api/v1/mattresslist/<int:pk>/', MattressViewSet.as_view({'put': 'update', 'delete':'destroy'})),

    path('api/v1/pillowlist/', PillowAPIList.as_view()),
    path('api/v1/pillowlist/<int:pk>/', PillowAPICRUD.as_view())
]

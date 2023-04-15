from django.contrib import admin
from django.urls import path
from Askona.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/mattresslist/', MattressAPIList.as_view()),
    path('upload/<int:pk>/', ImageUploadView.as_view()),
    path('api/v1/mattresslist/<int:pk>/', MattressAPICRUD.as_view()),
]

from django.contrib import admin
from django.urls import path, include
from Askona.views import *
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

matressRouter = routers.SimpleRouter()
matressRouter.register(r'mattress', MattressViewSet)

# usersRouter = routers.SimpleRouter()
# usersRouter.register(r'users', UserAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(matressRouter.urls)),

    path('api/v1/users/', UserAPIView.as_view()),

    path('api/v1/mattressPhoto/<int:pk>/', MattressAPICRUD.as_view()),

    path('api/v1/pillowlist/', PillowAPIList.as_view()),
    path('api/v1/pillowlist/<int:pk>/', PillowAPICRUD.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
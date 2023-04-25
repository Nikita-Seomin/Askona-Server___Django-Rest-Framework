from django.contrib import admin
from django.urls import path, include
from Askona.views import *
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

matressRouter = routers.SimpleRouter()
matressRouter.register(r'mattress', MattressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(matressRouter.urls)),
    # path('upload/', views.ImageViewSet.as_view(), name='upload'),

    path('api/v1/mattressPhoto/<int:pk>/', MattressAPICRUD.as_view()),

    path('api/v1/pillowlist/', PillowAPIList.as_view()),
    path('api/v1/pillowlist/<int:pk>/', PillowAPICRUD.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# class JPEGRenderer(renderers.BaseRenderer):
#     media_type = 'image/jpeg'
#     format = 'jpg'
#     charset = None
#     render_style = 'binary'
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return data
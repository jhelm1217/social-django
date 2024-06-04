"""
URL configuration for project_social project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from app_social.views import *
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import routers


router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'message', MessageViewSet)
router.register(r'image', ImageViewSet)


urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('create-user/', create_user),
    path('get-profile/', get_profile),
    path('message-poll/', message_poll),
    path('create-image/', create_image),
    path('get-images/', get_images),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
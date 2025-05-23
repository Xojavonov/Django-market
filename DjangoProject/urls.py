"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from pyexpat.errors import messages
from DjangoProject.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
       path('admin/', admin.site.urls),
    path('',include('apps.urls'))
]+static(MEDIA_URL,document_root=MEDIA_ROOT)

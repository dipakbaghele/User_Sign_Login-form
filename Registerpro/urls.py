"""Registerpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import Settings, settings
from django.contrib import admin
from django.template.context_processors import static
from django.conf.urls.static import static
from django.urls import path,include

from RegisterApp import views
from RegisterApp.views import show_home_page, show_category_page
from Registerpro.settings import MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RegisterApp.urls')),
    path('show',show_home_page),
    path('category/<int:cid>',show_category_page ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""addenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_xml.views import UserController, IndexController, header, footer, xml_converter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserController.register),
    path('views/index/index/', IndexController.index),
    path('views/index/header/', header.header_principal),
    path('views/index/footer/', footer.footer_principal),
    path('convert/', xml_converter.xml),

]

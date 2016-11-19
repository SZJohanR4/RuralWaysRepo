"""ruralways URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'', include('usuario.urls')),# un usuario que llega, no importa si esta logeado o no  es un usuario
    url(r'^administrador/', include('administrador.urls')),#cuando en el url aparesca administrador, tomara el urls.py de la app administrador
    url(r'^agricultor/', include('agricultor.urls')),#cuando en el url aparesca agricultor, tomara el urls.py de la app agricultor
    url(r'^cliente/', include('cliente.urls')),#cuando en el url aparesca cliente, tomara el urls.py de la app cliente
]

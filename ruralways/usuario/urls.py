from django.conf.urls import url
from administrador import views as admin_views
from agricultor import views as agricultor_views
from cliente import views as cliente_views
from . import views

urlpatterns = [
    url(r'^$',views.index_view, name='index'),
    ]
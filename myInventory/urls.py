from django.conf.urls import url
from .views import *
from django.urls import path, include


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_alimentos$', display_alimentos, name='display_alimentos')
]
from django.urls import path
from .views import index, listaMaterie, votiStudenti, mediaStudenti, MaxMinVoti

app_name='voti'
urlpatterns = [
    path('voti', index, name='index'),
    path('voti/lista_materie', listaMaterie, name='lista_materie'),
    path('voti/voti_studenti', votiStudenti, name='voti_studenti'),
    path('voti/media_studenti', mediaStudenti, name='media_studenti'),
    path('voti/max_min_voti', MaxMinVoti, name='max_min_voti')
]
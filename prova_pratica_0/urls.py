from django.urls import path
from prova_pratica_0.views import somma, media, index

app_name="prova_pratica_0"

urlpatterns = [
    path('prova_pratica_0/somma', somma, name='somma'),
    path('prova_pratica_0/media', media, name='media'),
    path('prova_pratica_0', index, name='index')
]
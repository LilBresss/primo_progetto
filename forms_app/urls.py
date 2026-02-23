from django.urls import path
from .views import index, contatti, listaContatti

app_name='forms_app'
urlpatterns = [
    path('contatti/', index, name='index'),
    path('contatti/contattaci/', contatti, name='contattaci'),
    path('contatti/lista_contatti/', listaContatti, name='lista_contatti')
]
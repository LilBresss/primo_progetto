from django.urls import path
from .views import index, contatti, listaContatti, modifica_contatto, elimina_contatto

app_name='forms_app'
urlpatterns = [
    path('contatti/', index, name='index'),
    path('contatti/contattaci/', contatti, name='contattaci'),
    path('contatti/lista_contatti/', listaContatti, name='lista_contatti'),
    path('contatti/modifica_contatto/<int:pk>', modifica_contatto, name='modifica_contatto'),
    path('contatti/elimina_contatto/<int:pk>', elimina_contatto, name='elimina_contatto')
]
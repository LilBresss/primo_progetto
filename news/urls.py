from django.urls import path
from .views import home, articoloDetailView, giornalistaDetailView, listaArticoli, index, queryBase

app_name="news"
urlpatterns = [
    path('news', index, name='index'),
    path('news/homeview', home, name='homeview'),
    path("news/articoli/<int:pk>", articoloDetailView, name="articoli_detail"),
    path("news/giornalista/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("news/lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("news/lista_articoli", listaArticoli, name="lista_articoli"),
    path("news/query_base", queryBase, name="query_base")
]
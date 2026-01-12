from django.urls import path
from .views import home, articoloDetailView, listaArticoli

app_name="news"
urlpatterns = [
    path('news', home, name='homeview'),
    path("news/articoli/<int:pk>", articoloDetailView, name="articoli_detail"),
    path("news/lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("news/lista_articoli", listaArticoli, name="lista_articoli")
]
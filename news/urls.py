from django.urls import path
from .views import home, articoloDetailView

app_name="news"
urlpatterns = [
    path('news', home, name='homeview'),
    path("news/articoli/<int:pk>", articoloDetailView, name="articoli_detail")
]
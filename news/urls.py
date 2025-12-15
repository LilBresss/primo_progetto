from django.urls import path
from .views import home

app_name="news"
urlpatterns = [
    path('news', home, name='homeview')
]
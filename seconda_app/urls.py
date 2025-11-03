from django.urls import path
from seconda_app.views import es_if, if_else_elif, es_for, index

app_name="seconda_app"
urlpatterns = [
    path('seconda_app/es_if', es_if, name='es_if'),
    path('seconda_app/if_else_elif', if_else_elif, name='if_else_elif'),
    path('seconda_app/es_for', es_for, name='es_for'),
    path('seconda_app', index, name='index_seconda_app')
]
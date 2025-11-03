from django.urls import path
from prima_app.views import homepage,welcome,lista,chi_siamo,variabili,index
from seconda_app.views import es_if

app_name="prima_app"
urlpatterns=[
    path('prima_app/homepage', homepage, name='homepage'),
    path('prima_app/welcome', welcome, name='welcome'),
    path('prima_app/lista', lista, name='lista'),
    path('prima_app/chi_siamo', chi_siamo, name='chi_siamo'),
    path('prima_app/variabili', variabili, name='variabili'),
    path('prima_app', index, name='index_prima_app')
]
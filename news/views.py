from django.shortcuts import render
from .models import Articolo, Giornalista

# Create your views here.
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()

    context = {"articoli":articoli, "giornalisti":giornalisti}
    
    print(context)

    return render(request, "home.html", context)
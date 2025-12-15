from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

# Create your views here.
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()

    context = {"articoli":articoli, "giornalisti":giornalisti}
    
    print(context)

    return render(request, "home.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)
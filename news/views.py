from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

# Create your views here.
def index(request):
    return render(request,"index_news.html")

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {
        "articoli":articoli, "giornalisti":giornalisti
    }
    print(context)
    return render(request, "news/home.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {
        "articolo": articolo
    }
    return render(request, "news/articolo_detail.html", context)

def listaArticoli(request, pk=None):
    if(pk==None):
        articoli = Articolo.objects.all()
        titolo = "Tutti gli articoli"
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
        giornalista = Giornalista.objects.get(id=pk)
        titolo = f"Articoli di {giornalista.nome} {giornalista.cognome}"

    context = {
        'titolo': titolo,
        'articoli': articoli            
    }
    
    return render(request, 'news/lista_articoli.html', context)
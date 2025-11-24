from django.shortcuts import render
import random

# Create your views here.
def somma(request):

    var1 = random.randint(1,10)
    var2 = random.randint(1,10)

    context= {
        'var1': var1,
        'var2': var2,
        'somma': var1 + var2
    }
    return render(request,"prova_pratica_0/somma.html",context)

def media(request):
    lista = []
    somma = 0
    for i in range(30):
        n = random.randint(1,10)
        lista.append(n)
        somma = somma + n

    media = round(somma/len(lista),2)

    context= {
        'lista': lista,
        'media': media,
        'len_lista': len(lista)
    }
    return render(request,"prova_pratica_0/media.html",context)

def index(request):
    return render(request,"index.html")
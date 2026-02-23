from django.shortcuts import render
from .forms import FormContatto
from .models import Contatto
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index_contatti.html")

def contatti(request):
    # se la richiesti è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":
        # creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        # is_valid() controlla se il form inserito è valido
        if form.is_valid():
            # a questo punto possiamo usare i dati validi!
            # tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            # ringrazio l'utente per averci contattato - volendo possiamo effettuare un redirect a una apgina specifica
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    # se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()

    # arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta(con metodo GET), o se il form non è valido e ha errori
    context = {
        "form": form
    }
    return render(request, "forms_app/contatto.html", context)

def listaContatti(request):
    contatti = Contatto.objects.all()
    context = {
        'contatti': contatti
    }
    return render(request, "forms_app/lista_contatti.html", context)
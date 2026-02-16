from django.shortcuts import render

# Create your views here.def index(request):
def index (request):
    return render(request,"index_voti.html")

def listaMaterie (request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]

    context = {
        'materie': materie
    }

    return render(request, "voti/lista_materie.html", context)

def votiStudenti (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    

    context = {
        'voti': voti
    }

    return render(request, "voti/voti_studenti.html", context)

def mediaStudenti (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    print(voti)
    medie = {}

    for studente in voti:
        media = 0
        n = 0
        for lista in voti[studente]:
            media += lista[1]
            n = n+1
        medie[studente] = media/n
    print(medie)

    context = {
        'medie': medie
    }

    return render(request, "voti/media_studenti.html", context)

def MaxMinVoti (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    max_studente=[]
    min_studente=[]
    max_materia=[]
    min_materia=[]
    max=0
    min=11

    for studente in voti:
        for materia, voto, assenze in voti[studente]:
            if(max<voto):
                max=voto
                max_materia=[materia]
                max_studente=[studente]
            elif(max==voto):
                if(materia not in max_materia):
                    max_materia.append(materia) 
                if(studente not in max_studente):
                    max_studente.append(studente)
            if(min>voto):
                min=voto
                min_materia=[materia]
                min_studente=[studente]
            elif(min==voto):
                if(materia not in min_materia):
                    min_materia.append(materia) 
                if(studente not in min_studente):
                    min_studente.append(studente)


    context = {
        'max_studente': max_studente,
        'min_studente': min_studente,
        'max_materia': max_materia,
        'min_materia': min_materia,
        'max': max,
        'min': min
    }

    return render(request, "voti/max_min_voti.html", context)
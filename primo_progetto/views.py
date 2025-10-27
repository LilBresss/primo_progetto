from django.shortcuts import render

# Create your views here.
def index_root(request):
    return render(request,"index_root.html")
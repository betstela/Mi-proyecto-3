from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def homepage(request):
    return render(request, "main/inicio.html", {"usuarios": Usuario.objects.all})
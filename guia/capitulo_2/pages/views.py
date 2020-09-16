from django.shortcuts import render
from random import randrange, random
import datetime
# Create your views here.
def home_page(request):
   return render(request, 'hola_mundo.html')

def about(request):
   parametros = {'numero_favorito':round(random()*10,2)}
   return render(request, 'joan.html', parametros)
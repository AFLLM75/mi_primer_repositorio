from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
   return render(request,'recetas.html')

def florcalab(request):
   return render(request,'Recetas/Flor_de_calabacin/index.html')

def canelon(request):
   return render(request,'Recetas/Canelones/index.html')

def pizza(request):
   return render(request,'Recetas/pizza/index.html')

def carbonara(request):
   return render(request,'Recetas/carbonara/index.html')

def ensaladilla(request):
   return render(request,'Recetas/ensaladilla_rusa/index.html')

def feijoada(request):
   return render(request,'Recetas/Feijoada/index.html')

def gazpacho(request):
   return render(request,'Recetas/Gazpacho/index.html')

def mafe(request):
   return render(request,'Recetas/mafe/index.html')

def menuinf(request):
   return render(request,'Recetas/Menú_Infantil/index.html')

def recetafacil(request):
   return render(request,'Recetas/Receta_Facil/index.html')

def noodles(request):
   return render(request,'Recetas/Sopa_de_Noodles/index.html')
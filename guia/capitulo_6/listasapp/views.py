from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def form(request):
   return render(request,'formulario.html')

def anadir(request):
   prioridad = request.POST["name_prioridad"]
   titulo= request.POST["nombre_titulo"]
   nota = request.POST["name_nota"]
   return (HttpResponse(f'Insertado <br> '
                        f'Prioridad: {prioridad}<br>'
                        f'Título: {titulo}<br>'
                        f'Nota: {nota}<br>'))
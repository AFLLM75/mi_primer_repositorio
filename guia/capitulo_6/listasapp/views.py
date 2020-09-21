from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def form(request):
   return render(request,'formulario.html')

def anadir(request):
   return HttpResponse('Insertado')
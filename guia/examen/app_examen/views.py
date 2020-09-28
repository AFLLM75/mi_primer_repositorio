from django.shortcuts import render

# Create your views here.
def exa(request):
   return render(request, 'examen.html')


def dja(request):
   return render(request,'django.html')
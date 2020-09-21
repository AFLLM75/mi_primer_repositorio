from django.shortcuts import render
from django.http import HttpResponse
import psycopg2


# Create your views here.
def form(request):
   return render(request,'formulario.html')
"""
def anadir(request):
   prioridad = request.POST["name_prioridad"]
   titulo= request.POST["nombre_titulo"]
   nota = request.POST["name_nota"]
   return (HttpResponse(f'Insertado <br> '
                        f'Prioridad: {prioridad}<br>'
                        f'Título: {titulo}<br>'
                        f'Nota: {nota}<br>'))
"""

def insert(request):
   conn = psycopg2.connect(dbname="capitulo_6_db",
                           user="capitulo_6_user",
                           password="patata")

   cursor = conn.cursor()
   cursor.execute("INSERT INTO Nota VALUES ('Máxima','Cumpleaños', \
                  'Comprar Regalo');")
   conn.commit()
   cursor.close()
   conn.close()
   return HttpResponse("Insertado")


def select(request):
   conn = psycopg2.connect(dbname="capitulo_6_db",
                           user="capitulo_6_user",
                           password="patata")
   cursor = conn.cursor()
   cursor.execute("select * from Nota")
   html = '<html>'
   columns = [col[0] for col in cursor.description]
   for column in columns:
       html += str(column) + '|'
   html += '<br>'
   for empleado in cursor.fetchall():
       for columna in empleado:
           html += str(columna) + '|'
       html += '<br>'
   html += '</html>'
   cursor.close()
   conn.close()
   return HttpResponse(html)
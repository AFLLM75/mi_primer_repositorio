from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import psycopg2.extras

# Create your views here

def form(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="1234")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    prioridad = request.GET.get('get_prioridad', default='%')
    with open("debug.log", "w") as debug_file:
        print(f"SELECT * FROM Nota WHERE prioridad LIKE '{prioridad}';", file=debug_file)
    if prioridad == 'Todas':
        prioridad = '%'
    cursor.execute(F"SELECT * FROM Nota WHERE prioridad LIKE '{prioridad}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'formulario.html', params)

"""
def form(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    prioridad = request.GET.get('get_prioridad', default='%')
    if prioridad == 'Todas':
        prioridad = '%'
    cursor.execute(F"SELECT * FROM Nota WHERE prioridad LIKE '{prioridad}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'formulario.html', params)
"""
"""
def form(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM Nota;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    prioridad = request.GET.get('get_prioridad', default=None)
    params = {'notas': result}
    return render(request, 'formulario.html', params)
"""

def anadir(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    prioridad = request.POST["name_prioridad"]
    titulo= request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]
    cursor.execute(f"INSERT INTO Nota VALUES ('{prioridad}','{titulo}', '{nota}');")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(form)

def borrar(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Nota;")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(form)


"""
def anadir(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    prioridad = request.POST["name_prioridad"]
    titulo= request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]
    cursor.execute(f"INSERT INTO Nota VALUES ('{prioridad}','{titulo}', '{nota}');")
    conn.commit()
    cursor.close()
    conn.close()
    return (HttpResponse(f'<i>Insertado</i><br> '
                         f'<b><u>Prioridad</u>:</b> {prioridad}<br>'
                         f'<b><u>Título</u>:</b> {titulo}<br>'
                         f'<b><u>Nota</u>:</b> {nota}<br>'))

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
"""
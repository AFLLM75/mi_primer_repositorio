import psycopg2
conn = psycopg2.connect(dbname="capitulo_6_db", user="capitulo_6_user", password="patata")
print("Funciona!")
# loops


mi_lista = [1,2,3,4,5,]

for i in mi_lista:
    print("el numero es:", i)

resultado = 0
for i in mi_lista:
   resultado += i

print(f"el resultado de mi lista es: {resultado}")

for i in range(2, 8):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i == "lunes":
     print(f"feliz {i}")

# while loop
i = 0

while i < 5:
   i += 1
   if i == 3:
      continue
   print(i)
   if i == 4:
      break
   
   else:
      print("i es mayor o iguala 5")

#practica 2
#mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]
# imprimir cada elelmnto de la lista 3 veces y cuandon sea lunes no lo incluyas
#pista: usa los dos tipos loops while y for en el mismo programa para lograrlo
#resultado:
#martes
#miercoles
#jueves
#viernes
#martes
#miercoles
#jueves
#viernes

contador = 0

while contador < 2:
   for i in mi_lista_2:
      if i == "lunes":
         continue
      print(i)
   contador += 1



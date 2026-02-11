# numeros 
print(int(7))
print(float(7.7))
print(type(7))
print(type(7.7))
print(int(1+2))
print(int(10*2))
print(int(1 + 4 - 2))
print(float(1 + 2.0))

# operaciones matematicos
# +
# -
# *
# /
# **
# % modulo

print(int(2**3))
print(int(4**8))
print(int(10%3))
print(int(25%4))
print(float(16%2))
print(float(10 / 3))

# variables 
print("=====variables=====")
x = 100
y = 1
print(x + y)

ventas = 1999991
print("nuestras muestras fueron", ventas)

is_activate = True
print(is_activate)

game_over = False
print(game_over)

some_string = "hola soy un string"
print(some_string)

print("=====condicionales======")
edad = 18

if (edad>18):

    print("si puedes entrar al bar")
else:
    print("no puedes entrar al bar")

mi_minumero = int (input("cual es el numero que deseas verificar?: "))
print(f"el numero que deseas verificar es {mi_minumero}")
if mi_minumero % 2 ==0:
    print(f"el numero{mi_minumero}es par")
else:
        print(f"el numero{mi_minumero}es inpar")

def par_inpar(numero):
     if numero %2 ==0:
         print(f"el numero{mi_minumero}es par")
     else:
         print(f"el numero{mi_minumero}es inpar")
print("======funcion par_impar()======")
mi_miumero = int (input("cual es el numero que deseas verificar?: "))
print(par_inpar(mi_minumero))
from enemigo import *
from zombie import *
from ogro import *

zombie1 = Zombie(10, 1)
ogro1 = Ogro(20, 3)

print(f"{zombie1.get_tipo_enemigo()} tiene {zombie1.puntos_energia} de energia y ataca con {zombie1.ataque}")
print(f"{ogro1.get_tipo_enemigo()} tiene {ogro1.puntos_energia} de energia y ataca con {ogro1.ataque}")

def batalla(e1:Enemigo,e2: Enemigo):
    e1.habla() 
    e2.habla()
    while e1.puntos_energia > 0 and e2.puntos_energia > 0:
        print("##############")
        e2.ataque_especial()
        e1.ataque_especial()

        print(f"{e1.get_tipo_enemigo()} ahora: {e1.puntos_energia} puntos de energía!!!")
        print(f"{e2.get_tipo_enemigo()} ahora: {e2.puntos_energia} puntos de energía!!!")
        print(f"Ataque: {e2.ataque}")
        e1.puntos_energia -= e2.ataque
        print("===========")

        print(f"Ataque: {e1.ataque}")
        e2.puntos_energia -= e1.ataque
        print("******")
       
        if e1.puntos_energia > 0:
         print(f"{e1.get_tipo_enemigo()} ganó!!!")

        else:
         print(f"{e2.get_tipo_enemigo()} ganó!!!")
               
               
        print("-----------BATALLA------------")
    batalla(Zombie, Ogro)
    print("-------FIN DE LA BATALLA-------------")
    #print(f"{zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energia y ataca con {zombie.ataque}")
    #print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y ataca con {ogro.ataque}")






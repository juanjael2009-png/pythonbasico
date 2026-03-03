from enemigo import *
import random
class Ogro(Enemigo):
    def ___init__(self, tipo_enemigo, puntos_energia=10, ataque=1):
        super().___init__(tipo_enemigo = "Ogro", puntos_energia=puntos_energia, ataque=ataque)


    def habla(self):
        print("Ogro aplastar todo!!!") 

        def ataque_especial(self):
            print("ogro ataque especial")
            funcion_ataque_especial = random.random() < 0.20
            if funcion_ataque_especial:
                self.ataque += 4
                print("ogro enojado y incremento su ataque por 4")

from enemigo import *
import random

class Zombie(Enemigo):
    def __init__(self, puntos_energia, ataque):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=ataque)

    def hablar(self):
        print("¡Grrrr...!")

    def propagar_enfermedad(self):
        print("El Zombie está tratando de propagar la enfermedad!")

    def ataque_especial(self):
        print("Zombie ataque especial")
        funciona_ataque_especial = random.ramdom() < 0.50
        if funciona_ataque_especial:
            self.puntos_energia += 2
            print("zombie a regresado su energia com HP2")
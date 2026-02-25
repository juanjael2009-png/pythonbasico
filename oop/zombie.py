from enemigo import *

class Zombie(Enemigo):
    def __init__(self, puntos_energia, ataque):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=ataque)

    def hablar(self):
        print("¡Grrrr...!")

    def propagar_enfermedad(self):
        print("El Zombie está tratando de propagar la enfermedad!")

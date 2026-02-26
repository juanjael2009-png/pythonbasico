from enemigo import *

class Ogro(Enemigo):
    def ___init__(self, tipo_enemigo, puntos_energia=10, ataque=1):
        super().___init__(tipo_enemigo = "Ogro", puntos_energia=puntos_energia, ataque=ataque)


    def habla(self):
        print("Ogro aplastar todo!!!")
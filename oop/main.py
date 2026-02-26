from enemigo import *
from zombie import *
from ogro import *

zombie1 = Zombie(10, 1)
ogro1 = Ogro(20, 3)

print(f"{zombie1.get_tipo_enemigo()} tiene {zombie1.puntos_energia} de energia y ataca con {zombie1.ataque}")
print(f"{ogro1.get_tipo_enemigo()} tiene {ogro1.puntos_energia} de energia y ataca con {ogro1.ataque}")

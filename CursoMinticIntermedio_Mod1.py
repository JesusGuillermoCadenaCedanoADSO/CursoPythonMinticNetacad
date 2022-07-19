#importacion de modulos, concepto de namespace
from math import sin, pi

print(sin(pi / 2))
#redefiniendo a pi:
pi = 3.14

#redefiniendo a sin:
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

import math as m
print(m.sin(m.pi/2))

#modulos utiles random
from random import random

for i in range(5):
    print(random())

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))


from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

#modulo platform
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine

print(machine())

from platform import processor

print(processor())

from platform import system

print(system())

from platform import version

print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

# 1.3.1.4 Módulos y Paquetes


import sys

for p in sys.path:
    print(p)

#1.3.1.7.
# para inicializar un paquete debe haber un archivo dentro de la carpeta del paquete
# llamado __init__.py
# El contenido del archivo se ejecuta cuando se importa cualquiera de los modulos del
# paquete. Si no se desea ninguna inicializacion especial se puede dejar el archivo vacio
# pero no se puede omitir

# " 1.4.1.4 Instalador de Paquetes de Python (PIP"

# Repositorio de PyPI: en cmd ejecutar pip --version, pip help, pip help install







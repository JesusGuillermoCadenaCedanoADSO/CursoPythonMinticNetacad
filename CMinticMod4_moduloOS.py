# obtener informacion del sistema operativo
# el módulo os proporciona una función llamada uname,
# que devuelve un objeto que contiene los siguientes atributos:
#
# systemname: almacena el nombre del sistema operativo.
# nodename: almacena el nombre de la máquina en la red.
# release: almacena el release (actualización) del sistema operativo.
# version: almacena la versión del sistema operativo.
# machine: almacena el identificador de hardware, por ejemplo, x86_64.

# la funcion mkdir crea directorios
# si se pasa solo el nombre de directorio como argumento, crea el directorios
# en el directorio de trabajo actual
# La función makedirs permite la creación recursiva de directorios
# chdir cambia de directorio
# listdir lista archivos y directorios dentro del directorio de trabajo
# getcwd devuelve el nombre de directorio actual
# rmdir elimina directorio especificado
# removedirs requiere que se especifique una ruta que contenga
# todos los directorios que deben eliminarse:
# la funcion system() ejecuta un comando que se le pasa como una cadena

import platform
import os
#print(platform.uname())
###os.mkdir("my_first_directory")
###os.makedirs("my_first_directory/my_second_directory")
#os.chdir("my_first_directory")
# print(os.listdir())
# print(os.getcwd())
# os.removedirs("my_first_directory/my_second_directory")
# os.rmdir("my_first_directory")
# print(os.listdir())
#
# returned_value = os.system("mkdir my_first_directory")
# print(returned_value)
os.chdir("tree")
os.chdir('../')
print(os.getcwd())

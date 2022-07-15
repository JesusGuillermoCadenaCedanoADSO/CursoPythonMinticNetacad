# curso mintic intermedio modulo 4
import os
nueva_lista = []


def directorios(path, carpeta):
    for j in list(os.listdir(path)):
        if j.split('/')[-1] == carpeta:
            print(path + "/" + j)
            nueva_lista.append(path + "/" + j)
        directorios(path + "/" + j, carpeta)
    return nueva_lista


print(directorios("./tree", "python"))
print(os.getcwd())
os.chdir('../')
print(os.getcwd())



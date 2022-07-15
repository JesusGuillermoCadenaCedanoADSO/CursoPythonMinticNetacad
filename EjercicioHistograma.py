# curso mintic intermedio modulo 4
from os import strerror

source_file_name = input("Ingresa el nombre del archivo fuente: ")
try:
    source_file = open(source_file_name, 'rt', encoding='utf-8')
    source_file.read(5)
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)


try:
    diccionario = {}
    for line in source_file:
        for char in line:
            if char.isalpha():
                new_char = char.casefold()
                if list(diccionario.keys()).count(new_char) < 1:
                    diccionario[new_char] = 1
                else:
                    diccionario[new_char] += 1

    claves = list(diccionario.keys())
    valores = list(diccionario.values())
    lista_diccionario = list(diccionario.items())
    #ordenamiento con funcion lambda
    lista_ordenada = sorted(lista_diccionario, key=lambda x: x[1], reverse=True)
    #print(lista_ordenada)


except IOError as e:
    print("No se puede llevar a cabo la obtencion de lista ordenada", strerror(e.errno))
    exit(e.errno)


destination_file_name = source_file_name.replace(".txt", ".hist")

try:
    destination_file = open(destination_file_name, 'wt', encoding='utf-8')
except Exception as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    source_file.close()
    exit(e.errno)


for i in range(len(lista_ordenada)):
    destination_file.write(lista_ordenada[i][0] + ' -> ' + str(lista_ordenada[i][1]) + '\n')

source_file.close()
destination_file.close()




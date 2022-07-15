# curso mintic intermedio modulo 4
import io


class StudentsDataException(Exception):
    def __init__(self, nombre_archivo, mensaje):
        Exception.__init__(self, mensaje)
        self.nombre_archivo = nombre_archivo


class FileEmpty(StudentsDataException):
    def __init__(self, nombre_archivo, mensaje, numero_de_caracteres):
        StudentsDataException.__init__(self, nombre_archivo, mensaje)
        self.numero_de_caracteres = numero_de_caracteres


class WrongLine(StudentsDataException):
    def __init__(self, nombre_archivo, linea, mensaje):
        StudentsDataException.__init__(self, nombre_archivo, mensaje)
        self.linea = linea


def verificar_registro_valido(archivo_entrada, linea):
    if len(linea.split()) != 3:
        raise WrongLine(archivo_entrada, linea, "numero de datos invalido")
    record = linea.split()
    score = record[2]
    if not score.replace(".", "", 1).isdigit():
        raise WrongLine(archivo_entrada, linea, "puntaje invalido: " + score)
    name = record[0]
    lastname = record[1]
    return name, lastname, score


def verificar_si_hay_datos(file, numero_de_caracteres):
    if not numero_de_caracteres:
        raise FileEmpty(file, "archivo vacio", numero_de_caracteres)


def verificar_archivo(archivo_entrada, modo_apertura):
    try:
        open(archivo_entrada, modo_apertura).close()
    except FileNotFoundError:
        raise StudentsDataException(archivo_entrada, "El archivo no se puede abrir")
    else:
        try:
            open(archivo_entrada, modo_apertura).read()
        except io.UnsupportedOperation:
            raise StudentsDataException(archivo_entrada,
                                        "archivo no leible (" + modo_apertura+")")
        else:
            print("Se pudo abrir archivo")


# source_file_name = input("Ingresa el nombre del archivo Jekyll: ")
source_file_name = 'ArchivoJekyll_2.txt'
modo = 'rt'
try:
    verificar_archivo(source_file_name, modo)
except StudentsDataException as error_ocurrido:
    print(error_ocurrido, ":", error_ocurrido.nombre_archivo)
else:
    try:
        with open(source_file_name, modo) as archivo:
            verificar_si_hay_datos(source_file_name, len(archivo.readline()))
    except FileEmpty as error_ocurrido:
        print(error_ocurrido, ":", error_ocurrido.nombre_archivo)
    else:
        with open(source_file_name, modo) as source_file:
            diccionario = {}
            nombre_mas_largo = 0
            for line in source_file:
                registro = line.split()
                try:
                    registro = verificar_registro_valido(source_file.name, line)
                except WrongLine as error_ocurrido:
                    print('El registro: ', error_ocurrido.linea, ' en el archivo ',
                          error_ocurrido.nombre_archivo,
                          "genera error: ", error_ocurrido)
                    exit()
                else:
                    nombre = registro[0]
                    apellido = registro[1]
                    puntaje = float(registro[2])
                    nombre_completo = nombre + ' ' + apellido
                    if len(nombre_completo) > nombre_mas_largo:
                        nombre_mas_largo = len(nombre_completo)
                    if list(diccionario.keys()).count(nombre_completo) < 1:
                        diccionario[nombre_completo] = puntaje
                    else:
                        diccionario[nombre_completo] += puntaje
            lista_diccionario = list(diccionario.items())
            lista_diccionario_ordenada = \
                sorted(lista_diccionario, key=lambda x: x[0], reverse=False)
            separador = ("{0:^3s}".format(""))
            for i in lista_diccionario_ordenada:
                texto = (i[0].ljust(nombre_mas_largo)) + separador + str(i[1])
                print(texto)

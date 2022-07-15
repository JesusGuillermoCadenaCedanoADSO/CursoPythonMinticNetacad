# Generadores
# Un generador de Python es un fragmento de código especializado
# capaz de producir una serie de valores y controlar el proceso de iteración
# Un generador devuelve una serie de valores, y en general,
# se invoca (implícitamente) más de una vez.

# serie fibonacci
# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("Fib iter")
#         return self
#
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
#
# class Class:
#     def __init__(self, n):
#         self.__iter = Fib(n)
#
#     def __iter__(self):
#         print("Class iter")
#         return self.__iter
#
#
# object = Class(8)
#
# for i in object:
#     print(i)

# ejemplo de objeto generador fun(n)

# def fun(n):
#     for i in range(n):
#         yield i
#
# for i in fun(4):
#     print(i)
#
# # potencias de 2
#
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
#
#
# for v in powers_of_2(6):
#     print(v)
#
# t = [x for x in powers_of_2(5)]
# print(t)
#
# t = list(powers_of_2(3))
# print(t)
#
# # serie fibonacci
#
# def fibonacci(n):
#     p = pp = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = p + pp
#             pp, p = p, n
#             yield n
#
# fibs = list(fibonacci(10))
# print(fibs)


# 4.1.1.6 Generadores y cierres

# con corchete se crea lista, con parentesis generador
# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
#
# for v in the_list:
#     print(v, end=" ")
# print()
#
# for v in the_generator:
#     print(v, end=" ")
# print()

# Funciones lambda

# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y
#
# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')
#
# print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
#

# la funcion map
# La función map() aplica la función pasada por su primer argumento
# a todos los elementos de su segundo argumento y devuelve un iterador
# que entrega todos los resultados de funciones subsequentes.

# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)
#
# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()

# la funcion filter

# from random import seed, randint
#
# seed()
# data = [randint(-10, 10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
#
# print(data)
# print(filtered)

# def outer(par):
#     loc = par
#
#     def inner():
#         return loc
#     return inner
#
#
# var = 1
# fun = outer(var)
# print(fun())

# tecnica de cierre

# def make_closure(par):
#     loc = par
#
#     def power(p):
#         return p ** loc
#     return power
#
#
# fsqr = make_closure(2)
# fcub = make_closure(3)
#
# for i in range(5):
#     print(i, fsqr(i), fcub(i))

# ejercicios

# class Vowels:
#     def __init__(self):
#         self.vow = "aeiouy "  # Sí, sabemos que y no siempre se considera una vocal.
#         self.pos = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.pos == len(self.vow):
#             raise StopIteration
#         self.pos += 1
#         return self.vow[self.pos - 1]
#
#
# vowels = Vowels()
# for v in vowels:
#     print(v, end=' ')


# def replace_spaces(replacement='*'):
#     def new_replacement(text):
#         return text.replace(' ', replacement)
#     return new_replacement
#
#
# stars = replace_spaces()
# print(stars("And Now for Something Completely Different"))

# Nota:
# las funciones lambdas no deben asignarse a variables, sino
# que deben definirse como funciones
#
# Recomendado:
# def f(x): return 3*x
#
# No recomendado:
# f = lambda x: 3*x

# 4.2.1.1 Procesando archivos

# los nombres de archivo de Windows deben escribirse de la siguiente manera:
#
# name = "\\dir\\file"
#
#
# Afortunadamente, también hay una solución más. Python es
# lo suficientemente inteligente como para poder convertir
# diagonales en diagonales invertidas cada vez que descubre que el
# sistema operativo lo requiere.
#
# Esto significa que cualquiera de las siguientes asignaciones:
#
# name = "/dir/file"
# name = "c:/dir/file"

# El lenguaje de programacion se comunica con el archivo a traves del STREAM
# HANDLE O MANEJADOR.

# Hay tres modos básicos utilizados para abrir un stream:
# Modo lectura (r)
# Modo escritura (w)
# Modo actualizar (permite lectura y escritura)
# El contenido de los stream se divide en tipo texto(t) y tipo binario(b)
# rt lectura
# wt escritura
# at lambda
# r+t lectura y actualizacion
# w+t escritura y actualizacion

# manejo de archivos (module 22%)(section 42%)
# streams predefinidos
# sys.stdin (entrada estandar)
# sys.stdout (salida estandar)
# sys.stderr (salida de error estandar)

# diagnosticando problemas con streams

# try:
#     pass
#     # Algunas operaciones con streams.
# except IOError as exc:
#     print(exc.errno)

#  algunas constantes seleccionadas útiles para detectar errores en los streams:

# errno.EACCES Permiso denegado
# errno.EBADF Número de archivo incorrecto
# errno.EEXIST  Archivo existente
# errno.EFBIG  Archivo demasiado grande
# errno.EISDIR Es un directorio
# errno.EMFILE Demasiados archivos abiertos
# errno.ENOENT El archivo o directorio no existe
# errno.ENOSPC No queda espacio en el dispositivo
# import errno
#
# try:
#     stream = open("file", "rb")
#     print("existe")
#     stream.close()
# except IOError as error:
#     if error.errno == errno.ENOENT:
#         print("ausente")
#     else:
#         print("desconocido")

# Diagnosticando errores con strerror()
# from os import strerror
#
# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # El procesamiento va aquí.
#     s.close()
# except Exception as exc:
#     print("El archivo no pudo ser abierto:", strerror(exc.errno))

# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
# stream = open("tzop.txt", "rt", encoding = "utf-8")
#
# # Se imprime el contenido del archivo:
# print(stream.read())

# from os import strerror
#
# try:
#     counter = 0
#     stream = open('text.txt', "rt", encoding="utf-8")
#     char = stream.read(1)
#     while char != '':
#         print(char, end='')
#         counter += 1
#         char = stream.read(1)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# from os import strerror
#
# try:
#     counter = 0
#     stream = open('text.txt', "rt",encoding = "utf-8")
#     content = stream.read()
#     for char in content:
#         print(char, end='')
#         counter += 1
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerr(e.errno))

# from os import strerror
#
# try:
#     character_counter = line_counter = 0
#     stream = open('text.txt', 'rt',encoding="utf-8")
#     line = stream.readline()
#     while line != '':
#         line_counter += 1
#         for char in line:
#             print(char, end='')
#             character_counter += 1
#         line = stream.readline()
#     stream.close()
#     print("\n\nCaracteres en el archivo:", character_counter)
#     print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# from os import strerror
#
# try:
#     character_counter = line_counter = 0
#     stream = open('text.txt', 'rt',encoding = "utf-8")
#     lines = stream.readlines(20)
#     while len(lines) != 0:
#         for line in lines:
#             line_counter += 1
#             for char in line:
#                 print(char, end='')
#                 character_counter += 1
#         lines = stream.readlines(10)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", character_counter)
#     print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# from os import strerror
#
# try:
# 	character_counter = line_counter = 0
# 	for line in open('text.txt', 'rt',encoding = "utf-8"):
# 		line_counter += 1
# 		for char in line:
# 			print(char, end='')
# 			character_counter += 1
# 	print("\n\nCaracteres en el archivo: ", character_counter)
# 	print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))


# 4.3.1.7 Trabajando con archivos reales module(37%) section(39%)
# from os import strerror
#
# try:
# 	file = open('newtext.txt', 'wt',encoding="utf-8") # Un nuevo archivo (newtext.txt) es creado.
# 	for i in range(10):
# 		s = "línea #" + str(i+1) + "\n"
# 		for char in s:
# 			file.write(char)
# 	file.close()
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))

# from os import strerror
#
# try:
#     file = open('newtext2.txt', 'wt',encoding = "utf-8")
#     for i in range(10):
#         file.write("línea #" + str(i+1) + "\n")
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# bytearrays
# son mutables, solo puede poseer enteros entre 0 y 255

# from os import strerror
#
# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 + i
#
# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# Ingresa aquí el código que lee los bytes del stream.

# from os import strerror
#
# data = bytearray(10)
#
# try:
#     binary_file = open('file.bin', 'rb')
#     binary_file.readinto(data)
#     binary_file.close()
#
#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# con el metodo read() el objeto creado a diferencia del objeto bytearray es inmutable

# from os import strerror
#
# try:
#     binary_file = open('file.bin', 'rb')
#     data = bytearray(binary_file.read())
#     binary_file.close()
#
#     for b in data:
#         print(hex(b), end=' ')
#
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))
#

# Si el método read() se invoca con un argumento,
# se especifica el número máximo de bytes a leer.
#
# from os import strerror
#
# try:
#     binary_file = open('file.bin', 'rb')
#     data = bytearray(binary_file.read(5))
#     binary_file.close()
#
#     for b in data:
#         print(hex(b), end=' ')
#
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# codigo que copia archivos bin

# from os import strerror
#
# source_file_name = input("Ingresa el nombre del archivo fuente: ")
# try:
#     source_file = open(source_file_name, 'rb')
# except IOError as e:
#     print("No se puede abrir archivo fuente: ", strerror(e.errno))
#     exit(e.errno)
#
# destination_file_name = input("Ingresa el nombre del archivo destino: ")
# try:
#     destination_file = open(destination_file_name, 'wb')
# except Exception as e:
#     print("No se puede crear el archivo de destino:", strerror(e.errno))
#     source_file.close()
#     exit(e.errno)
#
# buffer = bytearray(65536)
# total = 0
# try:
#     readin = source_file.readinto(buffer)
#     while readin > 0:
#         written = destination_file.write(buffer[:readin])
#         total += written
#         readin = source_file.readinto(buffer)
# except IOError as e:
#     print("No se puede crear el archivo de destino: ", strerror(e.errno))
#     exit(e.errno)
#
# print(total, 'byte(s) escritos con éxito')
# source_file.close()
# destination_file.close()
#
# Leer contenido de archivo llamado image.png
# y almacenarlo en una variable bytearray llamada image

# try:
#     stream = open("image.png", "rb")
#     image = bytearray(stream.read())
#     stream.close()
# except IOError:
#     print("fallido")
# else:
#     print("exitoso")

# 4.5.1.1. El modulo datetime

# Una de las clases proporcionadas por el módulo
# datetime es una clase llamada date. Los objetos de esta
# clase representan una fecha que consta de año, mes y día.

# En Unix, la marca de tiempo expresa el número de segundos
# desde el 1 de Enero de 1970 a las 00:00:00 (UTC).

# El módulo datetime proporciona varios métodos
# para crear un objeto date. Uno de ellos es el método fromisoformat,
# que toma una fecha en el formato AAAA-MM-DD compatible con el estándar ISO 8601.

# metodo replace
# from datetime import date
#
# d = date(1991, 2, 5)
# print(d)
#
# d = d.replace(year=1992, month=1, day=16)
# print(d)

# d = date(2019, 11, 4)
# print(d.weekday())

# clase time
# from datetime import time
#
# t = time(14, 53, 20, 1)
#
# print("Tiempo:", t)
# print("Hora:", t.hour)
# print("Minuto:", t.minute)
# print("Segundo:", t.second)
# print("Microsegundo:", t.microsecond)

# modulo time
# import time
#
# class Student:
#     def take_nap(self, seconds):
#         print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
#         time.sleep(seconds)
#         print("¡Dormí bien! ¡Me siento genial!")
#
# student = Student()
# student.take_nap(5)

# funcion ctime
# import time
# convierte el tiempo en segundos desde el 1 de enero de 1970 (época Unix) en una cadena
#
# timestamp = 1572879180
# print(time.ctime(timestamp))

# funciones gmtime y localtime
# import time
#
# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))

# funciones asctime y mktime

# import time
#
# timestamp = 1572879180
# st = time.gmtime(timestamp)
#
# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

# creacion de objetos datetime

# from datetime import datetime
#
# dt = datetime(2019, 11, 4, 14, 53)
#
# print("Fecha y Hora:", dt)
# print("Fecha:", dt.date())
# print("Hora:", dt.time())

# obtener fecha y hora actuales
# from datetime import datetime
#
# print("hoy:", datetime.today())
# print("ahora:", datetime.now())
# print("utc_ahora:", datetime.utcnow())

# obtener marca de tiempo
# from datetime import datetime
#
# dt = datetime(2020, 10, 4, 14, 55)
# print("Marca de tiempo:", dt.timestamp())

# formato de fecha y Hora
# from datetime import time
# from datetime import date
# from datetime import datetime
#
# d = date(2020, 1, 4)
# print(d.strftime('%Y/%m/%d'))
# t = time(14, 53)
# print(t.strftime("%H:%M:%S"))
#
# dt = datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%y/%B/%d %H:%M:%S"))

# La funcion strftime en el modulo time

# import time
#
# timestamp = 1572879180
# st = time.gmtime(timestamp)
#
# print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# # a continuacion hace el formateo usando la hora actual
# print(time.strftime("%Y/%m/%d %H:%M:%S"))

# el metodo strptime()
# import time
# from datetime import datetime
# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
# print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# operaciones con fecha y hora
# objeto timedelta se crea haciendo resta entre objetos date o datetime

# from datetime import date
# from datetime import datetime
#
# d1 = date(2020, 11, 4)
# d2 = date(2019, 11, 4)
#
# print(d1 - d2)
#
# dt1 = datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime(2019, 11, 4, 14, 53, 0)
#
# print(dt1 - dt2)

# crear objeto timedelta
# from datetime import timedelta
# from datetime import date
# from datetime import datetime
#
# delta = timedelta(weeks=2, days=2, hours=3)
# print("Días:", delta.days)
# print("Segundos:", delta.seconds)
# print("Microsegundos:", delta.microseconds)

# delta = timedelta(weeks=2, days=2, hours=2)
# print(delta)
#
# delta2 = delta * 2
# print(delta2)
#
# d = date(2019, 10, 4) + delta2
# print(d)
#
# dt = datetime(2019, 10, 4, 14, 53) + delta2
# print(dt)

# 4.5.1.22 LABORATORIO: Los módulos datetime y time

# from datetime import datetime
# from datetime import date
# import time
#
# d = datetime(2020, 11, 4, 14, 53)
# print(d.strftime('%Y/%m/%d %H:%M:%S'))
# print(d.strftime('%y/%B/%d %H:%M:%S %p'))
# print(d.strftime('%a, %Y %b %d'))
# print(d.strftime('%A, %Y %B %d'))
# print("Día de la semana: " + d.strftime('%w'))
# print("Día del año: " + d.strftime('%j'))
# print("Número de semana en el año: " + d.strftime('%W'))
#
# fecha = "2020/11/04 14:53:00"
# print("año: ", datetime.strptime(fecha, "%Y/%m/%d %H:%M:%S").year)
#
# timestamp = time.time()
# d = date.fromtimestamp(timestamp)
# print(d)
#
# dt1 = datetime(2022, 9, 21, 15, 38, 0)
# dt2 = datetime(2020, 8, 29, 14, 41, 0)
#
# print(dt1 - dt2)

# 4.6.1.2 El modulo calendar

# import calendar
# print(calendar.calendar(2020))
# calendar.prcal(2021)
#
# print(calendar.month(2020, 11))
#
# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2020, 12)
#
# print(calendar.weekday(2020, 12, 24))
#
# print(calendar.weekheader(2))
#
# print(calendar.isleap(2020))
# print(calendar.leapdays(2010, 2021))
#


# calendar.Calendar: proporciona métodos para preparar datos de calendario y dar formato.
# calendar.TextCalendar: se utiliza para crear calendarios de texto regulares.
# calendar.HTMLCalendar: se utiliza para crear calendarios HTML.
# calendar.LocalTextCalendar: es una subclase de la clase calendar.TextCalendar.
# El constructor de esta clase toma el parámetro locale,
# el cual se utiliza para devolver los nombres apropiados de los meses y días de la semana.
# calendar.LocalHTMLCalendar: es una subclase de la clase calendar.
# HTMLCalendar. El constructor de esta clase toma el parámetro "locale",
# que se usa para devolver los nombres apropiados de los meses y días de la semana.

# import calendar
# c = calendar.Calendar(calendar.SUNDAY)
#
# for weekday in c.iterweekdays():
#     print(weekday, end=" ")

# import calendar
# c = calendar.Calendar()
#
# for date in c.itermonthdates(2019, 11):
#     print(date, end=" ")

# for iter in c.itermonthdays(2019, 11):
#     print(iter, end=" ")

# for data in c.monthdays2calendar(2020, 12):
#     print(data)

# 4.6.1.13 LABORATORIO: El módulo calendar

# import calendar
# cal = calendar.isleap(2019)
# print(cal)
#
#
# MyCalendar = calendar.Calendar(firstweekday=0)
#
#
# def count_weekday_in_year(year, weekday):
#     days = ["Monday", "Tuesday", "Wednesday",
#             "Thursday", "Friday", "Saturday",
#             "Sunday"]
#     contador = 0
#     for mes in range(1, 13):
#         for data in MyCalendar.monthdays2calendar(year, mes):
#             for tupla in data:
#                 if tupla[0] != 0:
#                     if weekday == tupla[1]:
#                         contador += 1
#     return "The day " + days[weekday] + \
#            " occurs " + str(contador) + " times in the year " + \
#            str(year)
#
#
# print(count_weekday_in_year(2019, 0))

# from datetime import date
#
# date_1 = date(1992,1,16)
# date_2 = date(1991,2,5)
# print(date_1-date_2)

import calendar
c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday,end=" ")
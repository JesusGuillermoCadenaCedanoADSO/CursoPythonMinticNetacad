#modulo 1
#2.6.1.11 LABORATORIO: Operadores y expresiones
# hour = int(input("Hora de inicio (horas): "))
# mins = int(input("Minuto de inicio (minutos): "))
# dura = int(input("Duración del evento (minutos): "))


# Escribe tu código aqui.
# hora = (dura+mins)//60
# minutos = ((dura+mins) % 60)
# nueva_hora = (hora+hour) % 24
# print(nueva_hora, ":", minutos)

#modulo 3
#3.2.1.15 LABORATORIO: Hipótesis de Collatz
# numero = 1023
# pasos = 0
# while numero != 1:
#     if numero % 2 == 0:
#         pasos += 1
#         numero = numero / 2
#     else:
#         pasos += 1
#         numero = numero * 3 + 1
#     print(int(numero))
# print("pasos = ", pasos)

# flag_register = 0x1234
# the_mask = 8
# flag_register = flag_register & ~the_mask
# flag_register &= ~the_mask
# flag_register = flag_register ^ the_mask
# flag_register ^= the_mask
#
# print(flag_register)
#
# print(~4)
#
# variable_1 = 1
# variable_2 = 2
# variable_2 = variable_1
# variable_1 = variable_2
#
# print(variable_1)
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)
#
# for i in range(1):
#     print("#")
# else:
#     print("#")
#
# var = 0
# while var < 6:
#     var +=1
#     if var%2==0:
#         continue
#     print("X")
#
# list = [1,2,3]
# print(len(list))
# for v in range(len(list)):
#     list.insert(1,list[v])
# print(list)


# t = [[3-i for i in range (3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
#
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

#Examen modulo 4
#item
# tup = (1,2,4,8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)
# #item
# dictionary = {'one':'two','three':'one', 'two':'three'}
# v= dictionary['three']
# for k in range(len(dictionary)):
#     v = dictionary[v]
# print(v)
# #item
# dictionary = {}
# my_list = ['a','b','c','d']
# largo = len(my_list)
# for i in range(largo-1):
#     dictionary[my_list[i]]= (my_list[i],)
# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])
#     print(k)
# #item
# my_list = ['Mary', 'had', 'a', 'little', 'lamb']
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
# print(my_list(my_list))

#EXAMEN DE SECCION

# X=3
# Y=2
# X= X%Y
# X=X%Y
# Y=Y%X
# print(Y)
# print(hola)

# try:
#     print(5/0)
#     break
# except:
#     print(1)
# except (ValueError, ZeroDivisionError):
#     print(2)
#

# fpp = (1,2,3)
# fpp.index(0)

# lst = [[x for x in range(3)] for y in range(3)]
#
# for r in range(3):
#     for c in range(3):
#         if lst[r][c]%2 !=0:
#             print("X")

# lst = [i for i in range(-1,-2)]
# print(len(lst))

#print(None*None)

#print=1

# def func(a,b):
#     return a+b
#
# print(func(b=2,2))

# dct = {}
# dct['1']=(1,2)
# dct['2']=(2,1)
# for x in dct.keys():
#     print(dct[x][1], end="")

# my_list=[x*x for x in range(5)]
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
#
# print(fun(my_list))

# my_list=[1,2]
# for v in range(2):
#     my_list.insert(-1,my_list[v])
# print(my_list)

# 3.4.1.12 La clase Timer

# from datetime import time, timedelta
#
#
# class Timer:
#     def __init__(self, horas=0, minutos=0, segundos=0):
#         self.horas = horas
#         self.minutos = minutos
#         self.segundos = segundos
#         self.tiempo = segundos + minutos * 60 + horas * 3600
#
#     def nueva_hora(self):
#         self.horas = self.tiempo // 3600
#         self.minutos = (self.tiempo % 3600) // 60
#         self.segundos = (self.tiempo % 3600) % 60
#
#     def __str__(self):
#         return str(self.horas).zfill(2) + \
#                ":" + str(self.minutos).zfill(2) + \
#                ":" + str(self.segundos).zfill(2)
#
#     def next_second(self):
#         self.tiempo += 1
#         self.nueva_hora()
#
#     def prev_second(self):
#         self.tiempo -= 1
#         self.nueva_hora()
#         print("dif_tiempo:", self.tiempo)
#
#
# timer = Timer(3, 59, 00)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)
#
# hora_minut_segundo = time(timer.horas, timer.minutos, timer.segundos)
# print(hora_minut_segundo)
#
# hora_minut_segundo_2 = time(timer.horas, timer.minutos, timer.segundos)
#
# diferencia = timedelta(hours=timer.horas, minutes=timer.minutos, seconds=timer.segundos) \
#              - timedelta(seconds=1)
#
# diferencia_segundos = diferencia.seconds
# print(diferencia_segundos)

# 3.4.1.14 Puntos en un plano



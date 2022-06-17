# import math
# for name in dir(math):
#     print(name, end="\t")
#
# from platform import processor, version, system
#
# print("\n",processor())
# print("\n",version())
# print("\n",system())
#
# result = math.e != math.pow(2,4)
# print(int(result))

# print("".join(["omicron", "pi", "rho"]))
# print("www.cisco.com".lstrip("w.co"))
#
# s = 'Es fácil o imposible'
# s = s.replace('fácil', 'difícil').replace('im', '')
# print(s)

# # 2.3.1.18 tu propio split
# cadena_prueba = " Ser o no ser, esa es la pregunta "
# cadena_prueba_modificada = cadena_prueba.strip()
# palabra = ''
# nueva_lista = []
# cuenta = 0
# for letra in cadena_prueba_modificada:
#     cuenta += 1
#     if not letra.isspace():
#         palabra += letra
#         print(palabra)
#     else:
#         nueva_lista.append(palabra)
#         palabra = ''
#     if cuenta == len(cadena_prueba_modificada) and palabra != '':
#         nueva_lista.append(palabra)
# print(nueva_lista)
#
# print(ord('0')+ord('1')+ord('0'))
# print(ord('1')+ord('0'))

# s1 = '¿Dónde están las nevadas de antaño?'
# s2 = s1.split()
# print(s2)
# s3 = sorted(s2)
# print(s3)
# print(s3[1])

# s1 = '12.8'
# i = float(s1)
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)

# Cifrado César.
# text = input("Ingresa tu mensaje: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)
# print(cipher)
#
# #Procesador de numeros
# line = input("Ingresa una línea de números, sepáralos con espacios: ")
# strings = line.split()
# total = 0
# respuesta = False
# try:
#     for substr in strings:
#         if substr.isalnum():
#             total += float(substr)
#             respuesta = True
#         else:
#             continue
#     if respuesta:
#         print("El total es:", total)
#     else:
#         print("no ingreso numeros")
# except:
#     print(substr, "no es un numero.")

# Validador IBAN
# iban = 'GB72 HBZU 7006 7212 1253 00'
# iban = iban.replace(' ','')
#
# if not iban.isalnum():
#     print("Has introducido caracteres no válidos.")
# elif len(iban) < 15:
#     print("El IBAN ingresado es demasiado corto.")
# elif len(iban) > 31:
#     print("El IBAN ingresado es demasiado largo.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("El IBAN ingresado es válido.")
#     else:
#         print("El IBAN ingresado no es válido.")

# 2.6.1.9 Errores: el pan diario del programador | try-except
# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print("No puedes dividir entre cero, lo siento.")
# except ValueError:
#     print("Debes ingresar un valor entero.")
# except:
#     print("Oh cielos, algo salió mal...")
#
# print("FIN.")
#
# def bad_fun(n):
#     try:
#         return 1 / n
#     except ArithmeticError:
#         print("¡Problema Aritmético!")
#     return None
# bad_fun(0)
# print("FIN.")
#
#
# def bad_fun(n):
#     raise ZeroDivisionError
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¿Que pasó? ¿Un error?")
# print("FIN.")
#
#
# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("¡Lo hice otra vez!")
#         raise
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¡Ya veo!")
# print("FIN.")
#
#
# import math
# x = float(input("Ingresa un número: "))
# assert x >= 0.0
# x = math.sqrt(x)
# print(x)

## 2.8.1.4 Leer enteros de forma segura
## opcion 1
# def read_int(prompt, min, max):
#     global numero
#     numero = input(prompt)
#     valido = False
#     while not valido:
#         try:
#             numero = int(numero)
#             assert -10 < numero < 10
#             valido = True
#         except ValueError:
#             print("Error: entrada incorrecta")
#             read_int(prompt,min,max)
#         except AssertionError:
#             print("Error: el valor no está dentro del rango permitido")
#             read_int(prompt, min, max)
#         return numero
#
# v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)
#
# print("El número es:", v)

## opcion 2 mejorada
def read_int(prompt, min, max):
    while True:
        try:
            numero = int(input(prompt))
            assert min < numero < max
        except ValueError:
           print("Error: entrada incorrecta")
           continue
        except AssertionError:
            print("Error: el valor no está dentro del rango permitido")
            continue
        except:
            print("Algo salio mal")
            break

        return numero


v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)
print("El número es:", v)




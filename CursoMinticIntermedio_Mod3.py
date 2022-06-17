# class TheSimplestClass:
#     pass
#
# my_first_object = TheSimplestClass()

# #####################
# class Stack:  # Definiendo la clase de la pila.
#     def __init__(self):  # Definiendo la función del constructor.
#         print("¡Hola!")
#
# stack_object = Stack()  # Instanciando el objeto.
# #####################

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def get_sum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__counter = 0
#
#     def get_counter(self):
#         return self.__counter
#
#     def pop(self):
#         self.__counter += 1
#         Stack.pop(self)
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())
#
#
# stack_object = Stack()
# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)
#
# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())
#
# class Queue:
#     def __init__(self):
#         self.__lista = []
#
#     def put(self, elem):
#         self.__lista.append(elem)
#
#     def get(self):
#         val = self.__lista[0]
#         del self.__lista[0]
#         return val
#
#     def largo_lista(self):
#         return len(self.__lista)
#
# class SuperQueue(Queue):
#     def __init__(self):
#         Queue.__init__(self)
#
#     def isempty(self):
#         if (self.largo_lista()) > 0:
#             return False
#         return True
#
# class QueueError(Queue):  # Eligir la clase base para la nueva excepción.
#     def __init__(self):
#         Queue.__init__(self)
#
# que = SuperQueue()
# que.put(1)
# que.put("perro")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Cola vacía")
#
#
# que = QueueError()
# que.put(1)
# que.put("perro")
# que.put(False)
#
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Error de Cola")
#

# variables de instancia

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val
#
#     def set_second(self, val):
#         self.__second = val
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
#
# example_object_2.set_second(3)
#
# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
# print(example_object_1._ExampleClass__first)

# Variables de clase: una variable de clase siempre presenta el mismo valor
# en todas las instancias de clase

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
#
# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

# diferencia entre variable de objeto y variable de instacia
# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val
#         # mirar la diferencia con esta linea:
#         #self.varia = val
#
#
# print(ExampleClass.__dict__)
# example_object = ExampleClass(2)
#
# print(ExampleClass.__dict__)
# print(example_object.__dict__)

# comprobando la existencia de un atributo con funcion hasattr

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
# print(example_object.a)
#
# if hasattr(example_object, 'b'):
#     print(example_object.b)
#
#
# class ExampleClass:
#     attr = 1
#
#
# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'prop'))

# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2
#
#
# example_object = ExampleClass()
#
# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))


# # 3.4.1.2 POO: Métodos
#
# # El parámetro self es usado para obtener acceso a la instancia del objeto
# # y las variables de clase.
#
# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)
#     def other(self):
#         print("otro")
#         self.method()
#
# obj = Classy()
# obj.var = 3
# obj.method()
# obj.other()
#
# # metodo oculto
#
# class Classy:
#     def visible(self):
#         print("visible")
#
#     def __hidden(self):
#         print("oculto")
#
#
# obj = Classy()
# obj.visible()
#
# try:
#     obj.__hidden()
# except:
#     print("fallido")
#
# obj._Classy__hidden()
#
#
# # vida interna de clases y objetos
#
# class Classy:
#     varia = 1
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
#
# obj = Classy()
#
# print(obj.__dict__)
# print(Classy.__dict__)
#
# class Classy:
#     pass
#
#
# print(Classy.__name__)
# obj = Classy()
# print(type(obj).__name__)
# print(obj.__module__)
#
# # Introspección, que es la capacidad de un programa para examinar el tipo
# # o las propiedades de un objeto en tiempo de ejecución.
# # Reflexión, que va un paso más allá, y es la capacidad de un programa
# # para manipular los valores, propiedades y/o funciones de un objeto en tiempo de ejecución.

# class MyClass:
#     pass
#
#
# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5
#
#
# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)

# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)


# class Snake:
#     pass
#
#
# class Python(Snake):
#     pass
#
#
# print(Python.__name__, 'es una', Snake.__name__)
# print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)


# 3.4.1.12 La clase Timer
# from datetime import time, timedelta
# class Timer:
#     def __init__(self, horas=0, minutos=0, segundos=0):
#         self.__horas = horas
#         self.__minutos = minutos
#         self.__segundos = segundos
#         self.__tiempo = segundos + minutos * 60 + horas * 3600
#
#     def nueva_hora(self):
#         self.__horas = self.__tiempo // 3600
#         self.__minutos = (self.__tiempo % 3600) // 60
#         self.__segundos = (self.__tiempo % 3600) % 60
#
#     def __str__(self):
#         return str(self.__horas).zfill(2) + \
#                ":" + str(self.__minutos).zfill(2) + \
#                ":" + str(self.__segundos).zfill(2)
#
#     def next_second(self):
#         self.__tiempo += 1
#         self.nueva_hora()
#
#     def prev_second(self):
#         self.__tiempo -= 1
#         self.nueva_hora()
#         print("dif_tiempo:", self.__tiempo)
#
#
# timer = Timer(3, 59, 00)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)
#
# hora_minut_segundo = time(timer._Timer__horas, timer._Timer__minutos, timer._Timer__segundos)
# print(hora_minut_segundo)
#
# hora_minut_segundo_2 = time(timer._Timer__horas, timer._Timer__minutos, timer._Timer__segundos)
#
# diferencia = timedelta(hours=timer._Timer__horas, minutes=timer._Timer__minutos,
#                        seconds=timer._Timer__segundos) \
#              - timedelta(seconds=1)
#
# diferencia_segundos = diferencia.seconds
# print(diferencia_segundos)

# 3.5.1.4. Herencia: issubclass()

# class Vehicle:
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class TrackedVehicle(LandVehicle):
#     pass
#
#
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()
# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()
#
# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()


# Herencia operador Is

# class SampleClass:
#     def __init__(self, val):
#         self.val = val
#
#
# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1
#
# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)
#
# string_1 = "Mary tenía un "
# string_2 = "Mary tenía un corderito"
# string_1 += "corderito"
#
# print(string_1 == string_2, string_1 is string_2)

# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "Mi nombre es " + self.name + "."
#
#
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#
#
# obj = Sub("Andy")
#
# print(obj)

# uso de función super()
#
# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "Mi nombre es " + self.name + "."
#
#
# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)
#
#
# obj = Sub("Andy")
#
# print(obj)
#
# Probando propiedades: variables de clase.
# class Super:
#     supVar = 1
#
#
# class Sub(Super):
#     subVar = 2
#
#
# obj = Sub()
#
# print(obj.subVar)
# print(obj.supVar)

# Probando propiedades: variables de instancia.
# class Super:
#     def __init__(self):
#         self.supVar = 11
#
#
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12
#
#
# obj = Sub()
#
# print(obj.subVar)
# print(obj.supVar)

# Ejemplo con Herencia de 3 niveles
# class Level1:
#     variable_1 = 100
#
#     def __init__(self):
#         self.var_1 = 101
#
#     def fun_1(self):
#         return 102
#
#
# class Level2(Level1):
#     variable_2 = 200
#
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#
#     def fun_2(self):
#         return 202
#
#
# class Level3(Level2):
#     variable_3 = 300
#
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#
#     def fun_3(self):
#         return 302
#
#
# obj = Level3()
#
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

# Ejemplo simple con herencias multiples
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
#
#
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
#
#
# class Sub(SuperA, SuperB):
#     pass
#
#
# obj = Sub()
#
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())
#
# Ejemplo de anulacion de entidades:
# class Level1:
#     var = 100
#     def fun(self):
#         return 101
#
#
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
#
#
# class Level3(Level2):
#     pass
#
#
# obj = Level3()
#
# print(obj.var, obj.fun())

# busqueda de componentes entre clases:
# Podemos decir que Python busca componentes de objetos en el siguiente orden:
#
# Dentro del objeto mismo.
# En sus superclases, de abajo hacia arriba.
# Si hay más de una clase en una ruta de herencia, Python las escanea de izquierda a derecha.

# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"
#
#
# class Right:
#     var = "R"
#     var_right = "RR"
#     def fun(self):
#         return "Right"
#
#
# class Sub(Left, Right):
#     pass
#
#
# obj = Sub()
#
# print(obj.var, obj.var_left, obj.var_right, obj.fun())

# Ejemplo de jerarquia de clases

# class One:
#     def do_it(self):
#         print("do_it de One")
#
#     def doanything(self):
#         self.do_it()
#
#
# class Two(One):
#     def do_it(self):
#         print("do_it de Two")
#
#
# one = One()
# two = Two()
#
# one.doanything()
# two.doanything()

# composicion de objetos
# La herencia extiende las capacidades de una clase agregando
# nuevos componentes y modificando los existentes; en otras palabras,
# la receta completa está contenida dentro de la clase misma y todos sus ancestros;
# el objeto toma todas las pertenencias de la clase y las usa.
# La composición proyecta una clase como contenedor capaz de almacenar
# y usar otros objetos (derivados de otras clases) donde cada uno
# de los objetos implementa una parte del comportamiento de una clase.

# import time
#
# class Tracks:
#     def change_direction(self, left, on):
#         print("pistas: ", left, on)
#
#
# class Wheels:
#     def change_direction(self, left, on):
#         print("ruedas: ", left, on)
#
#
# class Vehicle:
#     def __init__(self, controller):
#         self.controller = controller
#
#     def turn(self, left):
#         self.controller.change_direction(left, True)
#         time.sleep(0.25)
#         self.controller.change_direction(left, False)
#
#
# wheeled = Vehicle(Wheels())
# tracked = Vehicle(Tracks())
#
# wheeled.turn(True)
# tracked.turn(False)

# 3.5.1.20 Fundamentos de POO: MRO

# class Top:
#     def m_top(self):
#         print("top")
#
#
# class Middle(Top):
#     def m_middle(self):
#         print("middle")
#
#
# class Bottom(Middle, Top):
#     def m_bottom(self):
#         print("bottom")
#
#
# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()

# El problema del diamante

# class Top:
#     def m_top(self):
#         print("top")
#
#
# class Middle_Left(Top):
#     def m_middle(self):
#         print("middle_left")
#
#
# class Middle_Right(Top):
#     def m_middle(self):
#         print("middle_right")
#
#
# class Bottom(Middle_Left, Middle_Right):
#     def m_bottom(self):
#         print("bottom")
#
#
# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()

# 3.5.1.22 RESUMEN DE SECCIÓN 1/2

# 3.6.1.1 Excepciones una vez más

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         return None
#     else:
#         print("Todo salió bien")
#         return n
#
#
# print(reciprocal(2))
# print(reciprocal(0))

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("División fallida")
#         n = None
#     else:
#         print("Todo salió bien")
#     finally:
#         print("Es momento de decir adiós")
#         return n
#
#
# print(reciprocal(2))
# print(reciprocal(0))


# Crear tu propia excepción
# class MyZeroDivisionError(ZeroDivisionError):
#     pass
#
#
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("peores noticias")
#     else:
#         raise ZeroDivisionError("malas noticias")
#
#
# for mode in [False, True]:
#     try:
#         do_the_division(mode)
#     except MyZeroDivisionError:
#         print('Mi división entre cero')
#     except ZeroDivisionError:
#         print('División entre cero original')
#
# se puede crear una jerarquia de excepciones personalizada para un problema
# especifico:

# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         Exception.__init__(self, message)
#         self.pizza = pizza
#
#
# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         PizzaError.__init__(self, pizza, message)
#         self.cheese = cheese
#
#
# def make_pizza(pizza, cheese):
#     if pizza not in ['margherita', 'capricciosa', 'calzone']:
#         raise PizzaError(pizza, "no hay tal pizza en el menú")
#     if cheese > 100:
#         raise TooMuchCheeseError(pizza, cheese, "demasiado queso")
#     print("¡Pizza lista!")
#
#
# for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
#     try:
#         make_pizza(pz, ch)
#     except TooMuchCheeseError as tmce:
#         print(tmce, ':', tmce.cheese)
#     except PizzaError as pe:
#         print(pe, ':', pe.pizza)

# Evaluacion
#1
# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self, msg + msg)
#         self.args = (msg,)
#
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)


#
#2
# class A:
#     def __init__(self,v):
#         self.__a = v+1
#
# a = A(0)
# print(a.__a)

#3
#
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
#
# print(issubclass(C,A))
#
# #4
# class A:
#     def __str__(self):
#         return 'a'
# class B(A):
#     def __str__(self):
#         return 'b'
#
# class C(B):
#     pass
# o=C()
# print(o)
#
# #5
#
# class A:
#     v=2
# class B(A):
#     v=1
#
# class C(B):
#     pass
#
# o = C()
# print(o.v)

#6

# class A:
#     x=0
#     def __init__(self, v=0):
#         self.Y=v
#         A.x +=v
# a = A()
# b = A(1)
# c = A(2)
# print(c.x)


#7
# class I:
#     def __init__(self):
#         self.s='abc'
#         self.i=0
#
#         def __iter__(self):
#         return self
#
#         def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i +=1
#         return v
#
# for x in I():
#     print(x, end='')
#

# 9
# class A:
#     def __init__(self,v=1):
#         self.v=v
#
#     def set(self,v):
#         self.v=v
#         return v
#
# a = A()
# print(a.set(a.v + 1))

# 11
# def f(x):
#     try:
#         x = x/x
#     except:
#         print("a",end='')
#     else:
#         print("b",end='')
#     finally:
#         print("c",end='')
#
# f(1)
# f(0)

#13
# class A:
#     def __str__(self):
#         return 'a'
#
# class B:
#     def __str__(self):
#         return 'b'
#
# class C(A,B):
#     pass
#
# o=C()
# print(o)

#14

# class A:
#     def __init__(self):
#         pass
# a = A(1)
# print(hasattr(a,'A'))

#15
#
# class A:
#     def a(self):
#         print('a')
#
# class B:
#     def a(self):
#         print('b')
#
# class C(B,A):
#     def c(self):
#             self.a()
#
# o=C()
# o.c()


#16
#
# class A:
#     A=1
# print(hasattr(A,'A'))

#11
# def f(x):
#     try:
#         x=x/x
#     except:
#         print("a",end='')
#     else:
#         print("b", end='')
#     finally:
#         print("c",end='')
# f(1)
# f(0)

#9
# class A:
#     def __init__(self,v=1):
#         self.v=v
#     def set(self,v):
#         self.v=v
#         return v
#
# a=A()
# print(a.set(a.v+1))


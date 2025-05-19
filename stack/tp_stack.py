# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.
# from random import randint

from stack import Stack
from typing import Any, Optional, List
# number_stack = Stack()
# ocurrencias = 0 


# for i in range(100):
#     rand_number = randint(1, 10)
#     print(rand_number)
#     number_stack.push(rand_number)

# buscado = int(input("Ingrese un numero a buscar en la pila: "))

# while number_stack.size() > 0:
#     number = number_stack.pop()
#     if number == buscado:
#         ocurrencias += 1        

# # print(f"Se encontro : {ocurrencias}  veces")


# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:

from dataclasses import dataclass

from dataclasses import dataclass

# dataclass para contruir la clase con inicializador y otros metodos 
@dataclass
class IronManSuit:
    modelo: str
    pelicula: str
    estado: str 

suits_stack = Stack()

suits_stack.push(IronManSuit("Mark III", "Iron Man", "Dañado"))
suits_stack.push(IronManSuit("Mark V", "Iron Man 2", "Destruido"))
suits_stack.push(IronManSuit("Mark XLIV", "Avengers: Age of Ultron", "Impecable"))  # Hulkbuster
suits_stack.push(IronManSuit("Mark XLVI", "Captain America: Civil War", "Dañado"))
suits_stack.push(IronManSuit("Mark XLVII", "Spider-Man: Homecoming", "Impecable"))

# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
# además mostrar el nombre de dichas películas;
def buscar_hulkbuster(stack: Stack):
    aux = Stack()
    encontrado = False

    print("Películas donde se usó el Hulkbuster (Mark XLIV):")
    while stack.size():
        traje = stack.pop()
        if traje.modelo == "Mark XLIV":
            print(f"- {traje.pelicula}")
            encontrado = True
        aux.push(traje)

    while aux.size():
        stack.push(aux.pop())

    if not encontrado:
        print("No se encontró el modelo Mark XLIV.")

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
def mostrar_daniados(stack: Stack):
    aux = Stack()
    print("Modelos dañados:")
    while stack.size():
        traje = stack.pop()
        if traje.estado == "Dañado":
            print(f"- {traje.modelo} ({traje.pelicula})")
        aux.push(traje)

    while aux.size():
        stack.push(aux.pop())

# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
def eliminar_destruidos(stack: Stack):
    aux = Stack()
    print("Modelos eliminados (Destruidos):")
    while stack.size():
        traje = stack.pop()
        if traje.estado == "Destruido":
            print(f"- {traje.modelo} ({traje.pelicula})")
            continue  # No lo volvemos a apilar
        aux.push(traje)

    while aux.size():
        stack.push(aux.pop())

# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película;
def agregar_modelo_sin_repetir(stack: Stack, nuevo_traje: IronManSuit):
    aux = Stack()
    repetido = False

    while stack.size():
        traje = stack.pop()
        if traje.modelo == nuevo_traje.modelo and traje.pelicula == nuevo_traje.pelicula:
            repetido = True
        aux.push(traje)

    while aux.size():
        stack.push(aux.pop())

    if not repetido:
        stack.push(nuevo_traje)
        print(f"Se agregó: {nuevo_traje.modelo} en {nuevo_traje.pelicula}")
    else:
        print("Ya existía ese modelo en esa película. No se agregó.")

# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.
def mostrar_trajes_por_pelicula(stack: Stack, peliculas: list[str]):
    aux = Stack()
    print("Trajes utilizados en las películas indicadas:")
    while stack.size():
        traje = stack.pop()
        if traje.pelicula in peliculas:
            print(f"- {traje.modelo} ({traje.pelicula})")
        aux.push(traje)

    while aux.size():
        stack.push(aux.pop())



# if __name__ == "__main__":
#     buscar_hulkbuster(suits_stack)
#     mostrar_daniados(suits_stack)
#     eliminar_destruidos(suits_stack)
#     agregar_modelo_sin_repetir(suits_stack,
#                                 IronManSuit("Mark LXXXV", 
#                                             "Avengers: Endgame", 
#                                             "Impecable"))
#     mostrar_trajes_por_pelicula(suits_stack, 
#                                 ["Spider-Man: Homecoming", 
#                                  "Captain America: Civil War"])


# 14_ Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.

def ordenar_pila(stack: Stack) -> Stack:
    aux_stack = Stack()

    while stack.size() > 0:
        temp = stack.pop()

        while aux_stack.size() > 0 and aux_stack.on_top() > temp:
            stack.push(aux_stack.pop())

        aux_stack.push(temp)

    return aux_stack


# if __name__ == "__main__":
#     p = Stack()
#     p.push(5)
#     p.push(1)
#     p.push(4)
#     p.push(2)
#     p.push(3)

#     print("Pila original:")
#     p.show()
    
#     ordenada = ordenar_pila(p)
#     print("\nPila ordenada de forma creciente:")
#     ordenada.show()


# 15. Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def partition(arr: List[int], start: int, end: int) -> int:
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort_iterative(arr: List[int]) -> None:
    stack = Stack()
    stack.push((0, len(arr) - 1))

    while stack.size() > 0:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot_index = partition(arr, start, end)

        if pivot_index + 1 < end:
            stack.push((pivot_index + 1, end))

        if start < pivot_index - 1:
            stack.push((start, pivot_index - 1))


# if __name__ == "__main__":
#     arreglo = [10, 7, 8, 9, 1, 5]
#     print("Antes:", arreglo)
#     quicksort_iterative(arreglo)
#     print("Después:", arreglo)


# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

def intersection(stack1: Stack, stack2: Stack) -> Stack:
    set1 = set()
    
    # Vaciar stack1 y guardar en set para poder usar funcion IN
    while stack1.size() > 0:
        set1.add(stack1.pop())

    result = Stack()

    # Vaciar stack2, si está en set1, guardar en resultado
    while stack2.size() > 0:
        val = stack2.pop()
        if val in set1:
            result.push(val)

    return result

# if __name__ == "__main__":
#     episodioV = Stack()
#     episodioV.push("Luke Skywalker")
#     episodioV.push("Darth Vader")
#     episodioV.push("Yoda")
#     episodioV.push("Han Solo")

#     episodioVII = Stack()
#     episodioVII.push("Rey")
#     episodioVII.push("Finn")
#     episodioVII.push("Han Solo")
#     episodioVII.push("Darth Vader")

#     interseccion = intersection(episodioV, episodioVII)

#     print("Personajes en ambos episodios:")
#     while interseccion.size() > 0:
#         print(interseccion.pop())

# 17. Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonan-
# tes y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego
# utilizando las operaciones de pila resolver las siguientes consignas:
# a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
# b. cantidad de espacios en blanco;
# c. porcentaje que representan las vocales respecto de las consonantes sobre el total de carac-
# teres del párrafo;
# d. cantidad de números;
# e. determinar si la cantidad de vocales y otros caracteres son iguales;
# f. determinar si existe al menos una z en la pila de consonantes.


def clasificar_parrafo(parrafo: str):
    vocales_stack = Stack()
    consonantes_stack = Stack()
    otros_stack = Stack()

    for ch in parrafo.lower():  
        if ch in "aeiou":
            vocales_stack.push(ch)
        elif ch.isalpha():
            consonantes_stack.push(ch)
        else:
            otros_stack.push(ch)

    return vocales_stack, consonantes_stack, otros_stack

def analizar_pilas(vocales: Stack, consonantes: Stack, otros: Stack):
    cant_vocales = 0
    cant_consonantes = 0
    cant_otros = 0
    espacios = 0
    numeros = 0
    contiene_z = False

# a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
# b. cantidad de espacios en blanco;
    while vocales.size() > 0:
        vocales.pop()
        cant_vocales += 1

    while consonantes.size() > 0:
        letra = consonantes.pop()
        cant_consonantes += 1
        # f. determinar si existe al menos una z en la pila de consonantes.
        if letra == 'z':
            contiene_z = True

    while otros.size() > 0:
        ch = otros.pop()
        cant_otros += 1
        if ch == ' ':
            espacios += 1
        # d. cantidad de números;    
        if ch.isdigit():
            numeros += 1

    # c. porcentaje que representan las vocales respecto de las consonantes sobre el total de carac-
    # teres del párrafo;
    if cant_consonantes > 0:
        porcentaje = (cant_vocales / cant_consonantes) * 100
    else:
        porcentaje = 0

    print("a) Cantidad de vocales:", cant_vocales)
    print("   Cantidad de consonantes:", cant_consonantes)
    print("   Cantidad de otros caracteres:", cant_otros)
    print("b) Espacios en blanco:", espacios)
    print("c) Porcentaje de vocales respecto de consonantes: {:.2f}%".format(porcentaje))
    print("d) Cantidad de números:", numeros)
    # e. determinar si la cantidad de vocales y otros caracteres son iguales;
    print("e) Vocales y otros son iguales:", cant_vocales == cant_otros)
    print("f) ¿Existe al menos una 'z'?:", contiene_z)

# if __name__ == "__main__":
#     parrafo = "Luke Skywalker tiene 2 sables, y Han Solo tiene 1. Ambos están en la batalla final."
#     vocales, consonantes, otros = clasificar_parrafo(parrafo)
#     analizar_pilas(vocales, consonantes, otros)



# 18. Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejem-
# plo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del
# objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras ex-
# tras, no se pueden utilizar métodos de ordenamiento.

@dataclass
class ObjetoOficina:
    nombre: str
    peso: float

    def __repr__(self):
        return f"{self.nombre} ({self.peso} kg)"


def ordenar_por_peso(pila: Stack) -> Stack:
    ordenada = Stack()

    while pila.size() > 0:
        actual = pila.pop()

        temp = Stack()

        while (ordenada.size() > 0 and ordenada.on_top().peso > actual.peso):
            temp.push(ordenada.pop())

        ordenada.push(actual)

        while temp.size() > 0:
            ordenada.push(temp.pop())

    return ordenada

# if __name__ == "__main__":
#     pila_objetos = Stack()
#     pila_objetos.push(ObjetoOficina("monitor", 3.0))
#     pila_objetos.push(ObjetoOficina("teclado", 0.5))
#     pila_objetos.push(ObjetoOficina("silla", 7.0))
#     pila_objetos.push(ObjetoOficina("mouse", 0.2))
#     pila_objetos.push(ObjetoOficina("CPU", 4.0))

#     ordenada = ordenar_por_peso(pila_objetos)

#     print("Pila ordenada (más liviano abajo, más pesado arriba):")
#     while ordenada.size() > 0:
#         print(ordenada.pop())

# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
# treno, desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.


@dataclass
class Pelicula:
    titulo: str
    estudio: str
    anio: int

    def __repr__(self):
        return f"{self.titulo} ({self.estudio}, {self.anio})"

def mostrar_peliculas_2014(pila: Stack):
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula.anio == 2014:
            print(pelicula)

def contar_peliculas_2018(pila: Stack) -> int:
    contador = 0
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula.anio == 2018:
            contador += 1
    return contador

def mostrar_marvel_2016(pila: Stack):
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula.estudio.lower() == "marvel studios" and pelicula.anio == 2016:
            print(pelicula)

# if __name__ == "__main__":
#     pila = Stack()
#     pila.push(Pelicula("Capitán América: Civil War", "Marvel Studios", 2016))
#     pila.push(Pelicula("Interstellar", "Paramount Pictures", 2014))
#     pila.push(Pelicula("Guardianes de la Galaxia", "Marvel Studios", 2014))
#     pila.push(Pelicula("Black Panther", "Marvel Studios", 2018))
#     pila.push(Pelicula("Infinity War", "Marvel Studios", 2018))

#     # Como las funciones consumen la pila, usamos una copia para cada una
#     import copy
#     pila_2014 = copy.deepcopy(pila)
#     pila_2018 = copy.deepcopy(pila)
#     pila_marvel_2016 = copy.deepcopy(pila)

#     print("Películas de 2014:")
#     mostrar_peliculas_2014(pila_2014)

#     print("\nCantidad de películas en 2018:")
#     print(contar_peliculas_2018(pila_2018))

#     print("\nPelículas de Marvel Studios en 2016:")
#     mostrar_marvel_2016(pila_marvel_2016)


# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

class Robot:
    def __init__(self):
        self.movimientos = Stack()
        self.posicion = [0, 0]  

    def mover(self, pasos: int, direccion: str):
        self.movimientos.push((pasos, direccion))
        print(f"Avanzó {pasos} paso(s) hacia {direccion}")
        

    def volver_al_inicio(self):
        print("\nVolviendo al punto de partida...\n")
        while self.movimientos.size() > 0:
            pasos, direccion = self.movimientos.pop()
            direccion_inversa = self.__invertir_direccion(direccion)
            print(f"Retrocede {pasos} paso(s) hacia {direccion_inversa}")
    
    def __invertir_direccion(self, direccion: str) -> str:
        inversa = {
            "norte": "sur", "sur": "norte",
            "este": "oeste", "oeste": "este",
            "noreste": "suroeste", "suroeste": "noreste",
            "noroeste": "sureste", "sureste": "noroeste"
        }
        return inversa.get(direccion, "desconocida")
    
# if __name__ == "__main__":
#     robot = Robot()
#     robot.mover(3, "norte")
#     robot.mover(2, "este")
#     robot.mover(1, "sureste")
#     robot.volver_al_inicio()

# 21. Realizar un algoritmo que ingrese en una pila los dos valores iniciales de la sucesión de Fi-
# bonacci –o condiciones de fin de forma recursiva– y a partir de estos calcular los siguientes
# valores de dicha sucesión, hasta obtener el valor correspondiente a un número n ingresado por
# el usuario.
def fibonacci_pila_recursiva(pila: Stack, n: int): 
    if pila.size() >= n:
        return
    
    ultimo = pila.pop()
    penultimo = pila.pop()

    siguiente = ultimo + penultimo

    pila.push(penultimo)
    pila.push(ultimo)
    pila.push(siguiente)

    fibonacci_pila_recursiva(pila, n)

# if __name__ == "__main__":
#     n = 10
#     fib_stack = Stack()
#     # Ingresamos los dos valores iniciales de la sucesión, por ejemplo 0 y 1
#     fib_stack.push(0)
#     fib_stack.push(1)

#     fibonacci_pila_recursiva(fib_stack, n)

#     print("Sucesión de Fibonacci calculada con pila y recursión:")
#     fib_stack.show()



# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
# Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
# costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
# de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
# quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
# que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

@dataclass
class Bitacora:
    planeta: str
    capturado: str
    costo: int

class Cazarrecompensas:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.misiones = Stack()

    def agregar_mision(self, bitacora: Bitacora):
        self.misiones.push(bitacora)

    def mostrar_planetas(self):
        print(f"Planetas visitados por {self.nombre}:")
        aux = Stack()
        while self.misiones.size() > 0:
            mision = self.misiones.pop()
            print(mision.planeta)
            aux.push(mision)
        while aux.size() > 0:
            self.misiones.push(aux.pop())

    def total_creditos(self) -> int:
        total = 0
        aux = Stack()
        while self.misiones.size() > 0:
            mision = self.misiones.pop()
            total += mision.costo
            aux.push(mision)
        while aux.size() > 0:
            self.misiones.push(aux.pop())
        return total

    def contar_capturas(self) -> int:
        return self.misiones.size()

    def buscar_mision_captura(self, nombre_capturado: str) -> int:
        # Retorna la posición desde el fondo de la pila
        aux = Stack()
        posicion = 0
        encontrada_posicion = -1  # -1 si no se encontró

        # Primero volcamos todo a aux para contar posiciones desde fondo
        while self.misiones.size() > 0:
            aux.push(self.misiones.pop())

        # Ahora aux tiene el fondo arriba, contamos y revisamos
        while aux.size() > 0:
            posicion += 1
            mision = aux.pop()
            if mision.capturado == nombre_capturado and encontrada_posicion == -1:
                encontrada_posicion = posicion
            self.misiones.push(mision)

        return encontrada_posicion


# if __name__ == "__main__":
#     # Creamos los cazarrecompensas
#     boba = Cazarrecompensas("Boba Fett")
#     din = Cazarrecompensas("Din Djarin")

#     # Cargamos misiones ejemplo para Boba Fett
#     boba.agregar_mision(Bitacora("Tatooine", "Han Solo", 5000))
#     boba.agregar_mision(Bitacora("Kashyyyk", "Chewbacca", 3000))
#     boba.agregar_mision(Bitacora("Endor", "Ewok", 1000))

#     # Cargamos misiones para Din Djarin
#     din.agregar_mision(Bitacora("Nevarro", "Cliente X", 4000))
#     din.agregar_mision(Bitacora("Tatooine", "Cliente Y", 2500))

#     # a) Mostrar planetas visitados
#     boba.mostrar_planetas()
#     din.mostrar_planetas()

#     # b) Total créditos y quién ganó más
#     total_boba = boba.total_creditos()
#     total_din = din.total_creditos()
#     print(f"\nTotal créditos Boba Fett: {total_boba}")
#     print(f"Total créditos Din Djarin: {total_din}")

#     if total_boba > total_din:
#         print("Boba Fett obtuvo mayor fortuna.")
#     elif total_din > total_boba:
#         print("Din Djarin obtuvo mayor fortuna.")
#     else:
#         print("Ambos obtuvieron la misma fortuna.")

#     # c) Número de misión en que Boba Fett capturó a Han Solo
#     pos = boba.buscar_mision_captura("Han Solo")
#     print(f"\nPosición desde el fondo de la pila de la misión donde Boba Fett capturó a Han Solo: {pos}")

#     # d) Cantidad de capturas
#     print(f"\nCapturas Boba Fett: {boba.contar_capturas()}")
#     print(f"Capturas Din Djarin: {din.contar_capturas()}")



# 23. Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
# obtener la siguiente información sin perder los datos:
# a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
# b. calcular el promedio de temperatura (o media) del total de valores;
# c. determinar la cantidad de valores por encima y por debajo de la media.

class MesTemperaturas:
    def __init__(self):
        self.temperaturas = Stack()

    def agregar_temperatura(self, temp: float):
        self.temperaturas.push(temp)

    def obtener_info(self):
        aux = Stack()
        minimo = None
        maximo = None
        suma = 0.0
        contador = 0

        # Primero recorremos para obtener min, max y suma
        while self.temperaturas.size() > 0:
            temp = self.temperaturas.pop()
            if (minimo is None) or (temp < minimo):
                minimo = temp
            if (maximo is None) or (temp > maximo):
                maximo = temp
            suma += temp
            contador += 1
            aux.push(temp)

        # Restauramos la pila original
        while aux.size() > 0:
            self.temperaturas.push(aux.pop())

        if contador == 0:
            return None  # No hay datos

        promedio = suma / contador

        # Contamos valores por encima y debajo del promedio
        encima = 0
        debajo = 0

        while self.temperaturas.size() > 0:
            temp = self.temperaturas.pop()
            if temp > promedio:
                encima += 1
            elif temp < promedio:
                debajo += 1
            aux.push(temp)

        # Restauramos la pila original
        while aux.size() > 0:
            self.temperaturas.push(aux.pop())

        return {
            "minimo": minimo,
            "maximo": maximo,
            "promedio": promedio,
            "por_encima": encima,
            "por_debajo": debajo
        }


if __name__ == "__main__":
    mes = MesTemperaturas()

    # Ejemplo: temperaturas promedio del mes de abril (30 días)
    datos_ejemplo = [
        18.5, 20.0, 19.8, 21.2, 22.1, 18.9, 17.5, 16.8, 19.0, 20.5,
        21.5, 22.8, 23.0, 21.0, 19.5, 18.7, 17.9, 16.2, 15.8, 17.0,
        18.3, 19.7, 20.2, 21.1, 20.0, 19.9, 19.6, 18.4, 17.2, 16.5
    ]

    for temp in datos_ejemplo:
        mes.agregar_temperatura(temp)

    info = mes.obtener_info()

    if info:
        print(f"Temperatura mínima: {info['minimo']}")
        print(f"Temperatura máxima: {info['maximo']}")
        print(f"Promedio mensual: {info['promedio']:.2f}")
        print(f"Días con temperatura por encima del promedio: {info['por_encima']}")
        print(f"Días con temperatura por debajo del promedio: {info['por_debajo']}")
    else:
        print("No hay datos de temperatura.")

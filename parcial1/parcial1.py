### MENU AL FINAL PARA PROBAR LOS 2 EJERCICIOS ###


# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# a) funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# b) funcion recursiva para listar los superheroes de la lista


superheroes_corta = [
    "Iron Man", "Spider-Man", "Thor", "Hulk", "Black Widow",
    "Hawkeye", "Doctor Strange", "Black Panther", "Wolverine",
    "Deadpool", "Ant-Man", "Vision", "Scarlet Witch", "Falcon",
    "Capitan America"  
]

# A)
def esta_capitan_america(lista):
    if not lista:
        return False
    if lista[0] == "Capitan America":
        return True
    return esta_capitan_america(lista[1:])

# B)
def listar_superheroes(lista):
    if not lista:
        return
    print(lista[0])
    listar_superheroes(lista[1:])


# Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
# A-Listado ordenado de manera ascendente por nombre de los personajes.
# B-Determinar en que posicion esta The Thing y Rocket Raccoon.
# C-Listar todos los villanos de la lista.
# D-Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# E-Listar los superheores que comienzan con  Bl, G, My, y W.
# F-Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# E-Listado de superheroes ordenados por fecha de aparación.
# H-Modificar el nombre real de Ant Man a Scott Lang.
# I-Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# J-Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from super_heroes_data import superheroes
from List_ import List
from Queue_ import Queue

# Funciones de criterio
def get_name(p):
    return p["name"]

def get_real_name(p):
    return str(p["real_name"]) 

def get_first_appearance(p):
    return p["first_appearance"]

# Funciones
def listado_ordenado_por_nombre(lista):
    lista.sort_by_criterion("name")
    lista.show()

def posicion_de_personaje(lista, nombre):
    index = lista.search(nombre, "name")
    return index

def listar_villanos(lista):
    villanos = []
    for personaje in lista:
        if personaje["is_villain"]:
            villanos.append(personaje)
    return List(villanos)

def villanos_pre_1980(lista_personajes):
    cola_villanos = Queue()
    for personaje in lista_personajes:
        if personaje["is_villain"]:  
            cola_villanos.arrive(personaje)

    villanos_antiguos = Queue()
    while cola_villanos.size() != 0:
        villano = cola_villanos.attention()
        if villano["first_appearance"] < 1980:
            villanos_antiguos.arrive(villano)

    return villanos_antiguos

def listar_por_prefijo(lista, prefijos):
    personajes_filtrados = []
    for personaje in lista:
        for prefijo in prefijos:
            if personaje["name"].startswith(prefijo):
                personajes_filtrados.append(personaje)
    return personajes_filtrados

def listado_por_nombre_real(lista):
    lista.add_criterion("real_name", get_real_name)  
    lista.sort_by_criterion("real_name")
    lista.show()

def listado_por_fecha_aparicion(lista):    
    lista.add_criterion("first_appearance", get_first_appearance)
    lista.sort_by_criterion("first_appearance")
    lista.show()

def modificar_nombre_real(lista, nombre, nuevo_nombre_real):
    index = lista.search(nombre, "name")
    if index is not None:
        lista[index]["real_name"] = nuevo_nombre_real
        return True
    return False

def personajes_con_palabras(lista, palabras):
    resultado = []
    for p in lista:
        bio = p["short_bio"].lower()
        if any(palabra in bio for palabra in palabras):
            resultado.append(p)
    return resultado

def eliminar_personajes(lista, nombres):
    eliminados = []
    for nombre in nombres:
        eliminado = lista.delete_value(nombre, "name")
        if eliminado:
            eliminados.append(eliminado)
    return eliminados


# MENÚ
if __name__ == "__main__":
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ejercicio 1: Lista simple de superhéroes")
        print("2. Ejercicio 2: Lista de personajes de Marvel")
        print("X. Salir")
        seleccion = input("Elegí una opción: ").upper()

        if seleccion == "1":
            print("\n--- EJERCICIO 1 ---")
            if esta_capitan_america(superheroes_corta):
                print("Capitan America está en la lista.")
            else:
                print("Capitan America NO está en la lista.")
            print("\nLista de superhéroes:")
            listar_superheroes(superheroes_corta)

        elif seleccion == "2":           
            superheroes = List(superheroes)
            superheroes.add_criterion("name", get_name)
            superheroes.add_criterion("real_name", get_real_name)
            superheroes.add_criterion("first_appearance", get_first_appearance)

            while True:
                print("\n--- MENÚ DE OPCIONES EJERCICIO 2  ---")
                print("A. Listado ordenado por nombre")
                print("B. Buscar posición de The Thing y Rocket Raccoon")
                print("C. Listar villanos")
                print("D. Villanos que aparecieron antes de 1980")
                print("E. Listar personajes con prefijo Bl, G, My, W")
                print("F. Listado por nombre real")
                print("G. Listado por fecha de aparición")
                print("H. Cambiar nombre real de Ant Man a Scott Lang")
                print("I. Buscar personajes con 'time-traveling' o 'suit' en la biografía")
                print("J. Eliminar a Electro y Baron Zemo")
                print("Z. Volver al menú principal")
                opcion = input("Elegí una opción: ").upper()

                if opcion == "A":
                    listado_ordenado_por_nombre(superheroes)
                elif opcion == "B":
                    pos1 = posicion_de_personaje(superheroes, "The Thing")
                    pos2 = posicion_de_personaje(superheroes, "Rocket Raccoon")
                    print(f"The Thing está en la posición {pos1}")
                    print(f"Rocket Raccoon está en la posición {pos2}")
                elif opcion == "C":
                    villanos = listar_villanos(superheroes)
                    villanos.show()
                elif opcion == "D":
                    villanos = listar_villanos(superheroes)
                    antiguos = villanos_pre_1980(villanos)
                    antiguos.show()
                elif opcion == "E":
                    filtrados = listar_por_prefijo(superheroes, ["Bl", "G", "My", "W"])
                    for f in filtrados:
                        print(f)
                elif opcion == "F":
                    listado_por_nombre_real(superheroes)
                elif opcion == "G":
                    listado_por_fecha_aparicion(superheroes)
                elif opcion == "H":
                    if modificar_nombre_real(superheroes, "Ant Man", "Scott Lang"):
                        print("Nombre real actualizado.")
                    else:
                        print("No se encontró a Ant Man.")
                elif opcion == "I":
                    encontrados = personajes_con_palabras(superheroes, ["time-traveling", "suit"])
                    for p in encontrados:
                        print(p)
                elif opcion == "J":
                    eliminados = eliminar_personajes(superheroes, ["Electro", "Baron Zemo"])
                    for e in eliminados:
                        print("Eliminado:", e)
                    if not eliminados:
                        print("No se encontraron esos personajes.")
                elif opcion == "Z":
                    break
                else:
                    print("Opción inválida. Intentá de nuevo.")
        
        elif seleccion == "X":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")
from typing import Any, Optional, Callable
from List_ import List

# --- Ejercicio 6 --- 
class Superheroe:
    def __init__(self, nombre: str, anio_aparicion: int, casa: str, biografia: str):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"Nombre: {self.nombre}, Año: {self.anio_aparicion}, "
                f"Casa: {self.casa}, Bio: {self.biografia}")


# --- Funciones criterio ---

def criterio_nombre(superheroe):
    return superheroe.nombre

def criterio_anio(superheroe):
    return superheroe.anio_aparicion


# --- Cargar datos ---
heroes = List([
    Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo y un traje especial."),
    Superheroe("Wolverine", 1974, "Marvel", "Garras de adamantium."),
    Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo con túnica mágica."),
    Superheroe("Iron Man", 1963, "Marvel", "Utiliza una armadura avanzada."),
    Superheroe("Capitana Marvel", 1968, "Marvel", "Poderosa guerrera con traje."),
    Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con armadura."),
    Superheroe("Flash", 1940, "DC", "Velocidad extrema."),
    Superheroe("Star-Lord", 1976, "Marvel", "Líder con traje espacial."),
    Superheroe("Batman", 1939, "DC", "Héroe con traje de murciélago."),
    Superheroe("Spider-Man", 1962, "Marvel", "Joven con traje arácnido."),
    Superheroe("Magneto", 1963, "Marvel", "Controla el magnetismo."),
    Superheroe("Superman", 1938, "DC", "Traje azul y capa roja.")
])

# Agregar criterios
heroes.add_criterion("nombre", criterio_nombre)
heroes.add_criterion("anio", criterio_anio)


# --- Funciones por punto ---

def a_eliminar_linterna_verde():
    heroes.delete_value("Linterna Verde", "nombre")

def b_anio_wolverine():
    index = heroes.search("Wolverine", "nombre")
    if index is not None:
        print("Wolverine apareció en:", heroes[index].anio_aparicion)

def c_cambiar_casa_strange():
    index = heroes.search("Dr. Strange", "nombre")
    if index is not None:
        heroes[index].casa = "Marvel"

def d_heroes_con_traje_armadura():
    print("Héroes con 'traje' o 'armadura':")
    for h in heroes:
        if "traje" in h.biografia.lower() or "armadura" in h.biografia.lower():
            print(h.nombre)

def e_heroes_antes_1963():
    print("Héroes con aparición antes de 1963:")
    for h in heroes:
        if h.anio_aparicion < 1963:
            print(f"{h.nombre} ({h.casa})")

def f_casa_capitana_y_mujer_maravilla():
    for name in ["Capitana Marvel", "Mujer Maravilla"]:
        index = heroes.search(name, "nombre")
        if index is not None:
            print(f"{name} pertenece a: {heroes[index].casa}")

def g_info_flash_y_starlord():
    for name in ["Flash", "Star-Lord"]:
        index = heroes.search(name, "nombre")
        if index is not None:
            print(heroes[index])

def h_heroes_con_BMS():
    print("Héroes que empiezan con B, M o S:")
    for h in heroes:
        if h.nombre[0] in "BMS":
            print(h.nombre)

def i_cantidad_por_casa():
    conteo = {"Marvel": 0, "DC": 0}
    for h in heroes:
        if h.casa in conteo:
            conteo[h.casa] += 1
    print("Cantidad por casa:")
    for casa, cantidad in conteo.items():
        print(f"{casa}: {cantidad}")


# --- Ejecución ---

print("a. Eliminar Linterna Verde")
a_eliminar_linterna_verde()

print("\nb. Año de aparición de Wolverine")
b_anio_wolverine()

print("\nc. Cambiar casa de Dr. Strange")
c_cambiar_casa_strange()

print("\nd. Superhéroes con 'traje' o 'armadura'")
d_heroes_con_traje_armadura()

print("\ne. Superhéroes anteriores a 1963")
e_heroes_antes_1963()

print("\nf. Casa de Capitana Marvel y Mujer Maravilla")
f_casa_capitana_y_mujer_maravilla()

print("\ng. Info Flash y Star-Lord")
g_info_flash_y_starlord()

print("\nh. Héroes que comienzan con B, M, S")
h_heroes_con_BMS()

print("\ni. Cantidad de superhéroes por casa")
i_cantidad_por_casa()


# --- Ejercicio  22--- 

class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie):
        self.nombre = nombre
        self.maestros = maestros  # lista de nombres
        self.colores_sable = colores_sable  # lista de colores
        self.especie = especie

    def __str__(self):
        return (f"Nombre: {self.nombre}, Maestros: {self.maestros}, "
                f"Colores sable: {self.colores_sable}, Especie: {self.especie}")


def criterio_nombre(jedi):
    return jedi.nombre

def criterio_especie(jedi):
    return jedi.especie


jedis = List([
    Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "azul", "blanco"], "togruta"),
    Jedi("Kit Fisto", ["Yoda"], ["verde"], "nautolano"),
    Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde", "azul"], "humano"),
    Jedi("Anakin Skywalker", ["Obi-Wan Kenobi", "Qui-Gon Jin"], ["azul"], "humano"),
    Jedi("Qui-Gon Jin", ["Conde Dooku"], ["verde"], "humano"),
    Jedi("Mace Windu", ["Cyslin Myr"], ["violeta"], "humano"),
    Jedi("Yoda", [], ["verde"], "desconocida"),
    Jedi("Aayla Secura", ["Quinlan Vos"], ["azul"], "twi'lek"),
    Jedi("Rey", ["Luke Skywalker", "Leia Organa"], ["azul", "amarillo"], "humano"),
    Jedi("Plo Koon", ["Tyvokka"], ["azul", "amarillo"], "kel dor"),
    Jedi("Depa Billaba", ["Mace Windu"], ["verde"], "humano"),
    Jedi("Obi-Wan Kenobi", ["Qui-Gon Jin", "Yoda"], ["azul"], "humano"),
])


jedis.add_criterion("nombre", criterio_nombre)
jedis.add_criterion("especie", criterio_especie)

# --- a. Listado ordenado por nombre y por especie ---
def a_listado_ordenado():
    print("Ordenado por nombre:")
    jedis.sort_by_criterion("nombre")
    for jedi in jedis:
        print(jedi.nombre)
    print("\nOrdenado por especie:")
    jedis.sort_by_criterion("especie")
    for jedi in jedis:
        print(f"{jedi.nombre} ({jedi.especie})")

# --- b. Mostrar info de Ahsoka Tano y Kit Fisto ---
def b_info_ahsoka_kit():
    for name in ["Ahsoka Tano", "Kit Fisto"]:
        idx = jedis.search(name, "nombre")
        if idx is not None:
            print(jedis[idx])

# --- c. Mostrar padawans de Yoda y Luke Skywalker ---
def c_padawans_yoda_luke():
    for maestro in ["Yoda", "Luke Skywalker"]:
        print(f"Padawans de {maestro}:")
        for jedi in jedis:
            if maestro in jedi.maestros:
                print(jedi.nombre)

# --- d. Jedi humanos y twi'lek ---
def d_humano_twilek():
    print("Jedi humanos y twi'lek:")
    for jedi in jedis:
        if jedi.especie in ["humano", "twi'lek"]:
            print(jedi.nombre, f"({jedi.especie})")

# --- e. Jedi que comienzan con A ---
def e_jedi_con_A():
    print("Jedi que comienzan con A:")
    for jedi in jedis:
        if jedi.nombre.startswith("A"):
            print(jedi.nombre)

# --- f. Jedi con más de un color de sable ---
def f_mas_de_un_color():
    print("Jedi con más de un color de sable:")
    for jedi in jedis:
        if len(jedi.colores_sable) > 1:
            print(jedi.nombre, jedi.colores_sable)

# --- g. Jedi con sable amarillo o violeta ---
def g_amarillo_violeta():
    print("Jedi con sable amarillo o violeta:")
    for jedi in jedis:
        if "amarillo" in jedi.colores_sable or "violeta" in jedi.colores_sable:
            print(jedi.nombre, jedi.colores_sable)

# --- h. Padawans de Qui-Gon Jin y Mace Windu ---
def h_padawans_qui_mace():
    for maestro in ["Qui-Gon Jin", "Mace Windu"]:
        print(f"Padawans de {maestro}:")
        encontrados = False
        for jedi in jedis:
            if maestro in jedi.maestros:
                print(jedi.nombre)
                encontrados = True
        if not encontrados:
            print("Ninguno")

# --- Ejecución ---
print("\n--- a ---")
a_listado_ordenado()
print("\n--- b ---")
b_info_ahsoka_kit()
print("\n--- c ---")
c_padawans_yoda_luke()
print("\n--- d ---")
d_humano_twilek()
print("\n--- e ---")
e_jedi_con_A()
print("\n--- f ---")
f_mas_de_un_color()
print("\n--- g ---")
g_amarillo_violeta()
print("\n--- h ---")
h_padawans_qui_mace()
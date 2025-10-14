from Queue_  import *
from Stack import *

# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

def eliminar_facebook(cola: Queue):
    for _ in range(cola.size()):
        noti = cola.attention()
        if noti["app"] != "Facebook":
            cola.arrive(noti)

def mostrar_twitter_python(cola: Queue):
    for _ in range(cola.size()):
        noti = cola.move_to_end()
        if noti["app"] == "Twitter" and "Python" in noti["mensaje"]:
            print(noti)

#pasamos a minutos para poder hacer la comparacion
def hora_a_minutos(hora: str) -> int:
    h, m = map(int, hora.split(":"))
    return h * 60 + m

def almacenar_en_rango(cola: Queue) -> Stack:
    pila = Stack()
    for _ in range(cola.size()):
        noti = cola.move_to_end()
        minutos = hora_a_minutos(noti["hora"])
        if 703 <= minutos <= 957:  # 11:43 = 703 min, 15:57 = 957 min
            pila.push(noti)
    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {pila.size()}")
    return pila


# if __name__ == "__main__":
#     cola = Queue()

#     cola.arrive({"hora": "11:45", "app": "Twitter", "mensaje": "Python 3.12 is out!"})
#     cola.arrive({"hora": "10:00", "app": "Facebook", "mensaje": "Nueva historia de tu amigo"})
#     cola.arrive({"hora": "14:30", "app": "Instagram", "mensaje": "Nueva foto de tu contacto"})
#     cola.arrive({"hora": "12:00", "app": "Facebook", "mensaje": "Recordatorio de evento"})
#     cola.arrive({"hora": "13:15", "app": "Twitter", "mensaje": "Curso gratuito de Python"})

#     # a) Eliminar notificaciones de Facebook
#     eliminar_facebook(cola)

#     # b) Mostrar notificaciones de Twitter que mencionen "Python"
#     print("Twitter + Python:")
#     mostrar_twitter_python(cola)

#     # c) Apilar notificaciones entre 11:43 y 15:57
#     pila_resultado = almacenar_en_rango(cola)
#     print("Contenido de la pila:")
#     pila_resultado.show()

# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

def mostrar_por_planetas(cola: Queue, planetas: list[str]):
    print(f"Personajes de los planetas {planetas}:")
    for _ in range(cola.size()):
        personaje = cola.move_to_end()
        if personaje["planeta"] in planetas:
            print(f"{personaje['nombre']} ({personaje['planeta']})")

def mostrar_planeta_de(cola: Queue, nombres: list[str]):
    for _ in range(cola.size()):
        personaje = cola.move_to_end()
        if personaje["nombre"] in nombres:
            print(f"{personaje['nombre']} es de {personaje['planeta']}")

def insertar_antes_de(cola: Queue, nombre_objetivo: str, nuevo_personaje: dict):
    nueva_cola = Queue()
    insertado = False

    while cola.size() > 0:
        actual = cola.attention()
        if not insertado and actual["nombre"] == nombre_objetivo:
            nueva_cola.arrive(nuevo_personaje)
            insertado = True
        nueva_cola.arrive(actual)

    # Restaurar la cola original con el nuevo personaje insertado
    while nueva_cola.size() > 0:
        cola.arrive(nueva_cola.attention())

def eliminar_despues_de(cola: Queue, nombre_objetivo: str):
    nueva_cola = Queue()
    eliminar = False

    while cola.size() > 0:
        actual = cola.attention()
        if eliminar:
            # Omitimos este personaje (lo eliminamos)
            eliminar = False
            continue
        nueva_cola.arrive(actual)
        if actual["nombre"] == nombre_objetivo:
            eliminar = True

    # Restaurar la cola sin el personaje eliminado
    while nueva_cola.size() > 0:
        cola.arrive(nueva_cola.attention())

# if __name__ == "__main__":
#     cola = Queue()
#     cola.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
#     cola.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
#     cola.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
#     cola.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
#     cola.arrive({"nombre": "Chewbacca", "planeta": "Kashyyyk"})
#     cola.arrive({"nombre": "maestro Yoda", "planeta": "Dagobah"})
#     cola.arrive({"nombre": "Wicket", "planeta": "Endor"})

#     print("\n--- a) Mostrar personajes de Alderaan, Endor y Tatooine ---")
#     mostrar_por_planetas(cola, ["Alderaan", "Endor", "Tatooine"])

#     print("\n--- b) Planeta natal de Luke Skywalker y Han Solo ---")
#     mostrar_planeta_de(cola, ["Luke Skywalker", "Han Solo"])

#     print("\n--- c) Insertar personaje antes de maestro Yoda ---")
#     nuevo = {"nombre": "Obi-Wan Kenobi", "planeta": "Stewjon"}
#     insertar_antes_de(cola, "maestro Yoda", nuevo)
#     cola.show()

#     print("\n--- d) Eliminar personaje después de Jar Jar Binks ---")
#     eliminar_despues_de(cola, "Jar Jar Binks")
#     cola.show()


# 12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
# ni métodos de ordenamiento.

def combinar_colas_ordenadas(c1: Queue, c2: Queue) -> Queue:
    resultado = Queue()

    while c1.size() > 0 and c2.size() > 0:
        if c1.on_front() <= c2.on_front():
            resultado.arrive(c1.attention())
        else:
            resultado.arrive(c2.attention())

    while c1.size() > 0:
        resultado.arrive(c1.attention())

    while c2.size() > 0:
        resultado.arrive(c2.attention())

    return resultado

# if __name__ == "__main__":
#     cola1 = Queue()
#     cola2 = Queue()

#     # Suponemos que ya están ordenadas
#     for valor in [1, 3, 5, 7]:
#         cola1.arrive(valor)

#     for valor in [2, 4, 6, 8]:
#         cola2.arrive(valor)

#     combinada = combinar_colas_ordenadas(cola1, cola2)

#     print("Cola combinada y ordenada:")
#     combinada.show()

# 13. Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:
# a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
# b. determinar cuántas letras hay en la segunda cola.
# c. determinar además si existen los caracteres “?” y “#”.

import random
import string

def generar_cola_aleatoria(tam: int) -> Queue:
    caracteres_posibles = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    cola = Queue()
    for _ in range(tam):
        cola.arrive(random.choice(caracteres_posibles))
    return cola

def separar_cola(cola: Queue) -> tuple[Queue, Queue]:
    digit_queue = Queue()
    others_queue = Queue()
    while cola.size() > 0:
        char = cola.attention()
        if char.isdigit():
            digit_queue.arrive(char)
        else:
            others_queue.arrive(char)
    return digit_queue, others_queue

def analizar_otros(others_queue: Queue) -> tuple[int, bool, bool]:
    letras_count = 0
    hay_pregunta = False
    hay_numeral = False
    while others_queue.size() > 0:
        char = others_queue.attention()
        if char.isalpha():
            letras_count += 1
        if char == '?':
            hay_pregunta = True
        if char == '#':
            hay_numeral = True
    return letras_count, hay_pregunta, hay_numeral


    
# if __name__ == "__main__":
#     original_queue = generar_cola_aleatoria(50000)
#     original_queue.show()
#     digit_queue, others_queue = separar_cola(original_queue)
#     letras_count, hay_pregunta, hay_numeral = analizar_otros(others_queue)
   

#     print(f"Cantidad de dígitos en digit_queue: {digit_queue.size()}")
#     print(f"Cantidad de letras en la otra cola: {letras_count}")
#     print(f"¿Existe '?': {hay_pregunta}")
#     print(f"¿Existe '#': {hay_numeral}")


# 14. Realizar un algoritmo que permita realizar las siguientes funciones:
# a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde –cargue
# al menos tres semáforos–.
# b. simular el funcionamiento de los semáforos cargados (cola circular).
# c. debe mostrar por pantalla el cambio de colores y el número del semáforo.

import time

def cargar_semaforos() -> Queue:
    cola_semaforos = Queue()
    semaforos = [
        {"id": 1, "tiempo_verde": 5},
        {"id": 2, "tiempo_verde": 3},
        {"id": 3, "tiempo_verde": 4},
    ]
    for s in semaforos:
        cola_semaforos.arrive(s)
    return cola_semaforos

def simular_semaforos(cola_semaforos: Queue, ciclos: int = 3) -> None:
    for _ in range(ciclos * cola_semaforos.size()):
        semaforo = cola_semaforos.attention()
        if semaforo is None:
            break
        print(f"Semáforo {semaforo['id']} - Verde encendido durante {semaforo['tiempo_verde']} segundos")
        time.sleep(semaforo['tiempo_verde'])
        print(f"Semáforo {semaforo['id']} - Rojo")
        cola_semaforos.arrive(semaforo)

# if __name__ == "__main__":
#     semaforos = cargar_semaforos()
#     simular_semaforos(semaforos, ciclos=2)

# 15. Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destruc-
# tor Estelar y necesita localizar la base rebelde más cercana– y se tiene una cola con informa-
# ción de las bases rebeldes en la tierra de las cuales conoce su nombre, número de flota aérea,

# coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes
# tareas una vez que aterrice:
# a. determinar cuál es la base rebelde más cercana desde su posición actual.
# b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:

# donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes de los
# dos puntos –por ejemplo coordenadas actual–, λ1 y λ2 las longitudes de los dos puntos
# –coordenadas de la base– ambos expresadas en radianes; para convertir de grados a
# radianes utilice la función math.radians(ángulo coordenada).

# c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y deter-
# minar cual tiene mayor flota aérea.

# d. determinar la distancia hasta la base rebelde con mayor flota aérea.

import math

def haversine(lat1_deg, lon1_deg, lat2_deg, lon2_deg):
    r = 6371000  # radio medio Tierra en metros
    phi1 = math.radians(lat1_deg)
    phi2 = math.radians(lat2_deg)
    delta_phi = math.radians(lat2_deg - lat1_deg)
    delta_lambda = math.radians(lon2_deg - lon1_deg)

    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return r * c

def cargar_bases() -> Queue:
    q = Queue()
    # Ejemplo de bases (nombre, nro flota, lat, lon)
    bases = [
        {"nombre": "Base Alpha", "flota": 120, "lat": -34.6037, "lon": -58.3816},  # Buenos Aires
        {"nombre": "Base Beta", "flota": 95, "lat": 40.7128, "lon": -74.0060},     # NY
        {"nombre": "Base Gamma", "flota": 150, "lat": 48.8566, "lon": 2.3522},     # Paris
        {"nombre": "Base Delta", "flota": 80, "lat": 35.6895, "lon": 139.6917},    # Tokio
        {"nombre": "Base Epsilon", "flota": 110, "lat": 51.5074, "lon": -0.1278}   # Londres
    ]
    for base in bases:
        q.arrive(base)
    return q

def bases_mas_cercanas_y_flota(queue_bases: Queue, lat_actual, lon_actual, n=3):
    # Primero extraemos las bases y calculamos distancia
    bases = []
    while queue_bases.size() > 0:
        base = queue_bases.attention()
        dist = haversine(lat_actual, lon_actual, base["lat"], base["lon"])
        base["distancia"] = dist
        bases.append(base)
    
    # Ordenar por distancia
    bases.sort(key=lambda b: b["distancia"])
    
    # Tomamos las n bases más cercanas
    cercanas = bases[:n]
    
    # Encontrar cuál de esas tiene mayor flota aérea
    mayor_flota_base = max(cercanas, key=lambda b: b["flota"])
    
    # Encontrar base con mayor flota en TODAS las bases
    mayor_flota_global = max(bases, key=lambda b: b["flota"])
    
    return cercanas, mayor_flota_base, mayor_flota_global


# if __name__ == "__main__":
#     # Posición actual (ejemplo)
#     lat_actual = 34.0522   
#     lon_actual = -118.2437
    
#     bases = cargar_bases()
    
#     cercanas, mayor_flota_cercanas, mayor_flota_global = bases_mas_cercanas_y_flota(bases, lat_actual, lon_actual)
    
#     print("Las 3 bases más cercanas:")
#     for b in cercanas:
#         print(f"- {b['nombre']} a {b['distancia']:.2f} metros (Flota aérea: {b['flota']})")
    
#     print(f"\nBase con mayor flota aérea entre las 3 más cercanas: {mayor_flota_cercanas['nombre']} ({mayor_flota_cercanas['flota']})")
    
#     dist_mayor_flota_global = haversine(lat_actual, lon_actual, mayor_flota_global["lat"], mayor_flota_global["lon"])
#     print(f"\nDistancia hasta la base rebelde con mayor flota aérea ({mayor_flota_global['nombre']}): {dist_mayor_flota_global:.2f} metros")



# 17. Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador,
# de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las siguientes situaciones:

# a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la fun-
# ción time.sleep (segundos) – hasta que se vacíe la cola.

# b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como
# máximo 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el
# tiempo restante para terminar su ejecución–.
# c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el
# quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.
# d. no se aplican criterios de prioridad en los procesos.

import time

def cargar_procesos_interactivos(cola: Queue):
    while True:
        agregar = input("¿Querés agregar un nuevo proceso? (s/n): ").strip().lower()
        if agregar != 's':
            break
        pid = input("Ingrese ID del proceso: ").strip()
        while True:
            try:
                tiempo = float(input("Ingrese tiempo de ejecución (segundos): "))
                if tiempo > 0:
                    break
                else:
                    print("El tiempo debe ser mayor a cero.")
            except ValueError:
                print("Valor inválido, ingrese un número.")
        cola.arrive({"id": pid, "tiempo": tiempo})

def simular_procesos(cola: Queue, quantum: float = 4.5):
    while cola.size() > 0:
        proceso = cola.attention()
        if proceso is None:
            break
        
        tiempo_actual = proceso["tiempo"]
        tiempo_a_ejecutar = min(tiempo_actual, quantum)
        
        print(f"Ejecutando proceso {proceso['id']} por {tiempo_a_ejecutar} segundos...")
        time.sleep(tiempo_a_ejecutar)
        
        tiempo_restante = tiempo_actual - tiempo_a_ejecutar
        if tiempo_restante > 0:
            print(f"Proceso {proceso['id']} no terminó. Tiempo restante: {tiempo_restante:.2f} segundos. Reencolando.")
            proceso["tiempo"] = tiempo_restante
            cola.arrive(proceso)
        else:
            print(f"Proceso {proceso['id']} terminó su ejecución.")
        
        # Después de atender el proceso, preguntar si se quieren agregar nuevos procesos
        cargar_procesos_interactivos(cola)

  

# if __name__ == "__main__":
#     cola_procesos = Queue()
#     print("Carga inicial de procesos:")
#     cargar_procesos_interactivos(cola_procesos)
#     simular_procesos(cola_procesos)


# 18. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
# letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
# que resuelva las siguientes situaciones:
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
# y F, y la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
# tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
# mayor que 506.

# Función para generar un turno aleatorio
def generar_turno():
    letra = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
    numero = random.randint(0, 999)
    return f"{letra}{numero:03d}"

# Punto (a)
def cargar_turnos(cantidad: int, cola: Queue):
    for _ in range(cantidad):
        turno = generar_turno()
        cola.arrive(turno)

# Punto (b)
def separar_colas(cola_original: Queue):
    cola_1 = Queue()
    cola_2 = Queue()
    for _ in range(cola_original.size()):
        turno = cola_original.attention()
        if turno[0] in ['A', 'C', 'F']:
            cola_1.arrive(turno)
        else:
            cola_2.arrive(turno)
    return cola_1, cola_2

# Punto (c)
def mayor_letra_en_cola(cola: Queue):
    contador = {}
    for _ in range(cola.size()):
        turno = cola.move_to_end()
        letra = turno[0]
        contador[letra] = contador.get(letra, 0) + 1
    letra_mayor = max(contador, key=contador.get)
    return letra_mayor, contador[letra_mayor]

# Punto (d)
def mostrar_turnos_mayores_506(cola: Queue):
    print("Turnos con número mayor a 506:")
    for _ in range(cola.size()):
        turno = cola.move_to_end()
        numero = int(turno[1:])
        if numero > 506:
            print(turno)

# # Ejecución principal
# if __name__ == "__main__":
#     # a. Cargar 1000 turnos
#     cola_general = Queue()
#     cargar_turnos(1000, cola_general)

#     # b. Separar en dos colas
#     cola_1, cola_2 = separar_colas(cola_general)

#     # c. Determinar cola con más turnos y letra con más apariciones
#     if cola_1.size() > cola_2.size():
#         mayor = cola_1
#         menor = cola_2
#         nombre_mayor = "cola_1"
#     else:
#         mayor = cola_2
#         menor = cola_1
#         nombre_mayor = "cola_2"

#     letra, cantidad = mayor_letra_en_cola(mayor)
#     print(f"La cola con más turnos es {nombre_mayor} con {mayor.size()} turnos.")
#     print(f"La letra con más apariciones en esta cola es '{letra}' con {cantidad} turnos.")

#     # d. Mostrar turnos de la cola menor con número > 506
#     mostrar_turnos_mayores_506(menor)


# 19. Modificar las funciones de arribo y atención del TDA cola para adaptarlo a una cola circular,
# que no necesite la función mover al final; y desarrollar un función que permita realizar un ba-
# rrido de dicha estructura respetando el principio de funcionamiento de la cola.

class CircularQueue:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.__elements = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def arrive(self, value: Any) -> None:
        if self.count == self.capacity:
            raise OverflowError("Cola circular llena")
        self.rear = (self.rear + 1) % self.capacity
        self.__elements[self.rear] = value
        self.count += 1

    def attention(self) -> Optional[Any]:
        if self.count == 0:
            return None
        value = self.__elements[self.front]
        self.__elements[self.front] = None  # Limpieza opcional
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    def size(self) -> int:
        return self.count

    def on_front(self) -> Optional[Any]:
        return self.__elements[self.front] if self.count > 0 else None

    def show(self) -> None:
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            print(self.__elements[index])


def barrer_circular_queue(cola: CircularQueue):
    print("Barrido de la cola circular:")
    for i in range(cola.size()):
        index = (cola.front + i) % cola.capacity
        print(cola._CircularQueue__elements[index])  # Acceso interno controlado

# if __name__ == "__main__":
#     cq = CircularQueue(10)
#     for i in range(5):
#         cq.arrive(f"T{i:03}")
    
#     cq.attention()
#     cq.arrive("T999")
    
#     barrer_circular_queue(cq)


# 20. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro),
# que resuelva las siguientes actividades:
# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son
# los siguientes:
# I. automóviles (tarifa $47);
# II. camionetas (tarifa $59);
# III. camiones (tarifa $71);
# IV. colectivos (tarifa $64).
# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

# Tarifas
TARIFAS = {
    "automóvil": 47,
    "camioneta": 59,
    "camión": 71,
    "colectivo": 64
}

# a. Cargar 30 vehículos aleatorios en las cabinas
def cargar_vehiculos(cabinas, cantidad=30):
    tipos = list(TARIFAS.keys())
    for _ in range(cantidad):
        tipo = random.choice(tipos)
        cabina = random.choice(cabinas)
        cabina.arrive(tipo)

# b y d. Atender cabinas, contar y acumular por tipo
def atender_cabinas(cabinas):
    recaudaciones = [0] * len(cabinas)
    conteos = [  # una lista por cabina
        {tipo: 0 for tipo in TARIFAS}
        for _ in range(len(cabinas))
    ]

    for i, cabina in enumerate(cabinas):
        while cabina.size() > 0:
            tipo = cabina.attention()
            recaudaciones[i] += TARIFAS[tipo]
            conteos[i][tipo] += 1

    return recaudaciones, conteos

# c. Cabina que más recaudó
def mostrar_resultados(recaudaciones, conteos):
    max_recaudado = max(recaudaciones)
    cabina_ganadora = recaudaciones.index(max_recaudado)
    print(f"\n💰 La cabina {cabina_ganadora + 1} recaudó más: ${max_recaudado}\n")

    for i, conteo in enumerate(conteos):
        print(f"Cabina {i + 1}:")
        for tipo, cantidad in conteo.items():
            print(f"  - {tipo.capitalize():10}: {cantidad} vehículos")
        print()

# Programa principal
# if __name__ == "__main__":
#     cabina1 = Queue()
#     cabina2 = Queue()
#     cabina3 = Queue()
#     cabinas = [cabina1, cabina2, cabina3]

#     cargar_vehiculos(cabinas)
#     recaudaciones, conteos = atender_cabinas(cabinas)
#     mostrar_resultados(recaudaciones, conteos)


# 21. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuer-
# to que tiene una pista, contemplando las siguientes actividades:

# a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de
# origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).
# b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de
# salida. Otra para los aterrizajes, se deben agregan a medida que arriban al aeropuerto.
# c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.
# d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas des-
# pués de realizar una atención.
# e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje –dado que son
# aviones que están sobrevolando en la zona de espera–, salvo que sea el horario de salida del
# primer avión de la cola de despegue, en ese caso se deberá atender dicho despegue.
# f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de despegue y aterri-
# zaje –adaptados a segundo para los fines prácticos del ejercicio–:
    # I. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
    # II. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
    # III. carga (aterrizaje = 12 segundos, despegue = 9 segundos).
# g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde
# cuando se lo atiende para despegar (en esta caso el horario de salida será mayor que el
# último de la cola).


TIPOS_AVION = {
    "pasajeros": {"aterrizaje": 10, "despegue": 5},
    "negocios": {"aterrizaje": 5, "despegue": 3},
    "carga": {"aterrizaje": 12, "despegue": 9},
}

def crear_vuelo(empresa, hora_salida, hora_llegada, origen, destino, tipo):
    return {
        "empresa": empresa,
        "hora_salida": hora_salida,
        "hora_llegada": hora_llegada,
        "origen": origen,
        "destino": destino,
        "tipo": tipo
    }

def agregar_despegue_ordenado(cola, vuelo):
    aux = Queue()
    agregado = False

    while cola.size() > 0:
        actual = cola.attention()
        if not agregado and vuelo["hora_salida"] < actual["hora_salida"]:
            aux.arrive(vuelo)
            agregado = True
        aux.arrive(actual)

    if not agregado:
        aux.arrive(vuelo)

    while aux.size() > 0:
        cola.arrive(aux.attention())

def uso_pista(vuelo, tipo_op):
    segundos = TIPOS_AVION[vuelo["tipo"]][tipo_op]
    print(f">> {tipo_op.upper()} de {vuelo['empresa']} ({vuelo['tipo']}) usando pista ({segundos}s)")
    time.sleep(0.2)  # simulación corta

def atender_pista(cola_aterrizaje, cola_despegue, hora_actual):
    primero_despegue = cola_despegue.on_front()

    if (
        primero_despegue is not None and
        primero_despegue["hora_salida"] == hora_actual
    ):
        vuelo = cola_despegue.attention()
        uso_pista(vuelo, "despegue")
    elif cola_aterrizaje.size() > 0:
        vuelo = cola_aterrizaje.attention()
        uso_pista(vuelo, "aterrizaje")
    else:
        print("-- No hay vuelos en espera --")

def cancelar_vuelo(cola, empresa):
    aux = Queue()
    encontrado = False
    while cola.size() > 0:
        vuelo = cola.attention()
        if vuelo["empresa"] == empresa:
            encontrado = True
            print(f">> Vuelo de {empresa} cancelado.")
        else:
            aux.arrive(vuelo)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    if not encontrado:
        print(f">> Vuelo de {empresa} no encontrado para cancelar.")

def reprogramar_vuelo(cola, empresa):
    aux = Queue()
    vuelo_reprogramado = None
    max_hora = 0

    while cola.size() > 0:
        vuelo = cola.attention()
        if vuelo["empresa"] == empresa:
            vuelo_reprogramado = vuelo
        else:
            aux.arrive(vuelo)
            if vuelo["hora_salida"] > max_hora:
                max_hora = vuelo["hora_salida"]

    if vuelo_reprogramado:
        vuelo_reprogramado["hora_salida"] = max_hora + 5
        print(f">> Vuelo de {empresa} reprogramado para las {vuelo_reprogramado['hora_salida']}")
        agregar_despegue_ordenado(aux, vuelo_reprogramado)
    else:
        print(f">> Vuelo de {empresa} no encontrado para reprogramar.")

    while aux.size() > 0:
        cola.arrive(aux.attention())

# if __name__ == "__main__":
#     cola_despegues = Queue()
#     cola_aterrizajes = Queue()

#     # Cargar vuelos de prueba
#     agregar_despegue_ordenado(cola_despegues, crear_vuelo("Flybondi", 1005, 0, "Ezeiza", "Córdoba", "pasajeros"))
#     agregar_despegue_ordenado(cola_despegues, crear_vuelo("Jetsur", 1010, 0, "Ezeiza", "Montevideo", "negocios"))

#     cola_aterrizajes.arrive(crear_vuelo("Latam", 0, 1003, "Mendoza", "Ezeiza", "carga"))
#     cola_aterrizajes.arrive(crear_vuelo("Aerolineas", 0, 1004, "Bariloche", "Ezeiza", "pasajeros"))

#     for hora in range(1000, 1020):
#         print(f"\n🕓 Hora actual: {hora}")
#         atender_pista(cola_aterrizajes, cola_despegues, hora)

#     cancelar_vuelo(cola_despegues, "Jetsur")
#     reprogramar_vuelo(cola_despegues, "Flybondi")

#     print("\n📋 Estado final de colas:")
#     print("Despegues:")
#     cola_despegues.show()
#     print("Aterrizajes:")
#     cola_aterrizajes.show()


from typing import Dict

def cargar_personajes(cola: Queue):
    datos = [
        {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
        {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
        {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
        {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
        {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
        {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
        {"personaje": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
        {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
        {"personaje": "Shuri", "superheroe": "Shuri", "genero": "F"},
    ]
    for dato in datos:
        cola.arrive(dato)

def procesar_mcu(cola: Queue):
    aux = Queue()

    # b) superhéroes femeninos
    print(" Superhéroes femeninos:")
    # c) personajes masculinos
    print(" Personajes masculinos:")
    # e) nombres que empiezan con S
    print(" Nombres que empiezan con S (personaje o superhéroe):")

    cap_marvel_personaje = None
    scott_lang_superheroe = None
    carol_danvers_superheroe = None

    while cola.size() > 0:
        dato = cola.attention()
        personaje = dato["personaje"]
        superheroe = dato["superheroe"]
        genero = dato["genero"]

        # a) Capitana Marvel
        if superheroe == "Capitana Marvel":
            cap_marvel_personaje = personaje

        # b) Superhéroes femeninos
        if genero == "F":
            print(f"- {superheroe}")

        # c) Personajes masculinos
        if genero == "M":
            print(f"- {personaje}")

        # d) Superhéroe de Scott Lang
        if personaje == "Scott Lang":
            scott_lang_superheroe = superheroe

        # e) Nombres que comienzan con S
        if personaje.startswith("S") or superheroe.startswith("S"):
            print(f"- Personaje: {personaje}, Superhéroe: {superheroe}, Género: {genero}")

        # f) Buscar Carol Danvers
        if personaje == "Carol Danvers":
            carol_danvers_superheroe = superheroe

        aux.arrive(dato)

    # Restaurar la cola original
    while aux.size() > 0:
        cola.arrive(aux.attention())

    # Mostrar resultados específicos
    print("\nResultados específicos:")
    if cap_marvel_personaje:
        print(f"a) Capitana Marvel es: {cap_marvel_personaje}")
    if scott_lang_superheroe:
        print(f"d) Scott Lang es: {scott_lang_superheroe}")
    if carol_danvers_superheroe:
        print(f"f) Carol Danvers está en la cola. Su identidad es: {carol_danvers_superheroe}")
    else:
        print("f) Carol Danvers no se encuentra en la cola.")


if __name__ == "__main__":
    cola_mcu = Queue()
    cargar_personajes(cola_mcu)
    procesar_mcu(cola_mcu)


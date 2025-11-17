"""Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
indicar qué personajes aparecieron en los nueve episodios de la saga."""

from graph import Graph

# Datos de personajes con episodios en los que aparecen
personajes_data = {
    "Luke Skywalker": [4, 5, 6, 7, 8, 9],
    "Darth Vader": [3, 4, 5, 6],
    "Yoda": [1, 2, 3, 5, 6, 7, 8, 9],
    "Boba Fett": [5, 6],
    "C-3PO": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Leia": [4, 5, 6, 7, 8, 9],
    "Rey": [7, 8, 9],
    "Kylo Ren": [7, 8, 9],
    "Chewbacca": [3, 4, 5, 6, 7, 8, 9],
    "Han Solo": [4, 5, 6, 7],
    "R2-D2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "BB-8": [7, 8, 9]
}

def contar_episodios_compartidos(personaje1, personaje2):
    """Cuenta cuántos episodios comparten dos personajes"""
    episodios1 = set(personajes_data[personaje1])
    episodios2 = set(personajes_data[personaje2])
    return len(episodios1.intersection(episodios2))

def crear_grafo_star_wars():
    """Crea el grafo con todos los personajes y sus conexiones"""
    grafo = Graph(is_directed=False)
    
    # Insertar todos los vértices (personajes)
    print("Cargando personajes de Star Wars...")
    for personaje in personajes_data.keys():
        grafo.insert_vertex(personaje)
    
    # Insertar aristas con el peso (episodios compartidos)
    personajes_lista = list(personajes_data.keys())
    for i in range(len(personajes_lista)):
        for j in range(i + 1, len(personajes_lista)):
            personaje1 = personajes_lista[i]
            personaje2 = personajes_lista[j]
            episodios_compartidos = contar_episodios_compartidos(personaje1, personaje2)
            if episodios_compartidos > 0:
                grafo.insert_edge(personaje1, personaje2, episodios_compartidos)
    
    print(f"Grafo creado con {len(personajes_data)} personajes.\n")
    return grafo

def encontrar_arbol_expansion_minima(grafo, personajes):
    """a. Halla el árbol de expansión mínimo desde varios personajes"""
    print("="*60)
    print("PUNTO A: ÁRBOL DE EXPANSIÓN MÍNIMA")
    print("="*60)
    
    for personaje in personajes:
        print(f"\nÁrbol de expansión mínima desde {personaje}:")
        expansion_tree = grafo.kruskal(personaje)
        
        # El árbol viene como: "vertice1;arista1;arista2;vertice2;arista3;..."
        # Las aristas están en formato "origen-destino-peso"
        peso_total = 0
        aristas = []
        elementos = expansion_tree.split(';')
        
        print(f"\nConexiones del árbol de expansión mínima:")
        for elemento in elementos:
            # Verificar si contiene un guión (es una arista)
            if '-' in elemento:
                # Separar la arista en partes
                partes = elemento.split('-')
                # El peso siempre es el último elemento
                if len(partes) >= 3:
                    peso = int(partes[-1])
                    # Los vértices son todos los elementos menos el peso
                    destino = partes[-2]
                    origen = '-'.join(partes[:-2])
                    peso_total += peso
                    aristas.append((origen, destino, peso))
                    print(f"  {origen:20} -- {destino:20} : {peso} episodios")
        
        print(f"\nTotal de aristas: {len(aristas)}")
        print(f"Peso total del árbol: {peso_total} episodios compartidos")
        print("-"*60)

def encontrar_maximo_episodios_compartidos(grafo):
    """b. Determina el máximo de episodios compartidos entre dos personajes"""
    print("\n" + "="*60)
    print("PUNTO B: MÁXIMO DE EPISODIOS COMPARTIDOS")
    print("="*60)
    
    max_episodios = 0
    pares_maximos = []
    
    # Recorrer todos los vértices y sus aristas
    for vertice in grafo:
        for arista in vertice.edges:
            # Evitar duplicados (solo contar cada par una vez)
            if vertice.value < arista.value:
                if arista.weight > max_episodios:
                    max_episodios = arista.weight
                    pares_maximos = [(vertice.value, arista.value)]
                elif arista.weight == max_episodios:
                    pares_maximos.append((vertice.value, arista.value))
    
    print(f"\nNúmero máximo de episodios compartidos: {max_episodios}")
    print(f"\nPares de personajes con {max_episodios} episodios juntos:")
    for par in pares_maximos:
        print(f"  • {par[0]} y {par[1]}")

def calcular_camino_mas_corto(grafo, origen, destino):
    """d. Calcula el camino más corto entre dos personajes usando Dijkstra"""
    path = grafo.dijkstra(origen)
    
    peso_total = None
    camino_completo = []
    destino_actual = destino
    
    # Reconstruir el camino desde el destino hasta el origen
    while path.size() > 0:
        value = path.pop()
        if value[0] == destino_actual:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destino_actual = value[2]
    
    camino_completo.reverse()
    return camino_completo, peso_total

def mostrar_caminos_mas_cortos(grafo):
    """d. Muestra los caminos más cortos solicitados"""
    print("\n" + "="*60)
    print("PUNTO D: CAMINOS MÁS CORTOS")
    print("="*60)
    
    rutas = [
        ("C-3PO", "R2-D2"),
        ("Yoda", "Darth Vader")
    ]
    
    for origen, destino in rutas:
        print(f"\nCamino más corto desde {origen} hasta {destino}:")
        camino, peso = calcular_camino_mas_corto(grafo, origen, destino)
        print(f"  Ruta: {' -> '.join(camino)}")
        print(f"  Costo total: {peso} episodios")

def personajes_nueve_episodios():
    """e. Indica qué personajes aparecieron en los 9 episodios"""
    print("\n" + "="*60)
    print("PUNTO E: PERSONAJES EN LOS 9 EPISODIOS")
    print("="*60)
    
    personajes_completos = []
    for personaje, episodios in personajes_data.items():
        if len(episodios) == 9:
            personajes_completos.append(personaje)
    
    print(f"\nPersonajes que aparecieron en los 9 episodios:")
    if personajes_completos:
        for personaje in personajes_completos:
            print(f"  • {personaje}")
    else:
        print("  No hay personajes que aparezcan en los 9 episodios.")
    
    print(f"\nPersonajes con más apariciones:")
    episodios_ordenados = sorted(personajes_data.items(), key=lambda x: len(x[1]), reverse=True)
    for personaje, episodios in episodios_ordenados[:5]:
        print(f"  • {personaje}: {len(episodios)} episodios")

def resolver_ejercicio_star_wars():
    """Función principal que resuelve todos los puntos del ejercicio"""
    print("="*60)
    print("EJERCICIO 2 - GRAFO DE STAR WARS")
    print("="*60)
    print()
    
    # Crear el grafo
    grafo = crear_grafo_star_wars()
    
    # a. Árbol de expansión mínima desde C-3PO, Yoda y Leia
    encontrar_arbol_expansion_minima(grafo, ["C-3PO", "Yoda", "Leia"])
    
    # b. Máximo de episodios compartidos
    encontrar_maximo_episodios_compartidos(grafo)
    
    # c. Los personajes ya fueron cargados al inicio
    
    # d. Caminos más cortos
    mostrar_caminos_mas_cortos(grafo)
    
    # e. Personajes en los 9 episodios
    personajes_nueve_episodios()
    
    print("\n" + "="*60)

if __name__ == "__main__":
    resolver_ejercicio_star_wars()



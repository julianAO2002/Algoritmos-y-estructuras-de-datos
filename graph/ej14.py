"""
14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv.
"""

from graph import Graph
from stack import Stack

class HouseGraph(Graph):
    """Grafo de casa que hereda de Graph para manejar ambientes y cableado"""
    
    def __init__(self):
        super().__init__(is_directed=False)  # Grafo no dirigido
    
    def insert_room(self, room_name: str):
        """Inserta un ambiente de la casa"""
        self.insert_vertex(room_name)
    
    def connect_rooms(self, room1: str, room2: str, distance_meters: float):
        """Conecta dos ambientes con la distancia en metros"""
        self.insert_edge(room1, room2, distance_meters)
    
    def show_house_layout(self):
        """Muestra el plano de la casa con las distancias"""
        print("=== PLANO DE LA CASA ===")
        for vertex in self:
            room = vertex.value
            connections = len(vertex.edges)
            print(f"{room} ({connections} conexiones):")
            for edge in vertex.edges:
                print(f"  -> {edge.value}: {edge.weight}m")
            print()
    
    def get_room_connections_count(self):
        """Muestra cuántas conexiones tiene cada ambiente"""
        print("Número de conexiones por ambiente:")
        for vertex in self:
            connections = len(vertex.edges)
            print(f"  {vertex.value}: {connections} conexiones")
    
    def find_shortest_path_dijkstra(self, origin, destination):
        """Encuentra el camino más corto usando Dijkstra"""
        path_stack = self.dijkstra(origin)
        
        # Reconstruir el camino
        current_destination = destination
        complete_path = []
        total_cost = None
        
        while path_stack.size() > 0:
            vertex_info = path_stack.pop()
            vertex_name = vertex_info[0]
            cost = vertex_info[1]
            predecessor = vertex_info[2]
            
            if vertex_name == current_destination:
                if total_cost is None:
                    total_cost = cost
                complete_path.append(vertex_name)
                current_destination = predecessor
        
        complete_path.reverse()
        return complete_path, total_cost

def load_house_data():
    """Carga todos los ambientes de la casa y sus conexiones"""
    house = HouseGraph()
    
    print("Cargando ambientes de la casa...")
    
    # a. Insertar todos los ambientes
    rooms = [
        "Cocina", "Comedor", "Cochera", "Quincho",
        "Baño 1", "Baño 2", "Habitación 1", "Habitación 2", 
        "Sala de Estar", "Terraza", "Patio"
    ]
    
    for room in rooms:
        house.insert_room(room)
    
    print("Configurando conexiones entre ambientes...")
    
    # b. Cargar conexiones (al menos 3 por vértice, 2 con 5 conexiones)
    # Diseño lógico de una casa: conectar ambientes cercanos
    
    # Cocina (5 conexiones) - centro de la casa
    house.connect_rooms("Cocina", "Comedor", 3.5)
    house.connect_rooms("Cocina", "Sala de Estar", 4.2)
    house.connect_rooms("Cocina", "Patio", 6.0)
    house.connect_rooms("Cocina", "Baño 1", 5.5)
    house.connect_rooms("Cocina", "Terraza", 7.2)
    
    # Sala de Estar (5 conexiones) - área social
    house.connect_rooms("Sala de Estar", "Comedor", 2.8)
    house.connect_rooms("Sala de Estar", "Habitación 1", 4.5)
    house.connect_rooms("Sala de Estar", "Habitación 2", 6.1)
    house.connect_rooms("Sala de Estar", "Terraza", 3.9)
    # Ya conectada con Cocina
    
    # Comedor (4 conexiones)
    house.connect_rooms("Comedor", "Quincho", 5.8)
    house.connect_rooms("Comedor", "Patio", 4.3)
    # Ya conectado con Cocina y Sala de Estar
    
    # Habitación 1 (3 conexiones)
    house.connect_rooms("Habitación 1", "Baño 1", 2.1)
    house.connect_rooms("Habitación 1", "Habitación 2", 3.7)
    # Ya conectada con Sala de Estar
    
    # Habitación 2 (4 conexiones)
    house.connect_rooms("Habitación 2", "Baño 2", 1.9)
    house.connect_rooms("Habitación 2", "Terraza", 4.8)
    # Ya conectada con Sala de Estar y Habitación 1
    
    # Baño 1 (3 conexiones)
    house.connect_rooms("Baño 1", "Baño 2", 6.5)
    # Ya conectado con Cocina y Habitación 1
    
    # Baño 2 (3 conexiones)
    house.connect_rooms("Baño 2", "Cochera", 8.2)
    # Ya conectado con Habitación 2 y Baño 1
    
    # Cochera (4 conexiones)
    house.connect_rooms("Cochera", "Patio", 3.1)
    house.connect_rooms("Cochera", "Quincho", 4.7)
    house.connect_rooms("Cochera", "Terraza", 9.3)
    # Ya conectada con Baño 2
    
    # Quincho (3 conexiones)
    house.connect_rooms("Quincho", "Patio", 2.5)
    # Ya conectado con Comedor y Cochera
    
    # Patio (4 conexiones)
    # Ya conectado con Cocina, Comedor, Cochera y Quincho
    
    # Terraza (4 conexiones)  
    # Ya conectada con Cocina, Sala de Estar, Habitación 2 y Cochera
    
    return house

def resolver():
    """Resuelve todos los puntos del ejercicio 14"""
    print("="*60)
    print("EJERCICIO 14: CABLEADO DE CASA")
    print("="*60)
    
    # Cargar la casa
    house = load_house_data()
    
    print("\na. y b. Casa cargada con ambientes y distancias:")
    house.show_house_layout()
    
    print("="*60)
    print("Verificación de conexiones mínimas:")
    house.get_room_connections_count()
    
    print("="*60)
    print("\nc. ÁRBOL DE EXPANSIÓN MÍNIMA (MST):")
    print("Calculando el cableado mínimo para conectar todos los ambientes...")
    
    mst = house.kruskal("Cocina")  # Empezar desde la cocina
    print(f"\nÁrbol de expansión mínima:")
    print(f"{mst}")
    
    # Calcular metros totales de cable
    if isinstance(mst, str):
        edges = mst.split(';')
        total_cable = 0
        print("\n--- CONEXIONES DEL MST ---")
        for edge in edges:
            if '-' in edge:
                parts = edge.split('-')
                if len(parts) >= 3:
                    room1, room2 = parts[0], parts[1]
                    distance = float(parts[-1])
                    print(f"{room1} ↔ {room2}: {distance}m")
                    total_cable += distance
        
        print(f"\n🔌 TOTAL DE CABLE NECESARIO: {total_cable:.1f} metros")
        print(f"💰 (Aproximadamente {total_cable * 2.5:.0f} pesos si el cable vale $2.50/metro)")
    
    print("="*60)
    print("\nd. CAMINO MÁS CORTO: Router (Habitación 1) → Smart TV (Sala de Estar)")
    print("Calculando cable de red necesario...")
    
    path, distance = house.find_shortest_path_dijkstra("Habitación 1", "Sala de Estar")
    
    if path and distance is not None:
        print(f"\n📡 RUTA ÓPTIMA: {' → '.join(path)}")
        print(f"📏 DISTANCIA TOTAL: {distance}m")
        print(f"🔗 CABLE DE RED NECESARIO: {distance:.1f} metros")
        print(f"💰 COSTO CABLE RED: ${distance * 5:.0f} (cable red $5/metro)")
        
        # Mostrar el recorrido paso a paso
        print(f"\n--- RECORRIDO DETALLADO ---")
        if len(path) > 1:
            for i in range(len(path) - 1):
                current_room = path[i]
                next_room = path[i + 1]
                # Buscar la distancia entre estos dos ambientes
                room_pos = house.search(current_room, 'value')
                if room_pos is not None:
                    for edge in house[room_pos].edges:
                        if edge.value == next_room:
                            print(f"  {current_room} → {next_room}: {edge.weight}m")
                            break
    else:
        print("❌ No se encontró camino entre Habitación 1 y Sala de Estar")
    
    print("="*60)
    print("🏠 RESUMEN DEL PROYECTO:")
    print(f"• Ambientes conectados: {len(house)}")
    print(f"• Cable estructural (MST): {total_cable:.1f}m")
    print(f"• Cable de red (Router-TV): {distance:.1f}m")
    print(f"• Total de cable: {total_cable + distance:.1f}m")
    print("="*60)

if __name__ == "__main__":
    resolver()
"""
5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
sarios para resolver las tareas, listadas a continuación:

a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
dor, router, switch, impresora;
b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
Red Hat, Debian, Arch;
c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
Red Hat, Fedora hasta la impresora;
d. encontrar el árbol de expansión mínima;
e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor "Guaraní";
f. indicar desde que computadora del switch 01 es el camino más corto
al servidor "MongoDB";
g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
h. debe utilizar un grafo no dirigido.
"""

from graph import Graph
from stack import Stack

class NetworkGraph(Graph):
    """Grafo de red que hereda de Graph para manejar dispositivos de red"""
    
    def __init__(self):
        super().__init__(is_directed=False)  # Grafo no dirigido como pide el ejercicio
        self.device_types = {}  # Diccionario para almacenar tipos de dispositivos
    
    def insert_device(self, name: str, device_type: str):
        self.insert_vertex(name)
        self.device_types[name] = device_type
    
    def get_device_type(self, name: str):
        """Obtiene el tipo de un dispositivo"""
        return self.device_types.get(name, "desconocido")
    
    def show_network(self):
        """Muestra la red con tipos de dispositivos"""
        print("=== RED DE DISPOSITIVOS ===")
        for vertex in self:
            device_type = self.get_device_type(vertex.value)
            print(f"{vertex.value} ({device_type})")
            for edge in vertex.edges:
                print(f"  -> {edge.value} (peso: {edge.weight})")
            print()
    
    def get_devices_by_type(self, device_type: str):
        """Obtiene lista de dispositivos por tipo"""
        devices = []
        for name, dtype in self.device_types.items():
            if dtype == device_type:
                devices.append(name)
        return devices
    
    def find_shortest_path_dijkstra(self, origin, destination):
        """Encuentra el camino más corto usando Dijkstra y devuelve el camino completo"""
        path_stack = self.dijkstra(origin)
        
        # Reconstruir el camino desde el destino hasta el origen
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
    

###RESOLUCION###

def load_network_data():
    """Carga todos los datos de la red según la imagen"""
    network = NetworkGraph()
    
    # Insertar todos los dispositivos con sus tipos
    print("Cargando dispositivos de red...")
    
    # PCs
    network.insert_device("Manjaro", "pc")
    network.insert_device("Ubuntu", "pc") 
    network.insert_device("Mint", "pc")
    network.insert_device("Fedora", "pc")
    network.insert_device("Parrot", "pc")
    
    # Notebooks  
    network.insert_device("Red Hat", "notebook")
    network.insert_device("Debian", "notebook")
    network.insert_device("Arch", "notebook")
    
    # Servidores
    network.insert_device("Guarani", "servidor")
    network.insert_device("MongoDB", "servidor")
    
    # Switches
    network.insert_device("Switch 1", "switch")
    network.insert_device("Switch 2", "switch")
    
    # Routers
    network.insert_device("Router 1", "router")
    network.insert_device("Router 2", "router")
    network.insert_device("Router 3", "router")
    
    # Impresora
    network.insert_device("Impresora", "impresora")    
    
    
    # Conexiones según la imagen (grafo no dirigido)
    # Switch 1 conexiones
    network.insert_edge("Switch 1", "Debian", 17)
    network.insert_edge("Switch 1", "Ubuntu", 18) 
    network.insert_edge("Switch 1", "Impresora", 22)
    network.insert_edge("Switch 1", "Mint", 80)
    network.insert_edge("Switch 1", "Router 1", 29)
    
    # Router 1 conexiones
    network.insert_edge("Router 1", "Router 2", 37)
    network.insert_edge("Router 1", "Router 3", 43)
    
    # Router 2 conexiones  
    network.insert_edge("Router 2", "Red Hat", 25)
    network.insert_edge("Router 2", "Guarani", 9)
    network.insert_edge("Router 2", "Router 3", 50)
    
    # Router 3 conexiones
    network.insert_edge("Router 3", "Switch 2", 61)
    
    # Switch 2 conexiones
    network.insert_edge("Switch 2", "Manjaro", 40)
    network.insert_edge("Switch 2", "Parrot", 12)
    network.insert_edge("Switch 2", "MongoDB", 5)
    network.insert_edge("Switch 2", "Arch", 56)
    network.insert_edge("Switch 2", "Fedora", 3)
    
    return network

def resolver():
    """Resuelve todos los puntos del ejercicio"""
    print("="*60)
    print("EJERCICIO 5: RED DE DISPOSITIVOS")
    print("="*60)
    
    # Cargar la red
    network = load_network_data()
    
    print("\na. Red cargada con tipos de dispositivos:")
    network.show_network()
    
    print("="*60)
    print("\nb. BARRIDOS desde las 3 notebooks:")
    
    notebooks = ["Red Hat", "Debian", "Arch"]
    
    for notebook in notebooks:
        print(f"\n--- Barridos desde {notebook} ---")
        
        print(f"Barrido en PROFUNDIDAD desde {notebook}:")
        network.deep_sweep(notebook)
        
        print(f"\nBarrido en AMPLITUD desde {notebook}:")
        network.amplitude_sweep(notebook)
        print()
    
    print("="*60)
    print("\nc. Camino más corto para imprimir desde PCs:")
    
    pcs_to_print = ["Manjaro", "Fedora"]  # Red Hat es notebook, no PC
    for pc in pcs_to_print:
        if network.get_device_type(pc) == "pc":
            path, cost = network.find_shortest_path_dijkstra(pc, "Impresora")
            if path:
                print(f"Desde {pc} a Impresora: {' -> '.join(path)} (Costo: {cost})")
            else:
                print(f"No hay camino desde {pc} a Impresora")
    
    print("="*60)
    print("\nd. Árbol de expansión mínima:")
    mst = network.kruskal("Switch 1")  # Usar cualquier vértice como origen
    print(f"Árbol de expansión mínima: {mst}")
    
    # Calcular peso total del MST
    if isinstance(mst, str):
        edges = mst.split(';')
        total_weight = 0
        print("Aristas del MST:")
        for edge in edges:
            if '-' in edge:
                parts = edge.split('-')
                if len(parts) >= 3:
                    origin, destination, weight = parts[0], parts[1], parts[-1]
                    print(f"  {origin} - {destination}: {weight}")
                    total_weight += int(weight)
        print(f"Peso total del MST: {total_weight}")
    
    print("="*60)
    print("\ne. Camino más corto desde PCs al servidor Guarani:")
    
    pcs = network.get_devices_by_type("pc")
    shortest_path = None
    shortest_cost = float('inf')
    best_pc = None
    
    for pc in pcs:
        path, cost = network.find_shortest_path_dijkstra(pc, "Guarani")
        if cost is not None and cost < shortest_cost:
            shortest_cost = cost
            shortest_path = path
            best_pc = pc
        if path:
            print(f"Desde {pc}: {' -> '.join(path)} (Costo: {cost})")
    
    print(f"\nEl camino MÁS CORTO es desde {best_pc}: {' -> '.join(shortest_path)} (Costo: {shortest_cost})")
    
    print("="*60)
    print("\nf. Desde computadoras del Switch 1 al servidor MongoDB:")
    
    # Buscar dispositivos conectados al Switch 1
    switch1_pos = network.search("Switch 1", "value")
    if switch1_pos is not None:
        connected_devices = []
        for edge in network[switch1_pos].edges:
            device_name = edge.value
            device_type = network.get_device_type(device_name)
            if device_type in ["pc", "notebook"]:  # Computadoras
                connected_devices.append(device_name)
        
        print(f"Computadoras conectadas al Switch 1: {connected_devices}")
        
        shortest_path_mongo = None
        shortest_cost_mongo = float('inf')
        best_pc_mongo = None
        
        for device in connected_devices:
            path, cost = network.find_shortest_path_dijkstra(device, "MongoDB")
            if cost is not None and cost < shortest_cost_mongo:
                shortest_cost_mongo = cost
                shortest_path_mongo = path
                best_pc_mongo = device
            if path:
                print(f"Desde {device}: {' -> '.join(path)} (Costo: {cost})")
        
        print(f"\nEl camino MÁS CORTO al MongoDB es desde {best_pc_mongo}: {' -> '.join(shortest_path_mongo)} (Costo: {shortest_cost_mongo})")
    
    print("="*60)
    print("\ng. Cambiar impresora al Router 2 y repetir barridos:")
    
    # Eliminar conexión actual de la impresora
    network.delete_edge("Switch 1", "Impresora", "value")
    # Conectar al Router 2 (asumiendo peso similar)
    network.insert_edge("Router 2", "Impresora", 25)
    
    print("\nImpresora reconectada al Router 2")
    print("Repitiendo barridos desde notebooks:")
    
    for notebook in notebooks:
        print(f"\n--- Barridos desde {notebook} (nueva configuración) ---")
        
        print(f"Barrido en PROFUNDIDAD desde {notebook}:")
        network.deep_sweep(notebook)
        
        print(f"\nBarrido en AMPLITUD desde {notebook}:")
        network.amplitude_sweep(notebook)
        print()

if __name__ == "__main__":
    resolver()
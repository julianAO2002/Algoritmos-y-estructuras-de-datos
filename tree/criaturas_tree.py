from tree import BinaryTree
from creatures import creatures
from collections import Counter

class CriaturasTree(BinaryTree):
    """
    Clase que implementa un árbol binario para manejar criaturas mitológicas.
    Extiende la funcionalidad de BinaryTree para resolver consultas específicas.
    """
    
    def __init__(self):
        super().__init__()
        self.load_creatures()
    
    def load_creatures(self):
        """Carga todas las criaturas del archivo creatures.py en el árbol."""
        for creature in creatures:
            # Crear datos completos de la criatura
            creature_data = {
                'name': creature['name'],
                'defeated_by': creature['defeated_by'],
                'description': '',  # Inicialmente vacía
                'captured_by': None  # Inicialmente no capturada
            }
            self.insert(creature['name'], creature_data)
    
    def add_description(self, creature_name, description):
        """Permite cargar una breve descripción sobre cada criatura."""
        node = self.search(creature_name)
        if node:
            node.other_values['description'] = description
            print(f"Descripción agregada para {creature_name}")
        else:
            print(f"Criatura {creature_name} no encontrada")
    
    def inorder_creatures_and_defeaters(self):
        """a. Listado inorden de las criaturas y quienes la derrotaron."""
        print("=== LISTADO INORDEN DE CRIATURAS Y SUS DERROTADORES ===")
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                defeated_by = root.other_values['defeated_by'] if root.other_values['defeated_by'] else "No derrotada"
                print(f"Criatura: {root.value} | Derrotada por: {defeated_by}")
                __in_order(root.right)
        
        if self.root is not None:
            __in_order(self.root)
    
    def show_talos_info(self):
        """c. Mostrar toda la información de la criatura Talos."""
        print("=== INFORMACIÓN DE TALOS ===")
        talos = self.search("Talos")
        if talos:
            data = talos.other_values
            print(f"Nombre: {talos.value}")
            print(f"Derrotada por: {data['defeated_by'] if data['defeated_by'] else 'No derrotada'}")
            print(f"Descripción: {data['description'] if data['description'] else 'Sin descripción'}")
            print(f"Capturada por: {data['captured_by'] if data['captured_by'] else 'No capturada'}")
        else:
            print("Talos no encontrada")
    
    def top_three_defeaters(self):
        """d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas."""
        print("=== TOP 3 DERROTADORES DE CRIATURAS ===")
        defeaters = []
        
        def __collect_defeaters(root):
            if root is not None:
                if root.other_values['defeated_by']:
                    defeaters.append(root.other_values['defeated_by'])
                __collect_defeaters(root.left)
                __collect_defeaters(root.right)
        
        if self.root is not None:
            __collect_defeaters(self.root)
        
        # Contar cuántas veces aparece cada derrotador
        counter = Counter(defeaters)
        # Obtener los 3 derrotadores con más criaturas derrotadas
        top_three = counter.most_common(3)
        
        for i in range(len(top_three)):
            hero = top_three[i][0]
            count = top_three[i][1]
            position = i + 1
            print(f"{position}. {hero}: {count} criaturas derrotadas")
    
    def creatures_defeated_by_heracles(self):
        """e. Listar las criaturas derrotadas por Heracles."""
        print("=== CRIATURAS DERROTADAS POR HERACLES ===")
        
        def __find_heracles_victims(root):
            if root is not None:
                if root.other_values['defeated_by'] == "Heracles":
                    print(f"- {root.value}")
                __find_heracles_victims(root.left)
                __find_heracles_victims(root.right)
        
        if self.root is not None:
            __find_heracles_victims(self.root)
    
    def undefeated_creatures(self):
        """f. Listar las criaturas que no han sido derrotadas."""
        print("=== CRIATURAS NO DERROTADAS ===")
        
        def __find_undefeated(root):
            if root is not None:
                if root.other_values['defeated_by'] is None:
                    print(f"- {root.value}")
                __find_undefeated(root.left)
                __find_undefeated(root.right)
        
        if self.root is not None:
            __find_undefeated(self.root)
    
    def capture_creatures_by_heracles(self):
        """h. Modificar los nodos indicando que Heracles capturó ciertas criaturas."""
        creatures_to_capture = ["Cerberus", "Cretan Bull", "Ceryneian Hind", "Erymanthian Boar"]
        
        print("=== MARCANDO CRIATURAS CAPTURADAS POR HERACLES ===")
        for creature_name in creatures_to_capture:
            node = self.search(creature_name)
            if node:
                node.other_values['captured_by'] = "Heracles"
                print(f"OK - {creature_name} capturada por Heracles")
            else:
                print(f"ERROR - {creature_name} no encontrada")
    
    def search_by_coincidence(self, pattern):
        """i. Búsquedas por coincidencia."""
        print(f"=== BÚSQUEDA POR COINCIDENCIA: '{pattern}' ===")
        results = []
        
        def __search_pattern(root):
            if root is not None:
                if pattern.lower() in root.value.lower():
                    results.append(root.value)
                __search_pattern(root.left)
                __search_pattern(root.right)
        
        if self.root is not None:
            __search_pattern(self.root)
        
        if results:
            for creature in results:
                print(f"- {creature}")
        else:
            print("No se encontraron coincidencias")
        
        return results
    
    def delete_creatures(self, creatures_names):
        """j. Eliminar criaturas especificadas."""
        print("=== ELIMINANDO CRIATURAS ===")
        for creature_name in creatures_names:
            deleted_value, deleted_data = self.delete(creature_name)
            if deleted_value:
                defeated_by = deleted_data['defeated_by'] if deleted_data['defeated_by'] else "nadie"
                print(f"OK - {creature_name} eliminada del árbol (era derrotada por {defeated_by})")
            else:
                print(f"ERROR - {creature_name} no encontrada")
    
    def modify_stymphalian_birds(self):
        """k. Modificar el nodo de las Aves del Estínfalo."""
        print("=== MODIFICANDO AVES DEL ESTÍNFALO ===")
        birds = self.search("Stymphalian Birds")
        if birds:
            birds.other_values['defeated_by'] = "Heracles"
            birds.other_values['description'] = "Heracles derrotó a varias de estas aves"
            print("OK - Aves del Estínfalo modificadas: Heracles derrotó a varias")
        else:
            print("ERROR - Aves del Estínfalo no encontradas")
    
    def rename_ladon(self):
        """l. Modificar el nombre de Ladón por Dragón Ladón."""
        print("=== RENOMBRANDO LADÓN ===")
        ladon = self.search("Ladon")
        if ladon:
            # Guardar datos
            old_data = ladon.other_values.copy()
            # Eliminar el nodo actual
            self.delete("Ladon")
            # Insertar con el nuevo nombre
            self.insert("Dragón Ladón", old_data)
            print("OK - Ladón renombrado a 'Dragón Ladón'")
        else:
            print("ERROR - Ladón no encontrado")
    
    def list_by_level(self):
        """m. Realizar un listado por nivel del árbol."""
        print("=== LISTADO POR NIVEL DEL ÁRBOL ===")
        from Queue_ import Queue
        
        # Verificar si el árbol está vacío
        if self.root is None:
            print("Árbol vacío")
            return
        
        # Crear cola para el recorrido por niveles
        tree_queue = Queue()
        tree_queue.arrive((self.root, 0))  # Agregar raíz con nivel 0
        current_level = 0
        
        # Procesar todos los nodos nivel por nivel
        while tree_queue.size() > 0:
            # Sacar el próximo nodo de la cola
            node, level = tree_queue.attention()
            
            # Si cambiamos de nivel, mostrar el nuevo nivel
            if level > current_level:
                print(f"\nNivel {level}:")
                current_level = level
            
            # Mostrar el nombre de la criatura
            print(f"  - {node.value}")
            
            # Agregar hijos a la cola con el nivel siguiente
            if node.left is not None:
                tree_queue.arrive((node.left, level + 1))
            if node.right is not None:
                tree_queue.arrive((node.right, level + 1))
    
    def creatures_captured_by_heracles(self):
        """n. Mostrar las criaturas capturadas por Heracles."""
        print("=== CRIATURAS CAPTURADAS POR HERACLES ===")
        
        def __find_captured_by_heracles(root):
            if root is not None:
                if root.other_values['captured_by'] == "Heracles":
                    print(f"- {root.value}")
                __find_captured_by_heracles(root.left)
                __find_captured_by_heracles(root.right)
        
        if self.root is not None:
            __find_captured_by_heracles(self.root)


if __name__ == "__main__":
    # Crear el árbol de criaturas
    criaturas_tree = CriaturasTree()
    
    # a. Listado inorden de las criaturas y quienes la derrotaron
    criaturas_tree.inorder_creatures_and_defeaters()
    print("\n" + "="*60 + "\n")
    
    # b. Cargar descripciones (ejemplos)
    print("=== CARGANDO DESCRIPCIONES DE EJEMPLO ===")
    criaturas_tree.add_description("Talos", "Gigante de bronce que protegía la isla de Creta")
    criaturas_tree.add_description("Medusa", "Gorgona con serpientes por cabello que convertía en piedra")
    criaturas_tree.add_description("Chimera", "Criatura con cabeza de león, cuerpo de cabra y cola de serpiente")
    print("\n" + "="*60 + "\n")
    
    # c. Mostrar toda la información de Talos
    criaturas_tree.show_talos_info()
    print("\n" + "="*60 + "\n")
    
    # d. Top 3 derrotadores
    criaturas_tree.top_three_defeaters()
    print("\n" + "="*60 + "\n")
    
    # e. Criaturas derrotadas por Heracles
    criaturas_tree.creatures_defeated_by_heracles()
    print("\n" + "="*60 + "\n")
    
    # f. Criaturas no derrotadas
    criaturas_tree.undefeated_creatures()
    print("\n" + "="*60 + "\n")
    
    # g & h. Capturar criaturas con Heracles
    criaturas_tree.capture_creatures_by_heracles()
    print("\n" + "="*60 + "\n")
    
    # i. Búsqueda por coincidencia
    criaturas_tree.search_by_coincidence("C")
    print("\n" + "="*60 + "\n")
    
    # j. Eliminar Basilisco y Sirenas
    criaturas_tree.delete_creatures(["Basilisk", "Sirens"])
    print("\n" + "="*60 + "\n")
    
    # k. Modificar Aves del Estínfalo
    criaturas_tree.modify_stymphalian_birds()
    print("\n" + "="*60 + "\n")
    
    # l. Renombrar Ladón
    criaturas_tree.rename_ladon()
    print("\n" + "="*60 + "\n")
    
    # m. Listado por nivel
    criaturas_tree.list_by_level()
    print("\n" + "="*60 + "\n")
    
    # n. Criaturas capturadas por Heracles
    criaturas_tree.creatures_captured_by_heracles()
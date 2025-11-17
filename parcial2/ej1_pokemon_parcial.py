"""Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, 
número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y 
si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de 
manera eficiente a los datos contemplando lo siguiente:
a.los índices de cada uno de los árboles deben ser nombre, número y tipo;
b.mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
c.mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
d.realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
e.mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
c.mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
d.determinar cuantos Pokémons tienen megaevolucion.
e.determinar cuantos Pokémons tiene forma gigamax."""


from tree import BinaryTree

# Lista de Pokémons para el parcial (25 pokémons con un tipo cada uno)
pokemon_data = [
    {"nombre": "Pikachu", "numero": 25, "tipo": "eléctrico", "debilidades": ["tierra"], "mega_evolucion": False, "forma_gigamax": True},
    {"nombre": "Charizard", "numero": 6, "tipo": "fuego", "debilidades": ["agua", "eléctrico", "roca"], "mega_evolucion": True, "forma_gigamax": True},
    {"nombre": "Bulbasaur", "numero": 1, "tipo": "planta", "debilidades": ["fuego", "psíquico", "volador", "hielo"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Squirtle", "numero": 7, "tipo": "agua", "debilidades": ["planta", "eléctrico"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Gengar", "numero": 94, "tipo": "fantasma", "debilidades": ["fantasma", "siniestro", "tierra", "psíquico"], "mega_evolucion": True, "forma_gigamax": True},
    {"nombre": "Alakazam", "numero": 65, "tipo": "psíquico", "debilidades": ["bicho", "fantasma", "siniestro"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Machamp", "numero": 68, "tipo": "lucha", "debilidades": ["volador", "psíquico", "hada"], "mega_evolucion": False, "forma_gigamax": True},
    {"nombre": "Jolteon", "numero": 135, "tipo": "eléctrico", "debilidades": ["tierra"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Lycanroc", "numero": 745, "tipo": "roca", "debilidades": ["agua", "planta", "lucha", "tierra", "acero"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": "dragón", "debilidades": ["lucha", "tierra", "acero", "agua", "planta", "hielo", "dragón", "hada"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Lucario", "numero": 448, "tipo": "acero", "debilidades": ["fuego", "lucha", "tierra"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Garchomp", "numero": 445, "tipo": "dragón", "debilidades": ["hielo", "dragón", "hada"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Mewtwo", "numero": 150, "tipo": "psíquico", "debilidades": ["bicho", "fantasma", "siniestro"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Rayquaza", "numero": 384, "tipo": "dragón", "debilidades": ["hielo", "roca", "dragón", "hada"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Rotom", "numero": 479, "tipo": "eléctrico", "debilidades": ["tierra", "fantasma", "siniestro"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Dialga", "numero": 483, "tipo": "acero", "debilidades": ["lucha", "tierra", "fuego"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Palkia", "numero": 484, "tipo": "agua", "debilidades": ["dragón", "hada"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Giratina", "numero": 487, "tipo": "fantasma", "debilidades": ["hielo", "fantasma", "dragón", "siniestro", "hada"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Blaziken", "numero": 257, "tipo": "fuego", "debilidades": ["agua", "tierra", "volador", "psíquico"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Sceptile", "numero": 254, "tipo": "planta", "debilidades": ["fuego", "hielo", "veneno", "volador", "bicho"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Swampert", "numero": 260, "tipo": "agua", "debilidades": ["planta"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Aggron", "numero": 306, "tipo": "acero", "debilidades": ["lucha", "tierra", "fuego", "agua"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Metagross", "numero": 376, "tipo": "acero", "debilidades": ["fuego", "tierra", "fantasma", "siniestro"], "mega_evolucion": True, "forma_gigamax": False},
    {"nombre": "Bulbizarre", "numero": 128, "tipo": "planta", "debilidades": ["fuego", "hielo", "volador"], "mega_evolucion": False, "forma_gigamax": False},
    {"nombre": "Electivire", "numero": 466, "tipo": "eléctrico", "debilidades": ["tierra"], "mega_evolucion": False, "forma_gigamax": False}
]

class PokemonTreeByName(BinaryTree):
    """Árbol binario de búsqueda por nombre de Pokémon"""
    
    def show_pokemon_data(self, name):
        """Muestra todos los datos de un Pokémon por nombre"""
        node = self.search(name)
        if node:
            pokemon = node.other_values
            print(f"\n=== DATOS DE {pokemon['nombre'].upper()} ===")
            print(f"Número: {pokemon['numero']}")
            print(f"Tipo: {pokemon['tipo']}")
            print(f"Debilidades: {', '.join(pokemon['debilidades'])}")
            print(f"Mega Evolución: {'Sí' if pokemon['mega_evolucion'] else 'No'}")
            print(f"Forma Gigamax: {'Sí' if pokemon['forma_gigamax'] else 'No'}")
        else:
            print(f"No se encontró el Pokémon: {name}")
    


class PokemonTreeByNumber(BinaryTree):
    """Árbol binario de búsqueda por número de Pokémon"""
    
    def show_pokemon_by_number(self, number):
        """Muestra todos los datos de un Pokémon por número"""
        node = self.search(number)
        if node:
            pokemon = node.other_values
            print(f"\n=== POKÉMON #{number} ===")
            print(f"Nombre: {pokemon['nombre']}")
            print(f"Tipo: {pokemon['tipo']}")
            print(f"Debilidades: {', '.join(pokemon['debilidades'])}")
            print(f"Mega Evolución: {'Sí' if pokemon['mega_evolucion'] else 'No'}")
            print(f"Forma Gigamax: {'Sí' if pokemon['forma_gigamax'] else 'No'}")
        else:
            print(f"No se encontró el Pokémon #{number}")
    


class PokemonTreeByType(BinaryTree):
    """Árbol binario de búsqueda por tipo de Pokémon"""
    
    def show_pokemons_by_type(self, pokemon_type):
        """Muestra todos los Pokémons de un tipo específico"""
        results = []
        
        def __search_by_type(root, pokemon_type, results):
            if root is not None:
                if root.value == pokemon_type:
                    results.append(root.other_values)
                __search_by_type(root.left, pokemon_type, results)
                __search_by_type(root.right, pokemon_type, results)
        
        __search_by_type(self.root, pokemon_type, results)
        return results

class PokemonManager:
    """Gestor principal que maneja los tres árboles de Pokémon"""
    
    def __init__(self):
        self.tree_by_name = PokemonTreeByName()
        self.tree_by_number = PokemonTreeByNumber()  
        self.tree_by_type = PokemonTreeByType()
        self.pokemons = []
    
    def load_pokemons(self):
        """Carga todos los Pokémons en los tres árboles"""
        print("Cargando base de datos de Pokémon...")
        
        for pokemon in pokemon_data:
            self.pokemons.append(pokemon)
            
            # Árbol por nombre
            self.tree_by_name.insert(pokemon["nombre"], pokemon)
            
            # Árbol por número
            self.tree_by_number.insert(pokemon["numero"], pokemon)
            
            # Árbol por tipo (un tipo por pokémon)
            self.tree_by_type.insert(pokemon["tipo"], pokemon)
        
        print(f"{len(pokemon_data)} Pokémons cargados exitosamente.")
    
    def search_by_proximity(self, pattern):
        """b. Búsqueda por proximidad de nombre"""
        print(f"\nBuscando Pokémons que contengan '{pattern}':")
        self.tree_by_name.proximity_search(pattern)
    
    def show_pokemons_by_types(self, types_list):
        """c. Mostrar Pokémons por tipos específicos"""
        for tipo in types_list:
            print(f"\nPokémons de tipo {tipo.upper()}:")
            results = self.tree_by_type.show_pokemons_by_type(tipo)
            
            if results:
                for pokemon in results:
                    print(f"  • {pokemon['nombre']}")
            else:
                print(f"  No hay Pokémons de tipo {tipo}")
    
    def list_ascending_order(self):
        """d. Listados en orden ascendente"""
        print("\nLISTADO POR NÚMERO (ascendente):")
        self.tree_by_number.in_order()
        
        print("\nLISTADO POR NOMBRE (ascendente):")
        self.tree_by_name.in_order()
        
        print("\nLISTADO POR NIVELES (por nombre):")
        self.tree_by_name.by_level()
    
    def find_weak_against_pokemons(self):
        """e. Pokémons débiles contra Jolteon, Lycanroc y Tyrantrum"""
        target_pokemons = ["Jolteon", "Lycanroc", "Tyrantrum"]
        
        # Obtener los tipos de estos Pokémons
        target_types = []
        for target_name in target_pokemons:
            node = self.tree_by_name.search(target_name)
            if node:
                target_types.append(node.other_values["tipo"])
        
        print(f"\nPokémons débiles contra {', '.join(target_pokemons)}:")
        print(f"   (Débiles a tipos: {', '.join(set(target_types))})")
        
        # Recorrer todos los Pokémons y verificar si tienen debilidades contra los tipos objetivo
        weak_pokemons = []
        for pokemon in self.pokemons:            
            for weakness in pokemon["debilidades"]:
                if weakness in target_types:
                    weak_pokemons.append(pokemon)
                    break  
        
        # Mostrar los Pokémons débiles con sus debilidades específicas
        for pokemon in weak_pokemons:
            shared_weaknesses = []
            for w in pokemon["debilidades"]:
                if w in target_types:
                    shared_weaknesses.append(w)
            print(f"  • {pokemon['nombre']} - débil a: {', '.join(shared_weaknesses)}")
    
    def count_types(self):
        """f. Contar tipos de Pokémons"""
        print("\nESTADÍSTICAS DE TIPOS:")
        type_count = {}
        
        for pokemon in self.pokemons:
            tipo = pokemon["tipo"]
            type_count[tipo] = type_count.get(tipo, 0) + 1
        
        # Ordenar por cantidad
        sorted_types = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
        
        for tipo, cantidad in sorted_types:
            print(f"  {tipo.capitalize():12} : {cantidad:2d} Pokémons")
    
    def count_mega_evolutions(self):
        """g. Contar Pokémons con mega evolución"""
        mega_count = 0
        for pokemon in self.pokemons:
            if pokemon["mega_evolucion"]:
                mega_count += 1
        total = len(self.pokemons)
        
        print(f"\nMEGA EVOLUCIONES:")
        print(f"  Con Mega Evolución: {mega_count}/{total}")
        print(f"  Porcentaje: {(mega_count/total)*100:.1f}%")
        
        print("  Pokémons con Mega Evolución:")
        for pokemon in self.pokemons:
            if pokemon["mega_evolucion"]:
                print(f"    • {pokemon['nombre']}")
    
    def count_gigamax_forms(self):
        """h. Contar Pokémons con forma Gigamax"""
        gigamax_count = 0
        for pokemon in self.pokemons:
            if pokemon["forma_gigamax"]:
                gigamax_count += 1
        total = len(self.pokemons)
        
        print(f"\nFORMAS GIGAMAX:")
        print(f"  Con Forma Gigamax: {gigamax_count}/{total}")
        print(f"  Porcentaje: {(gigamax_count/total)*100:.1f}%")
        
        print("  Pokémons con Forma Gigamax:")
        for pokemon in self.pokemons:
            if pokemon["forma_gigamax"]:
                print(f"    • {pokemon['nombre']}")

def solve_pokemon_parcial():
    """Función principal que resuelve todos los ejercicios del parcial"""
    print("="*60)
    print("PARCIAL 2 - EJERCICIO 1: POKÉDEX CON ÁRBOLES")
    print("="*60)
    
    # Crear el gestor de Pokémons
    manager = PokemonManager()
    
    # a. Cargar los tres árboles
    manager.load_pokemons()
    
    print("\n" + "="*60)
    
    # b. Búsquedas por número y proximidad
    print("\nPUNTO B: BÚSQUEDAS")
    print("\nBúsqueda por número:")
    manager.tree_by_number.show_pokemon_by_number(25)  # Pikachu
    print("\nBúsqueda por proximidad de nombre:")
    manager.search_by_proximity("bul")  # Debería encontrar Bulbasaur y Bulbizarre
    
    # c. Pokémons por tipos específicos
    print("\n" + "="*40)
    print("PUNTO C: POKÉMONS POR TIPO")
    manager.show_pokemons_by_types(["fantasma", "fuego", "acero", "eléctrico"])
    
    # d. Listados ordenados
    print("\n" + "="*40)
    print("PUNTO D: LISTADOS ORDENADOS")
    manager.list_ascending_order()
    
    # e. Débiles contra Jolteon, Lycanroc y Tyrantrum
    print("\n" + "="*40)
    print("PUNTO E: DEBILIDADES")
    manager.find_weak_against_pokemons()
    
    # f. Estadísticas de tipos
    print("\n" + "="*40)
    print("PUNTO F: ESTADÍSTICAS")
    manager.count_types()
    
    # g. Mega evoluciones
    print("\n" + "="*40)
    print("PUNTO G: MEGA EVOLUCIONES")
    manager.count_mega_evolutions()
    
    # h. Formas Gigamax
    print("\n" + "="*40)
    print("PUNTO H: FORMAS GIGAMAX")
    manager.count_gigamax_forms()
    
    print("\n" + "="*60)


if __name__ == "__main__":
    solve_pokemon_parcial()
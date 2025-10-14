from tree import BinaryTree
from super_heroes_data import superheroes

class SuperHeroTree(BinaryTree):
    def villain_in_order(self):
            def __villain_in_order(root):
                if root is not None:
                    __villain_in_order(root.left)
                    if root.other_values["is_villain"] is True:
                        print(root.value)
                    __villain_in_order(root.right)

            if self.root is not None:
                __villain_in_order(self.root)

    def divide_tree(self, arbol_h, arbol_v):
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)


        __divide_tree(self.root, arbol_h, arbol_v)

    def hero_start_with_c(self):
        def __hero_start_with_c(root):
            if root is not None:
                __hero_start_with_c(root.left)
                if root.value.startswith('C'):
                    print(root.value)
                __hero_start_with_c(root.right)

        if self.root is not None:
            __hero_start_with_c(self.root)



arbol = SuperHeroTree()
arbol_heroes = SuperHeroTree()
arbol_villanos = SuperHeroTree()


for super_hero in superheroes:
    arbol.insert(super_hero['name'], super_hero)


# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
arbol.divide_tree(arbol_heroes, arbol_villanos)

bosque = [arbol_heroes, arbol_villanos]

# b. listar los villanos ordenados alfabéticamente;
arbol_villanos.villain_in_order()

# c. mostrar todos los superhéroes que empiezan con C;  
arbol_heroes.hero_start_with_c()

# d. determinar cuántos superhéroes hay el árbol;
print(arbol_heroes.count_nodes())

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;

arbol.proximity_search('Dr')
name = input('ingrese nombre para modificar: ')
value, other_value = arbol.delete(name)

# f. listar los superhéroes ordenados de manera descendente;
arbol_heroes.post_order()

# G.1. determinar cuántos nodos tiene cada árbol;

for tree in bosque: 
    print(f'Cantidad de nodos en el arbol: {tree.count_nodes()}')
    

# G.2. II. realizar un barrido ordenado alfabéticamente de cada árbol;
arbol_heroes.in_order()
arbol_villanos.in_order()
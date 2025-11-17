from typing import Any

class HeapMax:
    """Max-heap: el elemento mayor siempre está en la raíz"""

    def __init__(self):
        self.elements = []  # Lista que representa el árbol binario
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        """Agrega un elemento y mantiene la propiedad del heap"""
        self.elements.append(value)  # Agregar al final
        self.float(self.size()-1)    # Flotar hacia arriba si es necesario
    
    def remove(self) -> Any:
        """Elimina y retorna el máximo (raíz)"""
        last = self.size() -1
        self.interchange(0, last)     # Poner el último en la raíz
        value = self.elements.pop()   # Extraer el máximo
        self.sink(0)                  # Hundir la nueva raíz
        return value

    def float(self, index: int) -> None:
        """Mueve un elemento hacia arriba hasta su posición correcta"""
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """Mueve un elemento hacia abajo hasta su posición correcta"""
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            # Encontrar el hijo mayor
            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            # Si el padre es menor que el hijo mayor, intercambiar
            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False  # Ya está en la posición correcta


    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def attention(self) -> Any:
        value = self.remove()
        return value


class HeapMin:
    """Min-heap: el elemento menor siempre está en la raíz"""

    def __init__(self):
        self.elements = []  # Lista que representa el árbol binario
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        """Agrega un elemento y mantiene la propiedad del min-heap"""
        self.elements.append(value)
        self.float(self.size()-1)
    
    def search(self, value):
        """Busca un valor en el heap y retorna su índice"""
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def remove(self) -> Any:
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """Cola de prioridad: agrega elemento con prioridad (1=baja, 2=media, 3=alta)"""
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def attention(self) -> Any:
        """Cola de prioridad: atiende al elemento de mayor prioridad"""
        value = self.remove()
        return value

    def change_priority(self, index, new_priority):
        """Cambia la prioridad de un elemento y reajusta el heap"""
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            # Reajustar según si aumentó o disminuyó la prioridad
            if new_priority > previous_priority:
                self.sink(index)   # Mayor prioridad = hundir en min-heap
            elif new_priority < previous_priority:
                self.float(index)  # Menor prioridad = flotar en min-heap

# priority_queue = HeapMin()

# priority_queue.arrive('x', 1)
# priority_queue.arrive('b', 2)
# priority_queue.arrive('a', 2)
# priority_queue.arrive('f', 1)
# priority_queue.arrive('y', 1)
# priority_queue.arrive('j', 2)
# priority_queue.arrive('z', 3)
# print(priority_queue.elements)

# while priority_queue.size() > 0:
#     print(priority_queue.attention())

# h = HeapMin()
# h.add(19)
# h.add(5)
# h.add(1)
# h.add(3)
# h.add(9)


# list_sort = h.heapsort()

# print(list_sort)
# print(h.elements)
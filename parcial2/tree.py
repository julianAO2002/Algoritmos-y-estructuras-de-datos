from typing import Any, Optional
from queue_ import Queue

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.hight = 0

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_hight(root)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)
    #orden ascendente
    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)
    #orden descendente
    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def hight(self, root):
        if root is None:
            return -1
        else:
            return root.hight

    def update_hight(self, root):
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_hight(root)
        self.update_hight(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control: # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.hight(root.left) - self.hight(root.right) == 2:
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.hight(root.right) - self.hight(root.left) == 2:
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root
    
    def count_nodes(self):
        """Devuelve la cantidad total de nodos en el árbol."""
        def _count(root):
            if root is None:
                return 0
            return 1 + _count(root.left) + _count(root.right)

        return _count(self.root)
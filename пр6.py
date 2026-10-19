class ArrayStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Вставляє об'єкт на вершину стеку"""
        self._items.append(item)

    def pop(self):
        """Повертає елемент з вершини стеку та видаляє його"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Повертає елемент з вершини стеку"""
        if self.is_empty():
            return None
        return self._items[-1]

    def clear(self):
        """Видаляє всі елементи з стеку"""
        self._items.clear()

    def count(self):
        """Повертає кількість елементів стеку"""
        return len(self._items)

    def size(self):
        """Повертає кількість елементів у стеку"""
        return len(self._items)

    def is_empty(self):
        """Перевіряє, чи порожній стек"""
        return len(self._items) == 0

    def toString(self):
        """Виводить всі елементи стеку, але не видаляє їх"""
        return " -> ".join(map(str, reversed(self._items))) if self._items else "Stack is empty"

    def __str__(self):
        return self.toString()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Посилання на попередній вузол нижче у стеку


class LinkedStack:
    def __init__(self):
        self.top = None  # top рівне None (null) - стек порожній
        self._size = 0

    def push(self, item):
        """Вставляє об'єкт на вершину стеку"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Повертає елемент з вершини стеку та видаляє його"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        """Повертає елемент з вершини стеку"""
        if self.is_empty():
            return None
        return self.top.data

    def clear(self):
        """Видаляє всі елементи з стеку"""
        self.top = None
        self._size = 0

    def count(self):
        """Повертає кількість елементів стеку"""
        return self._size

    def size(self):
        """Повертає кількість елементів у стеку"""
        return self._size

    def is_empty(self):
        """Перевіряє, чи стек порожній"""
        return self.top is None

    def toString(self):
        """Виводить всі елементи стеку, але не видаляє їх"""
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Stack is empty"

    def __str__(self):
        return self.toString()



if __name__ == "__main__":
    print("=== 1. ТЕСТУВАННЯ ARRAY STACK (Масив) ===")
    arr_stack = ArrayStack()
    arr_stack.push(11)
    arr_stack.push(22)
    arr_stack.push(33)

    print("Елементи стеку (toString):", arr_stack.toString())
    print("Кількість елементів (count/size):", arr_stack.count())
    print("Вершина стеку (peek):", arr_stack.peek())
    print("Видалено елемент (pop):", arr_stack.pop())
    print("Після pop (toString):", arr_stack.toString())
    arr_stack.clear()
    print("Після clear (toString):", arr_stack.toString())

    print("\n=== 2. ТЕСТУВАННЯ LINKED STACK (Вузли) ===")
    link_stack = LinkedStack()
    link_stack.push(11)
    link_stack.push(22)
    link_stack.push(33)

    print("Елементи стеку (top -> base):", link_stack.toString())
    print("Кількість елементів (count/size):", link_stack.size())
    print("Вершина стеку (peek):", link_stack.peek())
    print("Видалено елемент (pop):", link_stack.pop())
    print("Після pop (toString):", link_stack.toString())
    link_stack.clear()
    print("Після clear (toString):", link_stack.toString())
class Node:
    def __init__(self, _value):
        self._value = _value
        self.next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _value):
        self._value = _value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):  # Add new node to the list.
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def print_list(self):  # Print the list.
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print(None)


linkedlist = LinkedList()
linkedlist.append(2)
linkedlist.append(1)
linkedlist.append(6)
linkedlist.append(9)
linkedlist.append(3)
linkedlist.append(8)
linkedlist.print_list()

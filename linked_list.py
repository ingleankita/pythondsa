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

    def length(self):  # Get length of list.
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def get_position(self, query):  # Get the first occurrence of a value.
        index = 0
        current = self.head
        while current is not None:
            if current.value == query:
                return index
            current = current.next
            index += 1
        return -1


linkedlist = LinkedList()
linkedlist.append(21)
linkedlist.append(15)
linkedlist.append(31)
linkedlist.append(16)
linkedlist.append(23)
linkedlist.append(13)
linkedlist.print_list()
print(linkedlist.get_position(16))

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
    # Time complexity: O(1); single "head" pointer initialized
    # Space complexity: O(1); constant space for single "head" pointer
    def __init__(self):
        self.head = None

    # Time complexity: O(n); need to traverse entire list to append element at the tail
    # Space complexity: O(1); constant amount of additional space, for single "current" pointer
    def append(self, value):  # Add new node to the list.
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    # Time complexity: O(n); need to traverse entire list to print each value
    # Space complexity: O(1); constant amount of additional space, for single "current" pointer
    def print_list(self):  # Print the list.
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print(None)

    # Time complexity: O(n); need to traverse entire list to count elements
    # Space complexity: O(1); constant number of pointers assigned
    def length(self):  # Get length of list.
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    # Time complexity: O(n); need to traverse entire list in worst case to get the queried value's index
    # Space complexity: O(1); constant number of pointers assigned
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

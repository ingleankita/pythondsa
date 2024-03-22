"""Implement the hash table data structure"""


# Hash tables rely on a hash function, which takes a key as input and returns an index (often called a hash code)
# within a fixed range (the size of the array). This hash function should ideally distribute keys evenly across the
# available array indices.

# The hash table consists of an array of fixed size, often called buckets or slots. Each slot can hold either a
# key-value pair or a pointer to a linked list or another data structure that can handle collisions.


class HashTable:
    def __init__(self, max_size=4069):
        """Create a hast table of given size"""
        self.list = [None] * max_size

    # Time complexity: O(k) where k is size of key string
    def hash_key_and_get_index(self, string_key):
        """algorithm for hashing a key to a list index: convert each char of the string to a number using python's
        built-in ord function, get the hash of the string by summing all these numbers, the sum modulo hash table size is
        the index"""
        sum_of_chars = 0
        for char in string_key:
            sum_of_chars += ord(char)
        return sum_of_chars % len(self.list)

    # Time complexity: O(1) excluding the hashing operation
    def insert(self, key, value):
        """Insert a new key-value pair"""
        index = self.hash_key_and_get_index(key)
        self.list[index] = (key, value)

    # Time complexity: O(1) excluding the hashing operation
    def find(self, key):
        """Get the value given a key"""
        return self.list[self.hash_key_and_get_index(key)][1]

    # Time complexity: O(1) excluding the hashing operation
    def update(self, key, value):
        """Change the value associated with the given key"""
        index = self.hash_key_and_get_index(key)
        self.list[index] = (key, value)

    # Time complexity: O(n)
    def list_keys(self):
        """List all keys in the hash table"""
        return [kv[0] for kv in self.list if kv is not None]

    # Time complexity: O(n)
    def show_list(self):
        return [kv for kv in self.list if kv is not None]


my_hash_table = HashTable()
my_hash_table.insert('Apple', 48)
my_hash_table.insert('Banana', 123)
my_hash_table.insert('Mango', 13)

print(my_hash_table.show_list())


class HashTableWithLinearProbing:
    def __init__(self, max_size=4069):
        """Create a hast table of given size"""
        self.list = [None] * max_size

    def hash_key_and_get_index(self, string_key):
        """algorithm for hashing a key to a list index: convert each char of the string to a number using python's
        built-in ord function, get the hash of the string by summing all these numbers, the sum modulo hash table size is
        the index"""
        sum_of_chars = 0
        for char in string_key:
            sum_of_chars += ord(char)
        return sum_of_chars % len(self.list)

    # Time complexity: O(n)
    def probe_for_index(self, key):
        """When multiple keys have the same hash, this is referred to as a collision (addressed using Linear Probing)"""
        # Find the nearest empty index or index with matching key
        index_after_probing = self.hash_key_and_get_index(key)
        while True:
            if self.list[index_after_probing] is None or self.list[index_after_probing][0] == key:
                return index_after_probing
            index_after_probing = (index_after_probing + 1) % len(self.list)

    # Time complexity: O(n) for probing
    def insert(self, key, value):
        """Insert a new key-value pair; if key already exists, probing will simply update that position"""
        index = self.probe_for_index(key)
        self.list[index] = (key, value)

    # Time complexity: O(n) for probing
    def find(self, key):
        """Get the value given a key"""
        return self.list[self.probe_for_index(key)][1]

    # Time complexity: O(n) for probing
    def update(self, key, value):
        """Change the value associated with the given key"""
        index = self.probe_for_index(key)
        self.list[index] = (key, value)

    # Time complexity: O(n)
    def list_keys(self):
        """List all keys in the hash table"""
        return [kv[0] for kv in self.list if kv is not None]

    # Time complexity: O(n)
    def show_list(self):
        return [kv for kv in self.list if kv is not None]


my_probing_hash_table = HashTableWithLinearProbing()
my_probing_hash_table.insert('listen', 48)
my_probing_hash_table.insert('silent', 123)
my_probing_hash_table.insert('listen', 783)

print(my_probing_hash_table.show_list())

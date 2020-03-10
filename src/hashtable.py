# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # print(f"Index for insert: {index}")

        if index < self.capacity and self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        elif index < self.capacity and self.storage[index] is not None:
            new_node = LinkedPair(key, value)
            new_node.next = self.storage[index]
            self.storage[index] = new_node
        else:
            return "ERROR: Index out of bounds"

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if index < self.capacity and self.storage[index] is not None:
            if self.storage[index].key is key:
                self.storage[index] = self.storage[index].next
            else:
                current_node = self.storage[index]
                eval_node = current_node.next
                while eval_node is not None:
                    if eval_node.key is key:
                        current_node.next = eval_node.next
                        return
                    current_node = current_node.next
                    eval_node = eval_node.next
        elif index < self.capacity and self.storage[index] is None:
            return f"ERROR: No value found for key '{key}'"
        else:
            return "ERROR: Index out of bounds"

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # print(f"Index for retrieve: {index}")
        if index < self.capacity and self.storage[index] is not None:
            current_node = self.storage[index]
            if current_node.key is key:
                return current_node.value
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.key is key:
                    return current_node.value
            return None
        elif index < self.capacity and self.storage[index] is None:
            return None
        else:
            return "ERROR: Index out of bounds"

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity
        self.storage = new_storage
        for bucket in old_storage:
            if bucket is not None:
                node = bucket
                self.insert(node.key, node.value)
                while node.next:
                    node = node.next
                    self.insert(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # ht.remove("line_2")
    # ht.remove("line_1")
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

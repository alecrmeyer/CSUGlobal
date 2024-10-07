class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.count = 0
        self.buckets = [None] * self.size

    def _hash(self, key): 
        mult = 1 
        hv = 0 
        for ch in key: 
            hv += mult * ord(ch) 
            mult += 1 
        return hv % self.size 
    
    def _get_index(self, key):
        search_hash = self._hash(key)

        while self.buckets[search_hash] is not None:
            if self.buckets[search_hash].key == key:
                return search_hash
            search_hash += (search_hash + 1) % self.size
        return None
    
    def insert(self, key, value):
        hashItem = HashItem(key, value)
        current_hash = self._hash(hashItem.key)
        
        if self.buckets[current_hash]:
            while self.buckets[current_hash] is not None:
                if self.buckets[current_hash].key == current_hash:
                    self.buckets[current_hash] = hashItem
                    return
                current_hash += (current_hash + 1) % self.size

        self.buckets[current_hash] = hashItem

    def search(self, key):
        index = self._get_index(key)
        if index:
            return self.buckets[index].value
        return None
    
    def delete(self, key):
        index = self._get_index(key)
        self.buckets[index] = None


hash_table = HashTable()
hash_table.insert("gaming", "Set of ads for gaming")
hash_table.insert("shopping", "Set of ads for shopping")
hash_table.insert("fitness", "Set of ads for fitness")
hash_table.insert("education", [1, 4, 3, 2, 5])

print(hash_table.search("shopping"))
hash_table.delete("shopping")
print(hash_table.search("shopping"))




            

    
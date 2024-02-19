#hashmap implementation

class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None]*self.size

    def hashFun(self, key):
        return key%self.size
    
    def add(self,key, val):
       key_val = self.hashFun(key)
       item = [key,val]
       self.map[key_val] = [item]
    

    def retreive(self, key):
        hash = self.hashFun(key)
        if self.map[hash] is not None:
            for counter in self.map[hash]:
                if counter[0] == key:
                    return counter[1]
        raise KeyError(str(key))
        
        

    def printMap(self):
        print(self.map)

hash = HashMap()
hash.add(22,"thirty three")
hash.printMap()
print(hash.retreive(33))


        

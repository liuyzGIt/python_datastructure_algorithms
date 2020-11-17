class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __lt__(self, other):
        return self.key < other.key
        
    def __le__(self, other):
        return self.key < other.key or self.key == other.key
        
    def __gt__(self, other):
        return self.key > other.key
        
    def __ge__(self, other):
        return self.key > other.key or self.key == other.key
        
    def __str__(self):
        return "Assoc({0}, {1})".format(self.key, self.value)

    
class DictList:
    def __init__(self):
        self.elems = []        

    def is_empty(self):
        return not self.elems
    
    def num(self):
        return len(self.elems)
    
    def search(self, key):
        for k, v in self.elems:
            if k == key:
                return v
        return None
        
    def insert(self, key, value):        
        for i in range(len(self.elems)):
            if self.elems[i][0] == key:
                self.elems[i] = (key, value)
                return
        self.elems.append((key, value))
        
    def delete(self, key):
        index = -1
        for i in range(len(self.elems)):
            if self.elems[i][0] == key:
                index = i
                break
        if index > 0:
            self.elems.pop(index)
            
    def keys(self):
        for k, v in self.elems:
            yield k
            
    def values(self):
        for k, v in self.elems:
            yield v
            
    def show(self):
        for x in self.elems:
            print(x)
        
        
class OrderDictList(DictList):
    
    def search(self, key):
        found, index = self._find(key)
        if found:
            return self.elems[index].value
            
    def insert(self, key, value):
        found, index = self._find(key)
        if found:
            self.elems[index] = Assoc(key, value)
        else:
            self.elems.insert(index, Assoc(key, value))
            
    def delete(self, key):
        found, index = self._find(key)
        if found:
            self.elems.pop(index)        
        
        
    def _find(self, key):
        begin, end = 0, len(self.elems)-1
        
        while begin <= end:
            mid = (begin + end) //2
            
            if self.elems[mid].key == key:
                return True, mid
            elif self.elems[mid].key > key:
                end = mid - 1
            else:
                begin = mid + 1
        return False, begin
        
                
        
        
        
    
if __name__ == "__main__":
    # d = DictList()
    # d.insert(2, 2)
    # d.insert(1, 1)
    # d.insert(3, 3)
    # d.show()
    # print(d.is_empty())
    # print(d.num())
    
    # d.delete(3)
    # d.show()
    
    # for k in d.keys():
        # print(k)
        
    # for v in d.values():
        # print(v)
        
    od = OrderDictList()
    od.insert(1, 100)
    od.insert(2, 100)
    od.insert(3, 100)
    od.insert(8, 100)
    od.insert(9, 100)
    od.insert(4, 100)    
    od.show()
    print('*' * 10)
    od.insert(5, 1000)
    od.show()
    print('*' * 10)
    od.insert(3, 200)
    od.show()
    print('*' * 10)
    od.delete(1)
    od.delete(100)
    od.show()

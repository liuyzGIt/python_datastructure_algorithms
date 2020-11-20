    # * Set()
    # * is_empty()
    # * is_member(e)
    # * insert(e)
    # * delete(e)
    # * intersection(other)  求交集
    # * union(other)  求并集
    # * defferent(other) 求差集
    # * subset(other)    判断集合是否是其他集合的子集

class SetList:
    def __init__(self):
        self.elems = []
        
    def is_empty(self):
        return not self.elems
        
    def member(self, e):
        return True if self.binsearch(e) else False
    
    
    def num(self):
        return len(self.elems)
        
        
    def insert(self, e):
        if self.is_empty():
            self.elems.append(e)
        elif not self.binsearch(e):
            elems = self.elems
            low, high = 0, len(elems) - 1
            
            while low <= high:
                mid = low + (high-low) // 2
                if elems[mid] < e:
                    low = mid + 1
                else:
                    high = mid - 1
            self.elems.insert(low, e)
    
    def get(self, index):
        if self.is_empty():
            raise ValueError('Empty in get')
        if index >= self.num():
            raise ValueError('index is out of range in get')
        return self.elems[index]
        
        
    def delete(self, e):
        index = self.binsearch(e)
        if index:
            self.elems.pop(index)
        
    def intersection(self, other):
        i = j = 0
        r = []
        
        while i < self.num() and j < other.num():
            if self.get(i) > other.get(j):
                j += 1
            elif self.get(i) < other.get(j):
                i += 1
            else: 
                r.append(self.get(i))
                i += 1
                j += 1
        
        return r
        
        
    def union(self, other):
        pass
        # i = j = 0
        # r = []
        
        # while i < self.num() and j < other.num():
            # if self.get(i) > other.get(j):
                # r.append(other.get(j))
                # j += 1
            # elif self.get(i) < other.get(j):
                # r.append(self.get(i))
                # i += 1
            # else: 
                # r.append(self.get(i))
                # i += 1
                # j += 1
        # return r
    
    def different(self, other):
        pass
        # i = j = 0
        # r = []
        
        # while i < self.num() and j < other.num():
            # if self.get(i) > other.get(j):
                # # r.append(other.get(j))
                # j += 1
            # elif self.get(i) < other.get(j):
                # r.append(self.get(i))
                # i += 1
            # else: 
                # i += 1
                # j += 1
        
        # return r
    
    def binsearch(self, e):
        elems = self.elems
        low, high = 0, len(elems) - 1
        
        while low <= high:
            mid = low + (high-low) // 2
            
            if elems[mid] == e:
                return mid
            elif elems[mid] < e:
                low = mid + 1
            else:
                high = mid - 1
                
    def show(self):
        print(self.elems)
        


if __name__ == "__main__":
    # s = SetList()
    # s.insert(1)
    # s.insert(3)
    # s.insert(5)
    # s.insert(7)
    # s.insert(9)
    # s.show()
    
    # s2 =  SetList()
    # s2.insert(1)
    # s2.insert(3)
    # s2.insert(6)
    # s2.show()
    # print('*' * 10)
    # print(s.intersection(s2))
    # print(s.union(s2))
    # print(s.different(s2))
    
    # class A:
        # def __hash__(self):
            # return hash('abc')
            
    # class B:
        # pass
        
    # # a = A()
    # # a1 = A()
    # b = B()
    # b1 = B()
    
    # # print(hash(a))
    # # print(hash(a1))
    # print(hash(b))
    # print(hash(b1))
    
    

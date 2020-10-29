class PrioQueueError(ValueError):
    pass

class PrioQueue:
    """小顶堆"""
    def __init__(self, elist=[]):
        self.elems = list(elist)
        if self.elems:
            self.build_heap()
    
    def is_empty(self):
        return not self.elems
        
    def peek(self):
        if self.is_empty():
            raise PrioQueueError(" in peek")
        return self.elems[0]
        
    def enqueue(self, item):
        self.elems.append(None)
        self.shift_up(item, len(self.elems)-1)
        
    def shift_up(self, e, last):
        elems = self.elems        
        i, j = last, (last-1)//2
        while i>0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e    
    
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError(" in peek")
        e0 = self.elems[0]
        e = self.elems.pop()
        if len(self.elems) > 0:
            self.shift_down(e, 0, len(self.elems))
        return e0
    
    def shift_down(self, e, begin, end):
        elems = self.elems
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j*2+1
        elems[i] = e    
    
    def build_heap(self):
        end = len(self.elems)
        for i in range(end//2-1, -1, -1):
            self.shift_down(self.elems[i], i, end)
    
    def show(self):
        print(self.elems)
    
if __name__ == "__main__":
    pq = PrioQueue([100,86,48,95,2])
    print(pq.dequeue())
    pq.enqueue(1)
    print(pq.dequeue())
    pq.enqueue(2)
    print(pq.peek())
    
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.peek())
    

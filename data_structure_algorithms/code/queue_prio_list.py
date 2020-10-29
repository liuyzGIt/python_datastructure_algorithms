class PrioQueueError(ValueError):
    pass
    
    
class PrioQueue:
    """小的元素优先"""
    def __init__(self, elems):
        self.elems = list(elems)
        self.elems.sort(reverse=True)
    
    def is_empty(self):
        return not self.elems
    
    def enqueue(self, item):
        i = len(self.elems) -1
        
        while i >= 0:
            if self.elems[i] <= item:
                i -= 1
            else:
                break
        self.elems.insert(i+1, item)
        
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError(' Empty in dequeue')
        return self.elems.pop()
        
    def peek(self):
        if self.is_empty():
            raise PrioQueueError(' Empty in dequeue')
        return self.elems[-1]
    
    def show(self):
        print(self.elems)    
        
if __name__ == "__main__":
    pq = PrioQueue([1,54,8])
    
    pq.show()
    print(pq.dequeue())
    pq.enqueue(100)
    pq.show()
    pq.enqueue(2)
    pq.show()
    
    pq.dequeue()
    pq.show()
    pq.peek()
    pq.show()
    
    pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    
    

class Queue:
    def __init__(self):
        self.elems = []
        
    def is_empty(self):
        return not self.elems
        
    def enqueue(self, value):
        self.elems.append(value)
        
    def dequeue(self):
        if self.is_empty():
            raise ValueError("empty queue in dequeue")            
        return self.elems.pop(0)
        
    def peek(self):
        if self.is_empty():
            raise ValueError("empty queue in peek")            
        return self.elems[0]
    
    def show(self):
        print(self.elems)

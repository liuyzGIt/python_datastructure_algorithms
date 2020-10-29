class StackError(ValueError):
    pass
    
class SStack:
    def __init__(self):
        self.elems = []
    def is_empty(self):
        return not self.elems
    
    def push(self, data):
        self.elems.append(data)
    
    def pop(self):
        if self.is_empty():
            raise StackError('in pop')
        return self.elems.pop()
    
    def top(self):
        if self.is_empty():
            raise StackError('in top')
        return self.elems[-1]
        
    def __str__(self):
        return str(self.elems)
        

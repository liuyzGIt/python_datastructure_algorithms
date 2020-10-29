from stack import SStack


class BinTreeError(ValueError):
    pass


class BinTreeNode:
    def __init__(self, data, left=None, right= None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.data
    
    
class BinTree:
    def __init__(self):
        self._root = None
        
    def is_empty(self):
        return not self._root
        
    def left(self):
        if self.is_empty():
            raise BinTreeError(' in left')
        return self._root.left
        
    def right(self):
        if self.is_empty():
            raise BinTreeError('in right')
        return self._root.right
    
    def root(self):
        return self._root
        
    def set_root(self, node):
        self._root = node
        
    def set_left(self, node):
        if self.is_empty():
            raise BinTreeError('in set left')
        self._root.left = node
    
    def set_right(self, node):
        if self.is_empty():
            raise BinTreeError('in set right')
        self._root.right = node
    
    def pre_order(self):
        s = SStack()
        t = self._root
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()
        
    

def order_tree(t, process):
    if t is None:
        return    
    
    order_tree(t.left, process)    
    order_tree(t.right, process)
    process(t.data)


from queue import Queue
def level_order(t, proc):
    if t is None:
        return
    
    q = Queue()
    q.put(t)
    while not q.empty():
        node = q.get()
        if node.left:        
            q.put(node.left)
        if node.right:
            q.put(node.right)
        proc(node.data)


def pre_order(t, proc):
    if t is None:
        return
        
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:    # 沿左分支下行
            proc(t.data)        # 先根序处理跟数据
            s.push(t.right)     # 右分支入栈
            t = t.left          
        t = s.pop()             # 遇到空树，回溯
        
def mid_order(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        yield t.data
        t = t.right
        
        
def post_order(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left else t.right
        t = s.pop()
        yield t.data
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None
        
        


            
if __name__ == "__main__":
    r = BinTreeNode(1,
                    BinTreeNode(
                        2, 
                        BinTreeNode(4), 
                        # BinTreeNode(5)
                    ), 
                    BinTreeNode(
                        3, 
                        # BinTreeNode(6),
                        None, 
                        BinTreeNode(7)
                    ))
    bt = BinTree()
    bt.set_root(r)
    
    # for i in bt.pre_order():
        # print(i)
    
    # order_tree(bt.root(), lambda x: print(x))
    # level_order(bt.root(), lambda x: print(x))
    # pre_order(bt.root(), lambda x: print(x))
    # for i in mid_order(bt.root()):
        # print(i)
    for i in post_order(bt.root()):
        print(i)
    
    

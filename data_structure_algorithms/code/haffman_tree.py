from bintree import BinTreeNode
from queue_prio_heap import PrioQueue

class HTreeNode(BinTreeNode):
    def __lt__(self, other):
        return self.data < other.data
        
class HPrioQueue(PrioQueue):
    def size(self):
        return len(self.elems)
        

def build_huffman_tree(weights):
    if not weights:
        return
    
    q = HPrioQueue()
    for i in weights:
        q.enqueue(HTreeNode(i))
    
    while q.size() > 1:
        t1 = q.dequeue()
        t2 = q.dequeue()
        t = HTreeNode(t1.data+t2.data, t1, t2)
        q.enqueue(t)
    return q.dequeue()
    
if __name__ == "__main__":
    w = [2,3,7,10,4,2,5]
    t = build_huffman_tree(w)
    from bintree import BinTree
    
    bt = BinTree()
    bt.set_root(t)
    for i in bt.pre_order():
        print(i)

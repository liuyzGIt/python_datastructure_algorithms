class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('Argument for graph')
        self.mat = [i[:] for i in mat]
        
        self.unconn = unconn
        self.vnum = vnum
        
    def _invalid(self, v):
        return 0 > v or v >= self.vnum
    
    def is_empty(self):
        return not self.mat
        
    def vertex_num(self):
        return self.vnum
        
    def edge_num(self):
        return len([x for x in v for v in self.mat if x != self.unconn])
        
    def add_vertex(self, vertex):
        if len(vertex) != self.vnum+1:
            raise ValueError('argument for add_vertex')
        for i in range(self.vnum):
            self.mat[i].append(vertex[i])
        self.mat.append(vertex)
        self.vnum += 1
          
    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError('argument for add_edge')
        self.mat[vi][vj] = val
        
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError('argument for get_edge')
        return self.mat[vi][vj]
        
    def out_edge(self, v):
        if self._invalid(v):
            raise ValueError('argument for out_edge')
        return self._out_edge(self.mat[v], self.unconn)
        
    def degrees(self, v):
        if self._invalid(v):
            raise ValueError('argument for degrees')
        return len([x for x in self.mat[v] if x != self.unconn])
    
    @staticmethod
    def _out_edge(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges
        
    def __str__(self):
        return "\n" + ",\n".join(map(str, self.mat)) + "\n" \
        + "\n UnConnect:" + str(self.unconn)
    

class GraphAL(Graph):
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("argument for GraphAL")
        self.mat = [Graph._out_edge(i, unconn) for i in mat]
        self.vnum = vnum
        self.unconn = unconn
        
    def edge_num(self):
        return sum([len(v) for v in self.mat])
        
    def add_vertex(self, vertex):
        self.mat.append([])
        self.vnum += 1
        return self.vnum - 1
          
    def add_edge(self, vi, vj, val=1):
        if self.vnum <= 0:
            raise ValueError('cannot add edge to empty graph')
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError('argument for add_edge')
        row = self.mat[vi]
        is_contains = False
        for i in range(len(row)):
            if row[i][0] == vj:
                row[i] = (vj, val)
                is_contains = True
                break
        if not is_contains:
            row.append((vj, val))               
           
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError('argument for get_edge')
        row = self.mat[vi]
        for i, val in row:
            if i == vj:
                return val
        return self.unconn
                
    def out_edge(self, v):
        if self._invalid(v):
            raise ValueError('argument for out_edge')
        return self.mat[v]
        
    def degrees(self, v):
        if self._invalid(v):
            raise ValueError('argument for degrees')
        return len(self.mat[v])
    


if __name__ == "__main__":
    # g1 = Graph([
        # [0, 1, 1, 0],
        # [1, 0, 1, 0],
        # [1, 1, 0, 1],
        # [0, 0, 1, 0],
    # ])
    # print(g1)
    
    # g1.add_vertex([1, 1, 1, 1, 0])
    # print(g1)
    # g1.add_edge(0, 3)
    # print(g1)
    # print(g1.get_edge(1,3))
    # print(g1.out_edge(2))
    # print(g1.degrees(4))
    
    g1 = GraphAL([
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0],
    ])
    print(g1)
    
    g1.add_vertex([1, 1, 1, 1, 0])
    print(g1)
    g1.add_edge(0, 3)
    print(g1)
    print(g1.get_edge(1,3))
    print(g1.out_edge(2))
    print(g1.degrees(4))

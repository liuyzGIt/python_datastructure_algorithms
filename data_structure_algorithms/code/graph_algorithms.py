class GraphAL:
    def __init__(self, vertexs, mat, unconn):
        self.vertexs = vertexs
        self.vnum = len(vertexs)
        self.unconn = unconn
        self.mat = []
        if len(mat) != self.vnum:
            raise ValueError('arguments err in mat')
        for x in mat:
            if len(x) != self.vnum:
                raise ValueError('arguments err in mat')
            self.mat.append(GraphAL._out_edges(x, unconn))
            
    def vertex_num(self):
        return self.vnum
            
    def is_empty(self):
        return not self.mat
    
    def _invalid(self, i):
        return  i <0 or i >= self.vnum
        
    def add_vertex(self, v, edges):
        if len(edges) != self.vnum+1:
            raise ValueError('edges count error')
        for i in range(self.vnum):
            if edges[i] != self.unconn:
                self.mat[i].append(self.vnum, edges[i])
        self.mat.append([])
        for i in range(len(edges)):
            if edges[i] != self.unconn:
                self.mat[-1].append(i, edges[i])
        self.veretxs.append(v)
        self.vnum += 1
                
        
        
    def add_edge(self, vi, vj, weight):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError('vi or vj is invalid')
        row = self.mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                row[i] =  (vj, weight)
                return
            if row[i][0] > vj:
                break
            i += 1
        
        row.insert(i, (vj, weight))
    
        
    def get_vertex(self, v):
        if self._invalid(v):
            raise ValueError(str(v) + ' is not a valid vertex.')
        return self.vertexs[v]
        
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError('vi or vj is invalid')
        for i, val in self.mat[vi]:
            if i == vj:
                return val
        return self.unconn
        
    def out_edges(self, v):
        if self._invalid(v):
            raise ValueError(str(v) + ' is not a valid vertex.')
        return self.mat[v]
            
        
    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges
        
    def show(self):
        print(self.vertexs)
        for x in self.mat:
            print(x)
    

# DFS递归遍历
def DFS_recursion(graph, v, visited):
    visited[v] = 1
    print(graph.get_vertex(v))
    edges = graph.out_edges(v)
    for i, w in edges:
        if visited[i] == 0:
            v = i            
            DFS_recursion(graph, v, visited)


# DFS非递归遍历
from stack import SStack
def DFS(graph, v):
    visited = [0]*graph.vnum
    s = SStack()
    s.push(v)
    while not s.is_empty():
        v = s.pop()
        if visited[v] == 0:
            print(graph.get_vertex(v))
            visited[v] = 1
            outs = graph.out_edges(v)
            for out in outs:
                s.push(out[0])
    
    
# BFS遍历
from queue import Queue
def BFS(graph, v):
    visited = [0]*graph.vertex_num()
    q = Queue()
    q.enqueue(v)
    while not q.is_empty():
        v = q.dequeue()
        if visited[v] == 0:
            visited[v] = 1
            print(graph.get_vertex(v))
            edges = graph.out_edges(v)
            for e in edges:
                q.enqueue(e[0])    
   
# DFS生成树
def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum
    
    def dfs(graph, v):
        nonlocal span_forest
        
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)
                
    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
            
    return span_forest
            
    
# 克鲁斯卡尔算法
def Kruskal(graph):
    vnum = graph.vertex_num()   
    reps = [i for i in range(vnum)]         # 初始每个顶点的代表元是自己的下标
    mst, edges = [], []
        
    for i in range(vnum):                   # 将所有的边加入数组
        for v, w in graph.out_edges(i):
            edges.append((w, i, v))

    # 等价于 edges.sort(key=lambda x: x[0])
    edges.sort()                            # 将所有边排序
    
    for w, vi, vj in edges:        
        if reps[vi] != reps[vj]:            # 两个顶点的代表元不同，属于不同连通分量            
            mst.append(((vi, vj), w))       # 记录这条边，加入到生成树中
            if len(mst) == vnum -1:         # |V|=n-1,构造完成
                break            
            
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):           # 合并两个连通分量的代表元
                if reps[i] == orep:         # 使用其中一个的代表
                    reps[i] = rep

    return mst
        

# 普利姆算法
from queue_prio_list import PrioQueue
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None]*vnum
    cands = PrioQueue([(0, 0, 0)])
    
    count=0
    
    while count<vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue            
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))
    return mst


# 迪杰斯特拉算法
def Dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum 
    paths = [None] * vnum
    count = 0
    conds = PrioQueue([(0, 0, 0)])
    
    while count < vnum and not conds.is_empty():
        plen, u, vmin = conds.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                conds.enqueue((plen+w, vmin, v))
        count += 1
    return paths


# 最短路径的Floyd算法
def all_shortest_paths(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)]
            for i in range(vnum)]
            
    for i in a:
        print(i)
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)] for i in range(vnum)]
    # nvertex = [[-1 for j in range(vnum)] for i in range(vnum)]
    print('*'*100)
    for i in nvertex:
        print(i)
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if i !=j and k !=i and k != j:
                    if a[i][j] > a[i][k] + a[k][j]:
                        a[i][j] = a[i][k] + a[k][j]
                        nvertex[i][j] = nvertex[i][k]
                        # nvertex[i][j] = k
    return (a, nvertex)
    
def print_shortest_path(path, i, j):
    # if path[i][j] == -1:
    if path[i][j] == j:
        print(i, j)
    else:
        mid = path[i][j]
        print_shortest_path(path, i, mid)
        print_shortest_path(path, mid, j)
        
    
def topo_sort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0] * vnum, []
    zerov = -1
    
    for i in range(vnum):
        for v, w in graph.out_edges(i):
            indegree[v] +=1
            
    for v in range(vnum):
        if indegree[v] == 0:            
            indegree[v] = zerov
            zerov = v
    print(indegree)
    for n in range(vnum):
        if zerov == -1:
            return False
        print(zerov, indegree)
        vi = zerov
        zerov = indegree[vi]
        toposeq.append(vi)
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq
            

# * 从有向图中选择一个出度为0的顶点输出。
# * 删除选出的顶点，并删除指向该顶点的全部边。
# * 重复上述两步，直到剩余图中不存在出度为0的边为止。

def reverse_topo_sort(graph):
    vnum = graph.vertex_num()
    zerov = -1
    outdegrees, reverse_sort = [0] * vnum, []
    inedges = [[] for i in range(vnum)]
    
    
    for vi in range(vnum):
        edges = graph.out_edges(vi)
        outdegrees[vi] = len(edges)
        for v, w in edges:
            inedges[v].append(vi)
    
    for vi in range(vnum):
        if outdegrees[vi] == 0:
            outdegrees[vi] = zerov
            zerov = vi
            
    for i in range(vnum):
        if zerov == -1:
            return False
        reverse_sort.append(zerov)
        
        vi = zerov
        zerov = outdegrees[zerov]
                
        for v in inedges[vi]:
            outdegrees[v] -= 1
            if outdegrees[v] == 0:
                outdegrees[v] = zerov
                zerov = v
    
    return reverse_sort
        
            
def critical_paths(graph):   
    
    def topo_sort(g, vnum):
        indegree, toposeq = [0]*vnum, []        
        zerov = -1
        
        for vi in range(vnum):            
            for vj, w in g.out_edges(vi):               
                indegree[vj] +=1
        
        for i in range(vnum):
            if indegree[i] == 0:
                indegree[i] = zerov
                zerov = i
                
        for i in range(vnum):
            if zerov == -1:
                return False
            
            toposeq.append(zerov)            
            vi = zerov
            zerov = indegree[vi]            
            
            for vj, w in g.out_edges(vi):
                indegree[vj] -= 1
                if indegree[vj] == 0:
                    indegree[vj] = zerov
                    zerov = vj
        return toposeq
        
        
    def event_earliest_time(g, vnum, toposeq):
        ee = [0] * vnum
        for i in toposeq:           
            for j, w in g.out_edges(i):
                if ee[i] + w > ee[j]:
                    ee[j] = ee[i] + w
        return ee
        
    def event_latest_time(g, vnum, toposeq, eelast):        
        le = [eelast] * vnum
        for k in range(vnum-2, -1, -1):        
            i = toposeq[k]            
            for j, w in g.out_edges(i):
                if le[j] - w < le[i]:
                    le[i] = le[j] - w 
        return le
    
    def crt_path(vnum, g, ee, le):
        crt_actions = []
        
        for i in range(vnum):
            for j, w in g.out_edges(i):
                if ee[i] == le[j]-w: # 关键活动
                    crt_actions.append((i, j, ee[i]))
        return crt_actions
        
        
        
    vnum = graph.vertex_num()
    toposeq = topo_sort(graph, vnum)
    if not toposeq:  # 不存在拓扑序列
        return False  
    
    ee = event_earliest_time(graph, vnum, toposeq)
    le = event_latest_time(graph, vnum, toposeq,ee[-1])
    
    return crt_path(vnum, graph, ee, le)


Unconn = 0
Vertexs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

G7 = [
    [0, 0, 6, 3, 0, 0, 0],
    [11, 0, 4, 0, 0, 7, 0],
    [0, 3, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0, 0, 0]
]

G8 = [
    [0, 7, 7, 9, 0, 0, 0],
    [7, 0, 0, 3, 6, 0, 5],
    [7, 0, 0, 14, 0, 11, 0],
    [9, 3, 14, 0, 0, 0, 20],
    [0, 6, 0, 0, 0, 0, 8],
    [0, 0, 11, 0, 0, 0, 6],
    [0, 5, 0, 20, 8, 6, 0]
]

G9 = [
    [0, 5, 11, 5, 0, 0, 0],
    [5, 0, 0, 3, 9, 0, 7],
    [11, 0, 0, 7, 0, 6, 0],
    [5, 3, 7, 0, 0, 0, 20],
    [0, 9, 0, 0, 0, 0, 8],
    [0, 0, 6, 0, 0, 0, 8],
    [0, 7, 0, 20, 8, 8, 0]
]

G12 = [
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 8, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

G14 = [
    [0, 7, 13, 8, 0, 0,  0, 0,  0],
    [0, 0, 4,  0, 0, 14, 0, 0,  0],
    [0, 0, 0,  0, 5, 0,  8, 12, 0],
    [0, 0, 0,  0, 13,0,  0, 10, 0],
    [0, 0, 0,  0, 0, 7,  3, 0,  0],
    [0, 0, 0,  0, 0, 0,  0, 0,  6],
    [0, 0, 0,  0, 0, 0,  0, 0,  7],
    [0, 0, 0,  0, 0, 0,  0, 0,  8],
    [0, 0, 0,  0, 0, 0,  0, 0,  0],
]

# inf=float('inf')
# Unconn = inf
# G9 = [
    # [0,   5,   11,  5,   inf, inf, inf],
    # [5,   0,   inf, 3,   9,   inf, 7  ],
    # [11,  inf, 0,   7,   inf, 6,   inf],
    # [5,   3,   7,   0,   inf, inf, 20 ],
    # [inf, 9,   inf, inf, 0,   inf, 8  ],
    # [inf, inf, 6,   inf, inf, 0,   8  ],
    # [inf, 7,   inf, 20,  8,   8,   0  ]
# ]


if __name__ == "__main__":
    g7  = GraphAL(Vertexs, G7, Unconn)
    # g7.show()
    visited = [0]*g7.vertex_num()
    # DFS_recursion(g7, 0, visited)
    # BFS(g7, 0)
    # DFS(g7,0)
    # rs = DFS_span_forest(g7)
    # print(rs)
    
    
    
    g8  = GraphAL(Vertexs, G8, Unconn)
    visited = [0]*g8.vertex_num()
    # DFS_recursion(g8, 0, visited)
    # BFS(g8, 0)
    # DFS(g8,0)
    
    g9  = GraphAL(Vertexs, G9, Unconn)
    visited = [0]*g9.vertex_num()
    
    
    # print(Kruskal(g9))
    # print(Prim(g9))
    # print(Dijkstra_shortest_paths(g7, 0))
    # print(Dijkstra_shortest_paths(g8, 0))
    # print(Dijkstra_shortest_paths(g9, 0))
    
    # a, p = all_shortest_paths(g9)   
    # print_shortest_path(p, 0, 5)
    vertexs = ['c1', 'c2', 'c3', 'c4', 'c5','c6','c7','c8','c9','c10',]
    g12  = GraphAL(vertexs, G12, Unconn)
    
    # print(topo_sort(g12))
    # print(reverse_topo_sort(g12))
    
    vertexs = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5','v6','v7','v8']
    g14  = GraphAL(vertexs, G14, Unconn)
    print(critical_paths(g14))

from  queue import Queue  
Graph={'A':['B','D','E','F'],'D':['A'],'B':['A','F','C'],'F':['B','A'],'C':['B'],'E':['A']}
print("given graph is:")
print(Graph) 

def bfs(input_graph,source):
    Q=Queue()
    visited_vertices=list()
    Q.put(source)
    visited_vertices.append(source)
    while not Q.empty():
        vertex=Q.get()
        print(vertex,end=" ")
        for i in input_graph[vertex]:
            if i not in visited_vertices:
                Q.put(i)
                visited_vertices.append(i)
print("BFE traversal of graph with source is :")
bfs(Graph,"A")

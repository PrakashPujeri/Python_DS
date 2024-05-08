Graph={'A':['B','D','E','F'],'D':['A'],'B':['A','F','C'],'F':['B','A'],'C':['B'],'E':['A']}
print("given graph is:")
print(Graph)

def dfs_traversal(input_graph,source):
    stack=list()
    visited_list=list()
    stack.append(source)
    visited_list.append(source)
    while stack:
        vertex=stack.pop()
        print(vertex,end=" ")
        for i in input_graph[vertex]:
            if i  in visited_list:
                stack.append(i)
                visited_list.append(i)
print("DFS traversal of graph with source A is:")
dfs_traversal(Graph,"A")
       
from igraph import Graph

def dfs(graph,vertex,visited,dfs_traversal):
    visited[vertex]=True
    dfs_traversal.append(vertex)
    for neighbor in graph.neighbors(vertex):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, dfs_traversal)
            
graph = Graph()
graph.add_vertices(5)
graph.add_edges([(0,1),(0,2),(1,3),(2,3),(3,4)])

visited = [False] * graph.vcount()

dfs_traversal=[]
dfs(graph, 0, visited,dfs_traversal)
print("DFS Traversal:", dfs_traversal)
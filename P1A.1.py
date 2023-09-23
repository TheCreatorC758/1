from igraph import Graph

def bfs(graph,vertex):
    queue=[vertex]
    visited=[False]*graph.vcount()
    visited[vertex]=True

    while queue:
        current_vertex=queue.pop(0)
        print(current_vertex,end=" ")
        for neighbor in graph.neighbors(current_vertex):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True

graph = Graph()
graph.add_vertices(5)
graph.add_edges([(0,1),(0,2),(1,3),(2,3),(3,4)])
print("BFS Traversal:",end=" ")
bfs(graph,0)
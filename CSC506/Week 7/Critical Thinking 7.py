import heapq
import numpy as np
class Graph:
    def __init__(self, V: int):
        self.V = V
        self.adj = [[] for _ in range(V)]

    #Add edge to adjacency list
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    #Dijkstras shortest path algorihtm
    def Dijkstras(self, src: int):
        
        #Array size of the graph set to infinity
        dist = [np.inf] * self.V

        #Set initial distance value to 0
        dist[src] = 0

        pq = []
        #Push initial element
        heapq.heappush(pq, (0, src))

        while pq:

            value, cur_val_ind = heapq.heappop(pq)

            for val_ind, val_weight in self.adj[cur_val_ind]:

                if dist[val_ind] > dist[cur_val_ind] + val_weight:

                    dist[val_ind] = dist[cur_val_ind] + val_weight

                    heapq.heappush(pq, (dist[val_ind], val_ind))
        return dist
if __name__ == "__main__":
    V = 8
    g = Graph(V)
    g.addEdge(0, 1, 1)
    g.addEdge(0, 7, 3)
    g.addEdge(1, 2, 5)
    g.addEdge(1, 7, 13)
    g.addEdge(2, 3, 12)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 5, 2)
    g.addEdge(5, 6, 9)
    g.addEdge(6, 7, 4)
    g.addEdge(6, 7, 7)

    dist = g.Dijkstras(3)
    print("Fourth vertex to other verticies: " +  str(dist))

    dist = g.Dijkstras(0)
    print("First vertex to other verticies: " +  str(dist))
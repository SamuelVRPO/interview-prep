import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def add(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
    
    def update(self, item, new_priority):
        for i, (p, it) in enumerate(self.queue):
            if it == item:
                self.queue[i] = (new_priority, item)
                heapq.heapify(self.queue)
                break
    
    def pop(self):
        return heapq.heappop(self.queue)[1]

class Graph:
    def __init__(self, vertices: list[str], edges: dict):
        self.vertices = vertices
        self.edges = edges


def djikstra(graph: Graph, source: str):
    dist = {}
    prev = {}
    Q = PriorityQueue()
    for v in graph.vertices:
            dist[v] = 0 if v == source else float('inf')
            prev[v] = None
            Q.add(v, dist[v])


    while len(Q.queue) > 0:
        u = Q.pop()
        
        for p, v in Q.queue:
            if graph.edges.get((u, v)) != None:
                alt = dist[u] + graph.edges[(u, v)]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    Q.update(v, dist[v])
        
    return dist, prev
    


v = ['med', 'bog', 'cal', 'bar', 'ctg', 'let']
e = {
    ('med', 'bog'): 600,
    ('med', 'cal'): 500,
    ('med', 'bar'): 800,
    ('bog', 'med'): 600,
    ('bog', 'cal'): 700,
    ('bog', 'let'): 1000,
    ('cal', 'med'): 500,
    ('cal', 'bog'): 700,
    ('bar', 'med'): 800,
    ('bar', 'ctg'): 50,
    ('ctg', 'bar'): 50,
    ('let', 'bog'): 1000,
}

cities = Graph(v, e)

dist, prev = djikstra(cities, 'cal')
print(dist)
print(prev)

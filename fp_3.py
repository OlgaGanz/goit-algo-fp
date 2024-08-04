import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random as rnd


rnd.seed(1234)
G = nx.Graph()
G.add_edge(1, 2, weight = rnd.randrange(1,7))
G.add_edge(1, 3, weight = rnd.randrange(1,7))
G.add_edge(2, 3, weight = rnd.randrange(1,7))
G.add_edge(2, 4, weight = rnd.randrange(1,7))
G.add_edge(2, 5, weight = rnd.randrange(1,7))
G.add_edge(3, 6, weight = rnd.randrange(1,7))
G.add_edge(5, 2, weight = rnd.randrange(1,7))
G.add_edge(5, 4, weight = rnd.randrange(1,7))
G.add_edge(5, 6, weight = rnd.randrange(1,7))

def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return shortest_paths

print(G.nodes)
target = 6              # start node (1:6)
print("Find shortest path from:")
shortest_paths = dijkstra(G, target)
for key in shortest_paths.keys():
    print(f"{target} to {key} = {shortest_paths.get(key)}")

pos = nx.spring_layout(G)
color_map = []
for node in G:
    if node == target:
        color_map.append("Green")
    else: 
        color_map.append("LightGrey")

nx.draw_networkx_nodes(G, pos, node_size=700, node_color=color_map)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()

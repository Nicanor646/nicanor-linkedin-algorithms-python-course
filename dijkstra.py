import os

# test_graph ={
#     'U': { 'V': 6, 'W': 7},
#     'V': {'U': 6, 'X': 10},
#     'W': {'U': 7, 'X': 1},
#     'X': {'V': 10, 'W': 1},
# }
# source_node = 'U'
# target_node = 'X'

test_graph ={
    'A': { 'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5},
}
source_node = 'A'
target_node = 'C'

num_nodes = len(test_graph)
visited = []
unvisited = [idx for idx in test_graph.keys()]
distances = { k: float('inf') for k in test_graph.keys()}
full_path =  { k: None for k in test_graph.keys()}



distances[source_node] = 0
current_node = source_node

while unvisited:
    for u in unvisited:
        if u in test_graph[current_node]:
            if test_graph[current_node][u] + test_graph[current_node][u] < distances[u]:
                distances[u] = distances[current_node] + test_graph[current_node][u]
                full_path[u] = current_node

    unvisited.remove(current_node)
    visited.append(current_node)
    min_vertex_distance = float('inf')
    for u in unvisited:
        if distances[u] < min_vertex_distance:
            min_vertex_distance = distances[u]
            min_vertex_node = u
    current_node = min_vertex_node
print(distances)
print(full_path)

path = target_node
current_node = target_node
if full_path[current_node] or current_node == source_node:
    while current_node != source_node:
        path = f"{full_path[current_node]} -> {path}"
        current_node = full_path[current_node]
    print(f"The shortest path is {path} with a distance of {distances[target_node]}")
    
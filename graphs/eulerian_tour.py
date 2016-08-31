def get_neighbors(graph, node):
  neighbors = []

  for edge in graph:
    if edge[0] == node:
      neighbors.append((edge[1], edge))
    if edge[1] == node:
      neighbors.append((edge[0], edge))

  return neighbors

def eulerian_traversal(graph, head, path=[], depth=0):
  neighbors = get_neighbors(graph, head)

  if graph == None or len(graph) == 0:
    # Base case: No more paths left to traverse, so we've found an Eulerian tour
    return [path]

  found_paths = []
  for node, edge in neighbors:
    found_path = eulerian_traversal(set(graph) - {edge}, node, path + [node], depth + 1)

    if found_path:
      found_paths += found_path

  return found_paths

def find_eulerian_tour(graph):
  head = graph[0][0]

  return eulerian_traversal(graph, head, [head])

graph = [(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

print("All possible tours of graph:")
for tour in find_eulerian_tour(graph):
  print(tour)


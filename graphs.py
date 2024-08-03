#Adjacency matrix
# def create_adj_matrix():
#     n = int(input("Enter the number of vertices: "))

#     adj_matrix = [[0] * n for _ in range(n)]

#     e = int(input("Enter the number of edges: "))

#     print("Enter the edges (u v):")
#     for _ in range(e):
#         u, v = map(int, input().split())
#         adj_matrix[u][v] = 1
#         adj_matrix[v][u] = 1  

#     print("Adjacency Matrix:")
#     for row in adj_matrix:
#         print(row)

# create_adj_matrix()

#Adjacency list
# def create_adj_list():
#     # Get number of vertices
#     n = int(input("Enter the number of vertices: "))

#     # Initialize the adjacency list
#     adj_list = {i: [] for i in range(n)}

#     # Get number of edges
#     e = int(input("Enter the number of edges: "))

#     # Get edges from user input
#     print("Enter the edges (u v) :")
#     for _ in range(e):
#         u, v = map(int, input().split())
#         adj_list[u].append(v)
#         adj_list[v].append(u) 

#     # Print the adjacency list
#     print("Adjacency List:")
#     for key in adj_list:
#         print(f"{key}: {adj_list[key]}")

# # Call the function
# create_adj_list()

#BFS
# from collections import deque
# def create_adj_list():
#     n = 5
#     adj_list = {i: [] for i in range(1, n + 1)}
#     edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
#     for u, v in edges:
#         adj_list[u].append(v)
#         adj_list[v].append(u) 
#     return adj_list

# def bfs(adj_list, start_vertex):
#     visited = set()
#     queue = deque([start_vertex])
#     visited.add(start_vertex)

#     bfs_order = []
#     while queue:
#         vertex = queue.popleft()
#         bfs_order.append(vertex)

#         for neighbor in adj_list[vertex]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)

#     return bfs_order

# def main():
#     adj_list = create_adj_list()
#     start_vertex = 1
#     bfs_result = bfs(adj_list, start_vertex)
#     print("BFS Traversal Order:", bfs_result)

# if __name__ == "__main__":
#     main()

#DFS
# def create_adj_list():
#     n = 5
#     adj_list = {i: [] for i in range(1, n + 1)}
#     edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
#     for u, v in edges:
#         adj_list[u].append(v)
#         adj_list[v].append(u)  

#     return adj_list

# def dfs(adj_list, start_vertex, visited, dfs_order):
#     visited.add(start_vertex)
#     dfs_order.append(start_vertex)
#     for neighbor in adj_list[start_vertex]:
#         if neighbor not in visited:
#             dfs(adj_list, neighbor, visited, dfs_order)

# def main():
#     adj_list = create_adj_list()
#     start_vertex = 1  
#     visited = set()
#     dfs_order = []

#     dfs(adj_list, start_vertex, visited, dfs_order)
#     print("DFS Traversal Order:", dfs_order)

# if __name__ == "__main__":
#     main()

#Topological Sort
# from collections import deque, defaultdict
# def create_adj_list():
#     n = 6
#     adj_list = defaultdict(list)
#     in_degree = {i: 0 for i in range(n)}
#     edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
#     for u, v in edges:
#         adj_list[u].append(v)
#         in_degree[v] += 1

#     return adj_list, in_degree

# def topological_sort(adj_list, in_degree):
#     queue = deque([v for v in in_degree if in_degree[v] == 0])
    
#     top_order = []

#     while queue:
#         u = queue.popleft()
#         top_order.append(u)

#         for v in adj_list[u]:
#             in_degree[v] -= 1
#             if in_degree[v] == 0:
#                 queue.append(v)

#     return top_order

# def main():
#     adj_list, in_degree = create_adj_list()
#     top_order = topological_sort(adj_list, in_degree)
#     print("Topological Sort Order:", top_order)

# if __name__ == "__main__":
#     main()

#Cycle Detection in Undirected Graph
# from collections import defaultdict
# def create_adj_list():
#     n = 6
#     adj_list = defaultdict(list)
#     edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5)]
#     for u, v in edges:
#         adj_list[u].append(v)
#         adj_list[v].append(u) 

#     return adj_list

# def dfs(v, parent, visited, adj_list):
#     visited.add(v)

#     for neighbor in adj_list[v]:
#         if neighbor not in visited:
#             if dfs(neighbor, v, visited, adj_list):
#                 return True
#         elif neighbor != parent:
#             return True
#     return False

# def has_cycle(adj_list):
#     visited = set()
#     for vertex in adj_list:
#         if vertex not in visited:
#             if dfs(vertex, -1, visited, adj_list):
#                 return True

#     return False

# def main():
#     adj_list = create_adj_list()
#     if has_cycle(adj_list):
#         print("The graph contains a cycle.")
#     else:
#         print("The graph does not contain a cycle.")

# if __name__ == "__main__":
#     main()

#Cycle Detection in Directed Graph
# from collections import defaultdict
# def create_adj_list():
#     # Number of vertices
#     n = 6

#     # Initialize the adjacency list
#     adj_list = defaultdict(list)

#     # List of edges (each edge is a tuple of two vertices)
#     edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5)]

#     # Update the adjacency list
#     for u, v in edges:
#         adj_list[u].append(v)

#     return adj_list

# # Function to perform DFS and detect cycles
# def dfs(v, visited, rec_stack, adj_list):
#     # Mark the current node as visiting
#     visited[v] = True
#     rec_stack[v] = True

#     # Recur for all vertices adjacent to this vertex
#     for neighbor in adj_list[v]:
#         if not visited[neighbor]:
#             if dfs(neighbor, visited, rec_stack, adj_list):
#                 return True
#         elif rec_stack[neighbor]:
#             return True

#     # Unmark the current node from the recursion stack
#     rec_stack[v] = False
#     return False

# # Function to check for cycles in a directed graph
# def has_cycle(adj_list):
#     visited = [False] * len(adj_list)
#     rec_stack = [False] * len(adj_list)

#     # Check each component of the graph
#     for vertex in adj_list:
#         if not visited[vertex]:
#             if dfs(vertex, visited, rec_stack, adj_list):
#                 return True

#     return False

# # Main function
# def main():
#     adj_list = create_adj_list()
#     if has_cycle(adj_list):
#         print("The graph contains a cycle.")
#     else:
#         print("The graph does not contain a cycle.")

# # Call the main function
# if __name__ == "__main__":
#     main()

#find the num of connected components in graph and its size
# from collections import defaultdict
# # Function to create an adjacency list from hard-coded edges
# def create_adj_list():
#     # Number of vertices
#     n = 5

#     # Initialize the adjacency list
#     adj_list = defaultdict(list)

#     # List of edges (each edge is a tuple of two vertices)
#     edges = [(0, 1), (1, 2), (3, 4)]

#     # Update the adjacency list
#     for u, v in edges:
#         adj_list[u].append(v)
#         adj_list[v].append(u)

#     return adj_list, n

# # Function to perform DFS and track the size of connected components
# def dfs(v, visited, adj_list):
#     stack = [v]
#     size = 0
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             size += 1
#             for neighbor in adj_list[node]:
#                 if not visited[neighbor]:
#                     stack.append(neighbor)
#     return size

# # Function to find the number of connected components and their sizes
# def find_components(adj_list, n):
#     visited = [False] * n
#     component_sizes = []

#     for vertex in range(n):
#         if not visited[vertex]:
#             size = dfs(vertex, visited, adj_list)
#             component_sizes.append(size)

#     return len(component_sizes), component_sizes

# # Main function
# def main():
#     adj_list, n = create_adj_list()
#     num_components, component_sizes = find_components(adj_list, n)
#     print("Number of connected components:", num_components)
#     print("Sizes of connected components:", component_sizes)
#     #No. ways to get 2 friend that are unrelated
#     ans = 0
#     for i in component_sizes:
#         ans += i * (n-i)
#     print("Total 2 unrealted friends ways: ", ans//2)

# # Call the main function
# if __name__ == "__main__":
#     main()

#Bipartite Graph
# from collections import defaultdict, deque

# def create_adj_list():
#     n = 6
#     adj_list = defaultdict(list)
#     edges = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 5)]
#     for u, v in edges:
#         adj_list[u].append(v)
#         adj_list[v].append(u)
#     return adj_list, n

# def is_bipartite(adj_list, start_vertex, colorlist):
#     queue = deque([start_vertex])
#     colorlist[start_vertex] = True  # Start coloring with True (or any arbitrary color)

#     while queue:
#         vertex = queue.popleft()
#         current_color = colorlist[vertex]
#         for neighbor in adj_list[vertex]:
#             if neighbor not in colorlist:
#                 colorlist[neighbor] = not current_color  # Flip color for the neighbor
#                 queue.append(neighbor)
#             elif colorlist[neighbor] == current_color:
#                 return False  # A conflict in coloring, hence not bipartite

#     return True

# def main():
#     adj_list, n = create_adj_list()
#     colorlist = {}
#     start_vertex = 0

#     if is_bipartite(adj_list, start_vertex, colorlist):
#         print("Bipartite")
#     else:
#         print("Not bipartite")

# if __name__ == "__main__":
#     main()

#Cycle Detection in Undirected Graph using DSU
# n =10
# parent = list(range(n))
# sz = list(range(n))
# def make_set(v):
#     parent[v] = v
#     sz[v] = 1

# def find_set(v):
#     if v != parent[v]:
#         parent[v] = find_set(parent[v])
#     return parent[v]

# def union_set(a, b):
#     a = find_set(a)
#     b = find_set(b)
#     if(a != b):
#         if sz[a] < sz[b]:
#             a, b = b, a
#         parent[b] = a
#         sz[a] += sz[b]

# for i in range(n):
#     make_set(i)

# cycle = False
# edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5)]
# for i in edges:
#     u = i[0]
#     v = i[1]
#     x = find_set(u)
#     y = find_set(v)
#     if x == y:
#         cycle = True
#     else:
#         union_set(x, y)
# if cycle:
#     print("Cycle")
# else:
#     print("No cycle")

#Kruskal Algorithm - Minimum Spanning Tree
# n =10
# parent = list(range(n))
# sz = list(range(n))
# def make_set(v):
#     parent[v] = v
#     sz[v] = 1

# def find_set(v):
#     if v != parent[v]:
#         parent[v] = find_set(parent[v])
#     return parent[v]

# def union_set(a, b):
#     a = find_set(a)
#     b = find_set(b)
#     if(a != b):
#         if sz[a] < sz[b]:
#             a, b = b, a
#         parent[b] = a
#         sz[a] += sz[b]

# for i in range(n):
#     make_set(i)

# cost = 0
# edges = [(4, 0, 1), (2, 1, 2), (9, 2, 3), (6, 3, 0), (1, 4, 5)]
# edges.sort()
# for i in edges:
#     w = i[0]
#     u = i[1]
#     v = i[2]
#     x = find_set(u)
#     y = find_set(v)
#     if x == y:
#         continue
#     else:
#         print(x, "->", y)
#         cost += w
#         union_set(x, y)

# print(cost)

#Prims Algorithm - Minimum Spanning Tree
# import heapq
# def prim(n, edges):
#     adj = [[] for _ in range(n)]
#     for u, v, weight in edges:
#         adj[u].append((weight, v))
#         adj[v].append((weight, u))

#     # Initialize variables
#     total_cost = 0
#     mst = []
#     visited = [False] * n
#     min_heap = [(0, 0)]  # (weight, vertex), start with vertex 0

#     while min_heap:
#         weight, u = heapq.heappop(min_heap)
#         if visited[u]:
#             continue
#         visited[u] = True
#         total_cost += weight

#         for next_weight, v in adj[u]:
#             if not visited[v]:
#                 heapq.heappush(min_heap, (next_weight, v))
#                 mst.append((u, v, next_weight))

#     return mst, total_cost

# # Example usage
# n = 5  # Number of vertices
# edges = [
#     (0, 1, 10),
#     (0, 2, 6),
#     (0, 3, 5),
#     (1, 3, 15),
#     (2, 3, 4)
# ]

# mst, cost = prim(n, edges)
# print("Minimum Spanning Tree:", mst)
# print("Total cost:", cost)

#Dijkstra Algorithm
# import heapq

# def dijkstra(n, edges, start):
#     adj = [[] for _ in range(n)]
#     for u, v, weight in edges:
#         adj[u].append((weight, v))
#         adj[v].append((weight, u))  # If the graph is undirected

#     dist = [float('inf')] * n
#     dist[start] = 0
#     min_heap = [(0, start)]  # (distance, vertex)

#     while min_heap:
#         current_dist, u = heapq.heappop(min_heap)
#         if current_dist > dist[u]:
#             continue
        
#         for weight, v in adj[u]:
#             distance = current_dist + weight
#             if distance < dist[v]:
#                 dist[v] = distance
#                 heapq.heappush(min_heap, (distance, v))

#     return dist

# # Example usage
# n = 5  # Number of vertices
# edges = [
#     (0, 1, 10),
#     (0, 2, 6),
#     (0, 3, 5),
#     (1, 3, 15),
#     (2, 3, 4)
# ]
# start = 0

# distances = dijkstra(n, edges, start)
# print("Shortest distances from vertex", start, ":", distances)

#Bellman Ford
# def bellman_ford(n, edges, start):
#     # Initialize distances from start to all other vertices as infinity
#     dist = [float('inf')] * n
#     dist[start] = 0

#     # Relax edges up to n-1 times
#     for _ in range(n - 1):
#         for u, v, weight in edges:
#             if dist[u] != float('inf') and dist[u] + weight < dist[v]:
#                 dist[v] = dist[u] + weight

#     # Check for negative weight cycles
#     for u, v, weight in edges:
#         if dist[u] != float('inf') and dist[u] + weight < dist[v]:
#             print("Graph contains negative weight cycle")
#             return None

#     return dist

# # Example usage
# n = 5  # Number of vertices
# edges = [
#     (0, 1, -1),
#     (0, 2, 4),
#     (1, 2, 3),
#     (1, 3, 2),
#     (1, 4, 2),
#     (3, 2, 5),
#     (3, 1, 1),
#     (4, 3, -3)
# ]
# start = 0

# distances = bellman_ford(n, edges, start)
# if distances:
#     print("Shortest distances from vertex", start, ":", distances)

#Floyd Warshall
# def floyd_warshall(n, edges):
#     # Initialize the distance matrix with infinity
#     dist = [[float('inf')] * n for _ in range(n)]
    
#     # Distance from a vertex to itself is always 0
#     for i in range(n):
#         dist[i][i] = 0

#     # Initialize distances based on input edges
#     for u, v, weight in edges:
#         dist[u][v] = weight
#         #If the graph is undirected, uncomment the next line
#         #dist[v][u] = weight

#     # Floyd-Warshall algorithm
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if dist[i][j] > dist[i][k] + dist[k][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]

#     return dist

# # Example usage
# n = 4  # Number of vertices
# edges = [
#     (0, 1, 5),
#     (0, 3, 10),
#     (1, 2, 3),
#     (2, 3, 1)
# ]

# distances = floyd_warshall(n, edges)
# print("Shortest distances between every pair of vertices:")
# for row in distances:
#     print(row)

#Snake and Ladder
#from collections import deque

# def shortest_path_snakes_and_ladders(snakes, ladders):
#     # Board representation
#     board = list(range(101))  # Create a board from 0 to 100
#     for start, end in ladders:
#         board[start] = end
#     for start, end in snakes:
#         board[start] = end

#     # BFS initialization
#     queue = deque([1])  # Start from cell 1
#     visited = [False] * 101
#     distance = [float('inf')] * 101
#     visited[1] = True
#     distance[1] = 0

#     while queue:
#         current = queue.popleft()
        
#         # Check all possible dice rolls
#         for dice in range(1, 7):
#             next_cell = current + dice
#             if next_cell <= 100:
#                 next_cell = board[next_cell]  # Move according to snakes or ladders
                
#                 if not visited[next_cell]:
#                     visited[next_cell] = True
#                     distance[next_cell] = distance[current] + 1
#                     queue.append(next_cell)
                    
#                     if next_cell == 100:
#                         return distance[next_cell]  # Return the shortest path length

#     return -1  # If cell 100 is not reachable

# # Example usage
# snakes = [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)]
# ladders = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100), (85, 97)]

# shortest_path = shortest_path_snakes_and_ladders(snakes, ladders)
# if shortest_path != -1:
#     print(f"The shortest path to reach the end is {shortest_path} moves.")
# else:
#     print("The end is not reachable.")

#Surrounded regions
# def solve(board):
#     if not board:
#         return
    
#     rows, cols = len(board), len(board[0])
    
#     def dfs(r, c):
#         if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
#             return
#         board[r][c] = 'E'  # Temporarily mark this cell as 'E' (escaped)
#         # Explore all four directions
#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)
    
#     # Step 1: Run DFS from the boundary cells
#     for r in range(rows):
#         dfs(r, 0)
#         dfs(r, cols - 1)
#     for c in range(cols):
#         dfs(0, c)
#         dfs(rows - 1, c)
    
#     # Step 2: Convert all 'O' to 'X' (surrounded regions)
#     for r in range(rows):
#         for c in range(cols):
#             if board[r][c] == 'O':
#                 board[r][c] = 'X'
#             elif board[r][c] == 'E':
#                 board[r][c] = 'O'

# # Example usage
# board = [
#     ['X', 'X', 'X', 'X'],
#     ['X', 'O', 'O', 'X'],
#     ['X', 'X', 'O', 'X'],
#     ['X', 'O', 'X', 'X']
# ]

# solve(board)
# for row in board:
#     print(row)
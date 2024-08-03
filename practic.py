#You are given a weighted graph G that contains N nodes and M edges. Each edge has weight(w) associated to it. You are given Q queries of the following type:
#-> x y W. Find if there exists a path in G between nodes x and y such that the weight of each edge in the path is at most W. If such a path exists print 1, 
# otherwise print 0.

# from collections import defaultdict
# edges = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 1, 6), (4, 3, 2)]
# n = 5
# queries = [
#     (0, 3, 3),  # Should return 0
#     (0, 3, 4),  # Should return 1
#     (4, 0, 3)   # Should return 0
# ]
# def build_graph(edges):
#     adj = defaultdict(list)
#     for u, v, w in edges:
#         adj[u].append((v, w))
#         adj[v].append((u, w))
#     return adj

# def dfs(adj, start, end, max_weight, visited):
#     if start == end:
#         return True
    
#     visited[start] = True
    
#     for neighbor, weight in adj[start]:
#         if not visited[neighbor] and weight <= max_weight:
#             if dfs(adj, neighbor, end, max_weight, visited):
#                 return True
    
#     return False

# def check_path(adj, x, y, W):
#     visited = [False] * len(adj)
#     return 1 if dfs(adj, x, y, W, visited) else 0

# adj = build_graph(edges)
# for x, y, W in queries:
#     print(check_path(adj, x, y, W))

# from collections import defaultdict

# def build_graph(edges):
#     adj = defaultdict(list)
#     for u, v, w in edges:
#         adj[u].append((v, w))
#         adj[v].append((u, w))
#     return adj

# def dfs(adj, node, W, visited, current_max):
#     if current_max >= W:
#         return True
    
#     visited[node] = True
    
#     for neighbor, weight in adj[node]:
#         if not visited[neighbor]:
#             if dfs(adj, neighbor, W, visited.copy(), current_max+weight):
#                 return True
    
#     return False

# def check_weight(adj, W):
#     n = len(adj)
    
#     for start in range(n):
#         visited = [False] * n
#         if dfs(adj, start, W, visited, 0):
#             return 1
    
#     return 0

# # Example usage
# edges = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 6), (4, 2, 2)]
# adj = build_graph(edges)

# # Example queries
# queries = [2, 3, 4, 5, 13, 20]

# for W in queries:
#     print(f"W = {W}: {check_weight(adj, W)}")

#Problem :Given a tree having nodes with value 0 and 1. write a function to return the number of islands ?
#Follow up: I've to return all distinct size of island. E.g if there are 3 island of size 10 and 5 island of size 2 then ans would be 2.

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def count_islands(root):
#     global ans, count
    
#     if not root:
#         return
    
#     if root.data == 1:
#         count += 1
#     if root.data == 0:
#         if count > 0:
#             ans.append(count)
#         count = 0
    
#     count_islands(root.left)
#     count_islands(root.right)

# # Create the tree
# root = TreeNode(1)
# root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(0)
# root.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)

# ans = []
# count = 0

# count_islands(root)

# # Don't forget to append the last count if it's non-zero
# if count > 0:
#     ans.append(count)

# print(f"Islands: {ans}")
# print(f"Number of islands: {len(ans)}")

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def count_islands(root):
#     def dfs(node, current_island):
#         if not node:
#             return [], current_island

#         if node.data == 1:
#             current_island += 1
#         else:  # node.data == 0
#             if current_island > 0:
#                 return [current_island], 0
#             else:
#                 return [], 0

#         left_islands, left_current = dfs(node.left, current_island)
#         right_islands, right_current = dfs(node.right, left_current)

#         return left_islands + right_islands, right_current

#     islands, last_island = dfs(root, 0)
#     if last_island > 0:
#         islands.append(last_island)

#     return islands

# # Create the tree
# root = TreeNode(1)
# root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(0)
# root.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)

# # Count the islands
# islands = count_islands(root)
# print(f"Islands: {islands}")
# print(f"Number of islands: {len(islands)}")

# def count_monotonic_subarrays(N, M, arr):
#     count = 0
#     for i in range(N):
#         operations = 0
#         max_value = 0
#         for j in range(i, N):
#             if arr[j] < max_value:
#                 operations += max_value - arr[j]
#                 if operations > M:
#                     break
#             else:
#                 max_value = arr[j]
#             count += 1
#     return count

# # Read number of test cases
# T = int(input())

# for _ in range(T):
#     # Read N and M
#     N, M = map(int, input().split())
    
#     # Read the array
#     arr = list(map(int, input().split()))
    
#     # Calculate and print the result
#     result = count_monotonic_subarrays(N, M, arr)
#     print(result)

#First array is the numbers from 0 to n-1, e.g. a = [0, 1, 2, 3, 4].
#The second array is shuffled in a different order, e.g. b = [1, 3, 2, 4, 0].
# Apply the same shuffling from a to b to a third array test_data = ['cupcake', 'donut', 'eclair', 'froyo', 'gingerbread'].
# The result will be result = ['donut', 'froyo', 'eclair', 'gingerbread', 'cupcake'].
# from collections import defaultdict
# a = [0, 1, 2, 3, 4]
# b = [1, 3, 2, 4, 0]
# test_data = ['cupcake', 'donut', 'eclair', 'froyo', 'gingerbread']
# hmp = defaultdict(int)
# for idx, v in enumerate(b):
#     hmp[v] = idx

# n = max(a)
# ans = [0]*(n+1)
# for i in range(n+1):
#     ans[hmp[i]] = test_data[i]

# print(ans)
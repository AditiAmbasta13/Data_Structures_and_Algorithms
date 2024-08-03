#Create hast table
#from collections import defaultdict
# some_dict = defaultdict(int)
# some_dict[8] = 2
# print(some_dict[8])

#Hashing - Count frequency of elements
# def count_elements(elements):
#     count_dict = defaultdict(int)  # Default value for missing keys is 0
    
#     for element in elements:
#         count_dict[element] += 1
    
#     return count_dict

# # Example usage
# elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# count = count_elements(elements)
# print("Element counts:", dict(count))

#Hashing - Vertical Order Print
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def getVerticalOrder(root, hdis, m):
#     if not root:
#         return None
#     m[hdis].append(root.data)
#     getVerticalOrder(root.left, hdis-1, m)
#     getVerticalOrder(root.right, hdis+1, m)

# root = Node(10)
# root.left = Node(7)
# root.right = Node(4)
# root.left.left = Node(3)
# root.left.right = Node(11)
# root.right.left = Node(14)
# root.right.right = Node(6)

# m = defaultdict(list)
# hdis = 0

# getVerticalOrder(root, hdis, m)

# for key in sorted(m.keys()):
#     print(f"Vertical Distance {key}: {m[key]}")

# print(m)

#Hashing - Number of Subarrays with Sum Zero
# def count_subarrays_with_sum_zero(arr):
#     # Dictionary to store the cumulative sum frequencies
#     cumulative_sum_freq = defaultdict(int)
    
#     # Initialize the cumulative sum and count of subarrays
#     cumulative_sum = 0
#     count = 0
    
#     # Iterate through the array
#     for num in arr:
#         # Update the cumulative sum
#         cumulative_sum += num
        
#         # If the cumulative sum is zero, we found a subarray with sum zero
#         if cumulative_sum == 0:
#             count += 1
        
#         # If the cumulative sum has been seen before, 
#         # it means there are subarrays with sum zero
#         if cumulative_sum in cumulative_sum_freq:
#             count += cumulative_sum_freq[cumulative_sum]
        
#         # Update the frequency of the cumulative sum
#         cumulative_sum_freq[cumulative_sum] += 1
    
#     return count

# # Example usage
# arr = [1, -1, 1, -1]
# print("Number of subarrays with sum zero:", count_subarrays_with_sum_zero(arr))

#Hashing - Sliding Window Technique
# def min_sum_subarray(arr, k):
#     if len(arr) < k:
#         return None  # If the array is smaller than k, return None
    
#     # Calculate the sum of the first window of size k
#     window_sum = sum(arr[:k])
#     min_sum = window_sum
    
#     # Slide the window from start to end of the array
#     for i in range(len(arr) - k):
#         # Update the window sum by removing the element left behind and adding the new element
#         window_sum = window_sum - arr[i] + arr[i + k]
#         # Update the minimum sum if needed
#         min_sum = min(min_sum, window_sum)
    
#     return min_sum

# # Example usage
# arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 4
# print(f"Minimum sum of subarray of length {k}:", min_sum_subarray(arr, k))

#Hashing - TOP K MOST FREQUENT ELEMENTS
# from collections import defaultdict
# import heapq

# def top_k_frequent_elements(arr, k):
#     # Step 1: Count frequencies
#     frequency_map = defaultdict(int)
#     for num in arr:
#         frequency_map[num] += 1
    
#     # Step 2: Use a max-heap to keep track of top k elements
#     max_heap = []
#     for num, freq in frequency_map.items():
#         heapq.heappush(max_heap, (-freq, num))
    
#     # Step 3: Extract the top k elements from the heap
#     top_k_elements = []
#     for _ in range(k):
#         freq, num = heapq.heappop(max_heap)
#         top_k_elements.append(num)
    
#     return top_k_elements

# # Example usage
# arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5]
# k = 2
# print(f"Top {k} most frequent elements:", top_k_frequent_elements(arr, k))

#Sudoku Solver
# def solve_sudoku(board):
#     def is_valid(num, row, col):
#         # Check if the number is not already in the current row, column, or subgrid
#         if num in rows[row]:
#             return False
#         if num in cols[col]:
#             return False
#         if num in subgrids[(row // 3, col // 3)]:
#             return False
#         return True

#     def place_number(num, row, col):
#         board[row][col] = num
#         rows[row].add(num)
#         cols[col].add(num)
#         subgrids[(row // 3, col // 3)].add(num)

#     def remove_number(num, row, col):
#         board[row][col] = '.'
#         rows[row].remove(num)
#         cols[col].remove(num)
#         subgrids[(row // 3, col // 3)].remove(num)

#     def backtrack(row, col):
#         if row == 9:
#             return True
#         if col == 9:
#             return backtrack(row + 1, 0)
#         if board[row][col] != '.':
#             return backtrack(row, col + 1)
        
#         for num in range(1, 10):
#             if is_valid(num, row, col):
#                 place_number(num, row, col)
#                 if backtrack(row, col + 1):
#                     return True
#                 remove_number(num, row, col)
        
#         return False

#     # Initialize the tracking sets
#     rows = [set() for _ in range(9)]
#     cols = [set() for _ in range(9)]
#     subgrids = {(i, j): set() for i in range(3) for j in range(3)}
    
#     # Fill the sets with the initial numbers
#     for r in range(9):
#         for c in range(9):
#             if board[r][c] != '.':
#                 num = int(board[r][c])
#                 rows[r].add(num)
#                 cols[c].add(num)
#                 subgrids[(r // 3, c // 3)].add(num)
    
#     # Start the backtracking algorithm
#     backtrack(0, 0)

# # Example usage
# sudoku_board = [
#     [5, 3, '.', '.', 7, '.', '.', '.', '.'],
#     [6, '.', '.', 1, 9, 5, '.', '.', '.'],
#     ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
#     [8, '.', '.', '.', 6, '.', '.', '.', 3],
#     [4, '.', '.', 8, '.', 3, '.', '.', 1],
#     [7, '.', '.', '.', 2, '.', '.', '.', 6],
#     ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
#     ['.', '.', '.', 4, 1, 9, '.', '.', 5],
#     ['.', '.', '.', '.', 8, '.', '.', 7, 9]
# ]

# solve_sudoku(sudoku_board)
# for row in sudoku_board:
#     print(row)
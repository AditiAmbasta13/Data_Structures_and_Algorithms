"""
Round 1:

Find max length subarray which has all the element equal to key.(Two pointer question)
Example : Given array a = [1,2,2,1,3,4,5,2,3,2,2,2] and key 2 then max length of subarray containing only 2 is 3(last three element).

Now we are given key as querries, we need to give max length of subarray for each query.
Example : Given array a = [1,2,2,1,3,4,5,2,3,2,2,2] and keys [1,2,3] , we have return [1,3,1]

Now we need to find max length of subarray if you are allowed at most k different element apart from key.
Example : Given array a = [1,2,2,1,3,4,5,2,3,2,2,2] and key 2 and k = 2 that means we need to find a max subarray with at most 2 elements differing from key 2. Output = 6
"""

# a = [1, 2, 2, 1, 3, 4, 5, 2, 3, 2, 2, 2]
# key = 2
# k = 2
# max_len = 0
# left = 0
# count_non_key = 0
# for right in range(len(a)):
#     if a[right] != key:
#         count_non_key += 1
    
#     while count_non_key > k:
#         if a[left] != key:
#             count_non_key -= 1
#         left += 1
#     max_len = max(max_len, right - left + 1)
# print(max_len)

"""
Round 2 : Given an n ary tree we have to decode the string.
Example :
A
/ \\
B(Hi) C
/ \\
D(I) E(am)
Every leaf is linked to some decoded string which means every path from root to leaf has a decoded value.
"AB" -> "Hi"
"ACD" -> "I"
"ACE" -> "am"
Input will be a string that we need to decode if that is not possible return "Invalid".
Example "ABABACDACE" --> "HiHiIam"
"ABCBACE" --> "Invalid"
"""

# class TreeNode:
#     def __init__(self, letter, word) -> None:
#         self.letter = letter
#         self.word = word
#         self.left = None
#         self.right = None

# root = TreeNode("A", "")
# root.left = TreeNode("B", "Hi")
# root.right = TreeNode("C", "")
# root.left.left = TreeNode("D", "I")
# root.left.right = TreeNode("E", "am")

# def pre_order(root, order):
#     if not root:
#         return
#     print(root.word, end=" ")
#     pre_order(root.left)
#     pre_order(root.right)

# pre_order(root)


"""
Round 3: Given an array where elements are sorted based on the first 28 most significant bits. Sort the array.
Example: [1,3,2,4,10,9] --> [1,2,3,4,9,10]
"""

# def sort_28_msb(arr):
#     return sorted(arr, key=lambda x: (x >> 4, x & 0xF))

# # Test
# arr = [1, 3, 2, 4, 10, 9]
# print(sort_28_msb(arr))  # Output: [1, 2, 3, 4, 9, 10]

# def modified_counting_sort(arr):
#     # Create 16 buckets (2^4, as we're considering the last 4 bits)
#     buckets = [[] for _ in range(16)]
    
#     # Place each number in its corresponding bucket
#     for num in arr:
#         bucket_index = num & 0xF  # Get the last 4 bits
#         buckets[bucket_index].append(num)
    
#     # Flatten the buckets back into the array
#     return [num for bucket in buckets for num in bucket]

# # Test
# arr = [1, 3, 2, 4, 10, 9]
# print(modified_counting_sort(arr))  # Output: [1, 9, 2, 10, 4, 3]

# def full_modified_counting_sort(arr):
#     for shift in range(28, -1, -4):
#         buckets = [[] for _ in range(16)]
#         for num in arr:
#             bucket_index = (num >> shift) & 0xF
#             buckets[bucket_index].append(num)
#         arr = [num for bucket in buckets for num in bucket]
#     return arr

# # Test
# arr = [1, 3, 2, 4, 10, 9]
# print(full_modified_counting_sort(arr))  # Output: [1, 2, 3, 4, 9, 10]

"""Implement Minesweeper"""
# class Minesweeper:
#     def __init__(self, grid):
#         self.grid = grid
#         self.m, self.n = len(grid), len(grid[0])
#         self.display = [['-' for _ in range(self.n)] for _ in range(self.m)]

#     def count_adjacent_mines(self, x, y):
#         directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
#         count = 0
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < self.m and 0 <= ny < self.n and self.grid[nx][ny] == 9:
#                 count += 1
#         return count

#     def reveal(self, x, y):
#         if not (0 <= x < self.m and 0 <= y < self.n) or self.display[x][y] != '-':
#             return
        
#         if self.grid[x][y] == 9:
#             self.display[x][y] = 'X'
#             print("Game Over! You hit a mine.")
#             return
        
#         mines_count = self.count_adjacent_mines(x, y)
#         self.display[x][y] = str(mines_count)
        
#         if mines_count == 0:
#             directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 self.reveal(nx, ny)

#     def display_board(self):
#         for row in self.display:
#             print(' '.join(row))

# # Example usage:
# grid = [
#     [0, 1, 9],
#     [1, 2, 1],
#     [9, 1, 0]
# ]

# game = Minesweeper(grid)
# game.reveal(0, 0)
# game.display_board()

"""
word square or not?
BALL
AREA
LEAD
LADY
"""

def wordsq(words):
        k = len(words)
        for i in range(k):
            for j in range(i, k):  # Start from i to avoid redundant checks
                if words[i][j] != words[j][i]:
                    return False
        
        return True
    
words1 = ["BALL", "AREA", "LEAD", "LADY"]
print(wordsq(words1))  # Output: True

words2 = ["BALL", "AREA", "LEAD", "YARD"]
print(wordsq(words2))  # Output: False
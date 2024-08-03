# Tries
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True
    
#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.is_end_of_word
    
#     def starts_with(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True

# # Example usage:
# trie = Trie()

# # Insert words
# trie.insert("apple")
# trie.insert("app")
# trie.insert("apricot")

# # Search for words
# print(trie.search("apple"))    # True
# print(trie.search("app"))      # True
# print(trie.search("apricot"))  # True
# print(trie.search("apr"))      # False

# # Check prefixes
# print(trie.starts_with("app"))  # True
# print(trie.starts_with("apr"))  # True
# print(trie.starts_with("b"))    # False

#XOR SubArray - Tries Challenges
# class TrieNode:
#     def __init__(self):
#         self.children = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, num):
#         node = self.root
#         for i in range(31, -1, -1):  # Assuming 32-bit integers
#             bit = (num >> i) & 1 #Get current bit
#             if bit not in node.children:
#                 node.children[bit] = TrieNode()
#             node = node.children[bit]
    
#     def find_max_xor_pair(self, num):
#         node = self.root
#         max_xor = 0
#         for i in range(31, -1, -1):
#             bit = (num >> i) & 1
#             if 1 - bit in node.children: #If opposite is present
#                 max_xor |= (1 << i)
#                 node = node.children[1 - bit]
#             else:
#                 node = node.children[bit]
#         return max_xor

# def max_xor_subarray(arr):
#     trie = Trie()
#     max_xor = 0
#     trie.insert(0)
#     for num in arr:
#         # Find the maximum XOR with num using existing numbers in the Trie
#         max_xor = max(max_xor, trie.find_max_xor_pair(num))
#         # Insert num into the Trie
#         trie.insert(num)
#     return max_xor


# # # Test the function
# arr = [3, 10, 5, 15, 2]
# print(f"Maximum XOR subarray value: {max_xor_subarray(arr)}")

#Trie Bash - this code is not fully right
# class TrieNode:
#     def __init__(self):
#         self.child = {}
#         self.value = None

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, num):
#         node = self.root
#         for i in reversed(range(32)):  # Assuming 32-bit integers
#             bit = (num >> i) & 1
#             if bit not in node.child:
#                 node.child[bit] = TrieNode()
#             node = node.child[bit]
    
#     def find_max_xor(self, num):
#         node = self.root
#         current_xor = 0
#         for i in reversed(range(32)):  # Assuming 32-bit integers
#             bit = (num >> i) & 1
#             opposite_bit = 1 - bit
#             if opposite_bit in node.child:
#                 current_xor = (current_xor << 1) | 1
#                 node = node.child[opposite_bit]
#             else:
#                 current_xor = (current_xor << 1)
#                 node = node.child[bit]
#         return current_xor

# def max_xor_sum(arr):
#     n = len(arr)
    
#     # Step 1: Calculate max XOR for subarrays ending at each index from right to left
#     right_max_xor = [0] * (n + 1)
#     trie = Trie()
#     prefix_xor = 0
    
#     # This will store the maximum XOR of subarrays ending at each index
#     max_xor_right = 0
    
#     for i in range(n - 1, -1, -1):
#         prefix_xor ^= arr[i]
#         trie.insert(prefix_xor)
#         max_xor_right = max(max_xor_right, trie.find_max_xor(prefix_xor))
#         right_max_xor[i] = max_xor_right
    
#     # Step 2: Calculate max XOR for subarrays starting at each index from left to right
#     left_max_xor = [0] * (n + 1)
#     trie = Trie()
#     prefix_xor = 0
    
#     # This will store the maximum XOR of subarrays starting at each index
#     max_xor_left = 0
    
#     for i in range(n):
#         prefix_xor ^= arr[i]
#         trie.insert(prefix_xor)
#         max_xor_left = max(max_xor_left, trie.find_max_xor(prefix_xor))
#         left_max_xor[i] = max_xor_left
    
#     # Step 3: Find the maximum sum of XORs from two non-overlapping subarrays
#     max_sum = 0
#     for i in range(n - 1):
#         max_sum = max(max_sum, left_max_xor[i] + right_max_xor[i + 1])
    
#     return max_sum

# # Example usage:
# arr = [1, 2, 6, 8]
# print(max_xor_sum(arr))  # Output should be 17

#Digital Dictionary
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True
    
#     def starts_with(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False, []
#             node = node.children[char]
        
#         # If the prefix exists, perform DFS to find all words with this prefix
#         results = []
#         self._dfs(node, prefix, results)
#         return True, results
    
#     def _dfs(self, node, path, results):
#         if node.is_end_of_word:
#             results.append(path)
#         for char, child_node in node.children.items():
#             self._dfs(child_node, path + char, results)
    
#     def find_and_add_word(self, prefix, new_word):
#         exists, words = self.starts_with(prefix)
#         if exists:
#             # Prefix exists, display words with the prefix
#             print(f"Words with prefix '{prefix}': {words}")
#         else:
#             # Prefix does not exist, display message and insert new word
#             print(f"No words found with prefix '{prefix}'. Adding '{new_word}'.")
#             self.insert(new_word)
#             # Recheck all words with the prefix including the new word
#             exists, words = self.starts_with(prefix)
#             print(f"Words with prefix '{prefix}' after adding '{new_word}': {words}")

# # Example usage
# trie = Trie()

# # Insert some initial words
# trie.insert("apple")
# trie.insert("app")
# trie.insert("applet")
# trie.insert("apply")

# # Test case 1: Prefix exists
# prefix = "app"
# new_word = "appleseed"
# trie.find_and_add_word(prefix, new_word)  # Should display existing words with prefix and then add the new word

# # Test case 2: Prefix does not exist
# prefix = "banana"
# new_word = "bananas"
# trie.find_and_add_word(prefix, new_word)  # Should display message that prefix is not found, then add the new word
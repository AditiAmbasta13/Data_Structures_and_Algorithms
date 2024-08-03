# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         self.root = self._insert(self.root, value)
    
#     def _insert(self, node, value):
#         if node is None:
#             return Node(value)
#         if value < node.value:
#             node.left = self._insert(node.left, value)
#         else:
#             node.right = self._insert(node.right, value)
#         return node
    
#     def inorder_print(self):
#         self._inorder_print(self.root)
#         print()
    
#     def _inorder_print(self, node):
#         if node:
#             self._inorder_print(node.left)
#             print(node.value, end=' ')
#             self._inorder_print(node.right)
    
#     def search(self, value):
#         return self._search(self.root, value)
    
#     def _search(self, node, value):
#         if node is None or node.value == value:
#             return node
#         if value < node.value:
#             return self._search(node.left, value)
#         return self._search(node.right, value)
    
#     def delete(self, value):
#         self.root = self._delete(self.root, value)
    
#     def _delete(self, node, value):
#         if node is None:
#             return node
#         if value < node.value:
#             node.left = self._delete(node.left, value)
#         elif value > node.value:
#             node.right = self._delete(node.right, value)
#         else:
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#             temp = self._min_value_node(node.right)
#             node.value = temp.value
#             node.right = self._delete(node.right, temp.value)
#         return node
    
#     def _min_value_node(self, node):
#         current = node
#         while current.left:
#             current = current.left
#         return current
    
#     def construct_from_preorder(self, preorder):
#         if not preorder:
#             return None
#         self.root = self._construct_from_preorder(preorder, float('-inf'), float('inf'))
#         return self.root

#     def _construct_from_preorder(self, preorder, min_val, max_val):
#         if not preorder or preorder[0] < min_val or preorder[0] > max_val:
#             return None

#         value = preorder.pop(0)
#         root = Node(value)

#         root.left = self._construct_from_preorder(preorder, min_val, value - 1)
#         root.right = self._construct_from_preorder(preorder, value + 1, max_val)

#         return root

#     def preorder_print(self):
#         self._preorder_print(self.root)
#         print()

#     def _preorder_print(self, node):
#         if node:
#             print(node.value, end=' ')
#             self._preorder_print(node.left)
#             self._preorder_print(node.right)


# # Usage example
# bst = BST()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(1)
# bst.insert(9)

# # print("Inorder traversal:")
# # bst.inorder_print()

# # print("Searching for 7:")
# # result = bst.search(7)
# # print("Found" if result else "Not found")

# # print("Deleting 3")
# # bst.delete(3)

# # print("Inorder traversal after deletion:")
# # bst.inorder_print()

# preorder = [8, 5, 1, 7, 10, 12]
# bst.construct_from_preorder(preorder)
# bst.preorder_print()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def is_valid_bst(root):
#     def validate(node, low=float('-inf'), high=float('inf')):
#         if not node:
#             return True
        
#         if node.val <= low or node.val >= high:
#             return False
        
#         return (validate(node.left, low, node.val) and
#                 validate(node.right, node.val, high))
    
#     return validate(root)

# #Balanced bst from sorted array
# def sorted_array_to_bst(nums):
#     if not nums:
#         return None
    
#     mid = len(nums) // 2
    
#     root = TreeNode(nums[mid])
#     root.left = sorted_array_to_bst(nums[:mid])
#     root.right = sorted_array_to_bst(nums[mid+1:])
    
#     return root

# def preorder_traversal(root):
#     if not root:
#         return
#     print(root.val, end=' ')
#     preorder_traversal(root.left)
#     preorder_traversal(root.right)

# #Catalan Numbers
# def catalan(n):
#     if n <= 1:
#         return 1
#     result = 0
#     for i in range(n):
#         result += catalan(i) * catalan(n - i - 1)
#     return result
# def num_trees(n):
#     return catalan(n)

# def generate_trees(start, end):
#     trees = []
    
#     if start > end:
#         trees.append(None)
#         return trees
    
#     for i in range(start, end + 1):
#         left_subtrees = generate_trees(start, i - 1)
#         right_subtrees = generate_trees(i + 1, end)

#         for left in left_subtrees:
#             for right in right_subtrees:
#                 root = TreeNode(i)
#                 root.left = left
#                 root.right = right
#                 trees.append(root)
    
#     return trees

# #Identical BST
# def are_identical_bsts(root1, root2):
#     # If both trees are empty, they're identical
#     if root1 is None and root2 is None:
#         return True
    
#     # If one tree is empty and the other isn't, they're not identical
#     if root1 is None or root2 is None:
#         return False
    
#     # Check if current nodes have same value
#     # and recursively check left and right subtrees
#     return (root1.val == root2.val and
#             are_identical_bsts(root1.left, root2.left) and
#             are_identical_bsts(root1.right, root2.right))

# # Helper function to insert a value into BST
# def insert(root, val):
#     if not root:
#         return TreeNode(val)
#     if val < root.val:
#         root.left = insert(root.left, val)
#     else:
#         root.right = insert(root.right, val)
#     return root

# # Create two identical BSTs
# # bst1 = None
# # bst2 = None
# # values = [5, 3, 7, 1, 4, 6, 8]
# # for val in values:
# #     bst1 = insert(bst1, val)
# #     bst2 = insert(bst2, val)

# # # Create a different BST
# # bst3 = None
# # different_values = [5, 3, 7, 1, 4, 6, 9]
# # for val in different_values:
# #     bst3 = insert(bst3, val)

# # # Check if BSTs are identical
# # print("BST1 and BST2 are identical:", are_identical_bsts(bst1, bst2))
# # print("BST1 and BST3 are identical:", are_identical_bsts(bst1, bst3))

# #Longest BST in BT
# class NodeInfo:
#     def __init__(self, size, min_val, max_val, is_bst):
#         self.size = size
#         self.min_val = min_val
#         self.max_val = max_val
#         self.is_bst = is_bst

# def largest_bst_subtree(root):
#     def largest_bst_helper(node):
#         if not node:
#             return NodeInfo(0, float('inf'), float('-inf'), True)
#         left = largest_bst_helper(node.left)
#         right = largest_bst_helper(node.right)
        
#         if (left.is_bst and right.is_bst and
#             left.max_val < node.val < right.min_val):
#             return NodeInfo(
#                 left.size + right.size + 1,
#                 min(left.min_val, node.val),
#                 max(right.max_val, node.val),
#                 True
#             )
#         else:
#             return NodeInfo(
#                 max(left.size, right.size),
#                 float('-inf'),
#                 float('inf'),
#                 False
#             )
#     return largest_bst_helper(root).size

# root = TreeNode(50)
# root.left = TreeNode(30)
# root.right = TreeNode(60)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(20)
# root.right.left = TreeNode(45)
# root.right.right = TreeNode(70)
# root.right.right.left = TreeNode(65)
# root.right.right.right = TreeNode(80)

# largest_bst_size = largest_bst_subtree(root)
# print("Size of the largest BST subtree:", largest_bst_size)

# #Recover BST
# def recoverTree(self, root):
#     self.first = None
#     self.second = None
#     self.prev = TreeNode(float('-inf'))
    
#     def inorder(node):
#         if not node:
#             return
        
#         inorder(node.left)
        
#         if self.first is None and self.prev.val >= node.val:
#             self.first = self.prev
#         if self.first is not None and self.prev.val >= node.val:
#             self.second = node
#         self.prev = node
        
#         inorder(node.right)
    
#     inorder(root)
#     self.first.val, self.second.val = self.second.val, self.first.val

# from collections import deque
# def zigzag_traversal(root):
#     if not root:
#         return []
    
#     result = []
#     queue = deque([root])
#     left_to_right = True
    
#     while queue:
#         level_size = len(queue)
#         level_nodes = deque()
        
#         for _ in range(level_size):
#             node = queue.popleft()
            
#             if left_to_right:
#                 level_nodes.append(node.val)
#             else:
#                 level_nodes.appendleft(node.val)
            
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         result.extend(level_nodes)
#         left_to_right = not left_to_right
    
#     return result

# # Helper function to create a BST
# def insert(root, val):
#     if not root:
#         return TreeNode(val)
#     if val < root.val:
#         root.left = insert(root.left, val)
#     else:
#         root.right = insert(root.right, val)
#     return root

# # Create a sample BST
# root = None
# values = [4, 2, 6, 1, 3, 5, 7]
# for val in values:
#     root = insert(root, val)

# # Perform zig-zag traversal
# result = zigzag_traversal(root)
# print("Zig-zag traversal:", result)

# def print_tree(root, level=0, prefix="Root: "):
#     if root is not None:
#         print(" " * (level * 4) + prefix + str(root.val))
#         if root.left or root.right:
#             print_tree(root.left, level + 1, "L--- ")
#             print_tree(root.right, level + 1, "R--- ")

# # Generate all possible BSTs with 3 nodes
# all_trees = generate_trees(1, 3)

# # Print all generated trees
# for i, tree in enumerate(all_trees, 1):
#     print(f"\nTree {i}:")
#     print_tree(tree)

# # Test the function
# sorted_array = [1, 2, 3, 4, 5, 6, 7]
# bst_root = sorted_array_to_bst(sorted_array)

# print("Inorder traversal of the balanced BST:")
# preorder_traversal(bst_root)

# # Test the function
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(7)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(8)

#print(is_valid_bst(root))  # Should print True
# #Binary Tree
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# # def inorder_traversal(root):
# #     if root:
# #         inorder_traversal(root.left)
# #         print(root.value, end=' ')
# #         inorder_traversal(root.right)

# # def preorder_traversal(root):
# #     if root:
# #         print(root.value, end=' ')
# #         preorder_traversal(root.left)
# #         preorder_traversal(root.right)

# # def postorder_traversal(root):
# #     if root:
# #         postorder_traversal(root.left)
# #         postorder_traversal(root.right)
# #         print(root.value, end=' ')

# #     print("Inorder traversal:")
# #     inorder_traversal(root)
# #     print("\nPreorder traversal:")
# #     preorder_traversal(root)
# #     print("\nPostorder traversal:")
# #     postorder_traversal(root)

# #Building a Binary Tree from Inorder and Preorder Traversals
# # class TreeNode:
# #     def __init__(self, value=0, left=None, right=None):
# #         self.value = value
# #         self.left = left
# #         self.right = right
# # def build_tree_from_inorder_preorder(inorder, preorder):
# #     if not inorder or not preorder:
# #         return None

# #     # The first element in preorder is the root
# #     root_value = preorder.pop(0)
# #     root = TreeNode(root_value)

# #     # Split the inorder list into left and right subtrees
# #     inorder_index = inorder.index(root_value)

# #     # Build the left subtree before the right subtree since we are consuming preorder from the start
# #     root.left = build_tree_from_inorder_preorder(inorder[:inorder_index], preorder)
# #     root.right = build_tree_from_inorder_preorder(inorder[inorder_index + 1:], preorder)

# #     return root

# # # Example usage:
# # inorder = [4, 2, 5, 1, 6, 3, 7]
# # preorder = [1, 2, 4, 5, 3, 6, 7]
# # root = build_tree_from_inorder_preorder(inorder, preorder)

# # def inorder_traversal(root):
# #     if root:
# #         inorder_traversal(root.left)
# #         print(root.value, end=' ')
# #         inorder_traversal(root.right)

# # print("Inorder traversal of the constructed tree:")
# # inorder_traversal(root)

# #Building a Binary Tree from Inorder and Postorder Traversals
# # class TreeNode:
# #     def __init__(self, value=0, left=None, right=None):
# #         self.value = value
# #         self.left = left
# #         self.right = right

# # def build_tree_from_inorder_postorder(inorder, postorder):
# #     if not inorder or not postorder:
# #         return None

# #     # The last element in postorder is the root
# #     root_value = postorder.pop()
# #     root = TreeNode(root_value)

# #     # Split the inorder list into left and right subtrees
# #     inorder_index = inorder.index(root_value)

# #     # Build the right subtree before the left subtree since we are consuming postorder from the end
# #     root.right = build_tree_from_inorder_postorder(inorder[inorder_index + 1:], postorder)
# #     root.left = build_tree_from_inorder_postorder(inorder[:inorder_index], postorder)

# #     return root

# # # Example usage:
# # inorder = [4, 2, 5, 1, 6, 3, 7]
# # postorder = [4, 5, 2, 6, 7, 3, 1]
# # root = build_tree_from_inorder_postorder(inorder, postorder)

# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.value, end=' ')
#         inorder_traversal(root.right)

# # print("Inorder traversal of the constructed tree:")
# # inorder_traversal(root)

# #Level Order Traversal
# from collections import deque
# def printLevelOrder(root):
#     if root == None:
#         return
#     queue = deque([root])
    
#     while queue:
#         node = queue.popleft()
#         print(node.value, end=' ')
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

# #Sum At Kth Level
# def sumatK(root, k):
#     if root == None:
#         return -1
#     queue = deque([(root, 0)])
#     sum = 0
#     while queue:
#         node, level = queue.popleft()
#         if level == k:
#             sum += node.value
#         if node.left:
#             queue.append((node.left, level+1))
#         if node.right:
#             queue.append((node.right, level+1))
#     return sum

# def countNodes(root):
#     if root == None:
#         return 0
#     return countNodes(root.left) + countNodes(root.right) + 1

# def sumNodes(root):
#     if root == None:
#         return 0
#     return sumNodes(root.left) + sumNodes(root.right) + root.value

# def heightTree(root): #O(n)
#     if root == None:
#         return 0
#     heightl = heightTree(root.left)
#     heightr = heightTree(root.right)
#     return max(heightl, heightr) + 1

# #Diameter of a tree, number of node in the longest path between two leaves
# def diameterTree(root):  #O(n*n)
#     if root == None:
#         return 0
#     heightl = heightTree(root.left)
#     heightr = heightTree(root.right)
#     currdia = heightl + heightr + 1

#     ldia = diameterTree(root.left)
#     rdia = diameterTree(root.right)
#     return max(currdia, max(ldia, rdia))

# def diameter_optimized(root):  #O(n)
#     def dfs(node):
#         if not node:
#             return 0, 0
#         left_height, left_diameter = dfs(node.left)
#         right_height, right_diameter = dfs(node.right)
        
#         height = max(left_height, right_height) + 1
#         curr_diameter = left_height + right_height + 1
#         max_diameter = max(curr_diameter, left_diameter, right_diameter)
#         return height, max_diameter
#     _, diameter = dfs(root)
#     return diameter

# #Sum Replacement in Binary Tree - Replace sum of each node with the sum of all subtree nodes and itself
# def sumReplace(root):
#     if root == None:
#         return
#     sumReplace(root.left)
#     sumReplace(root.right)
#     if root.left != None:
#         root.value += root.left.value
#     if root.right != None:
#         root.value += root.right.value

# #Balanced Height in Binary Tree - for each node leftsubtree height - rightsubtree height <= 1
# # def isBalanced(root): #O(n*n)
# #     if root == None:
# #         return True
# #     if not isBalanced(root.left):
# #         return False
# #     if not isBalanced(root.right):
# #         return False
# #     lh = heightTree(root.left)
# #     rh = heightTree(root.right)
# #     if abs(lh - rh) <= 1:
# #         return True
# #     else:
# #         return False
    
# def isBalanced(root): #O(n)
#     def dfs(node):
#         if not node:
#             return 0, True
        
#         left_height, left_balanced = dfs(node.left)
#         right_height, right_balanced = dfs(node.right)
        
#         balanced = (left_balanced and right_balanced and 
#                     abs(left_height - right_height) <= 1)
        
#         return max(left_height, right_height) + 1, balanced
    
#     _, is_balanced = dfs(root)
#     return is_balanced

# #Right View of a Binary Tree
# def rightView(root):
#     if root == None:
#         return
#     queue = deque([root])
#     while queue:
#         n = len(queue)
#         for i in range(n):
#             node = queue.popleft()
#             if i == n-1:
#                 print(node.value, end=' ')
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

# #Left View of a Binary Tree
# def leftView(root):
#     if root == None:
#         return
#     queue = deque([root])
#     while queue:
#         n = len(queue)
#         for i in range(n):
#             node = queue.popleft()
#             if i == 0:
#                 print(node.value, end=' ')
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

# #Shortest distance between two nodes
# def LCA(root, n1, n2):
#     if root is None:
#         return None
#     if root.value == n1 or root.value == n2:
#         return root

#     left = LCA(root.left, n1, n2)
#     right = LCA(root.right, n1, n2)

#     if left is not None and right is not None:
#         return root
#     return left if left is not None else right

# def findDist(root, k, dist):
#     if root is None:
#         return -1
#     if root.value == k:
#         return dist

#     left = findDist(root.left, k, dist + 1)
#     if left != -1:
#         return left

#     return findDist(root.right, k, dist + 1)

# def distanceBtw(root, n1, n2):
#     lca = LCA(root, n1, n2)
#     if lca is None:
#         return -1

#     d1 = findDist(lca, n1, 0)
#     d2 = findDist(lca, n2, 0)

#     return d1 + d2

# #Flatten Binary Tree in place
# def Flatten(root):
#     if root == None or (root.left == None and root.right == None):
#         return
#     if root.left != None:
#         Flatten(root.left)

#         temp = root.right
#         root.right = root.left 
#         root.left = None

#         t = root.right
#         while(t.right != None):
#             t = t.right
#         t.right = temp

#     Flatten(root.right)

# #Nodes at Distance K in Binary Tree
# #Case 1 Subtree
# def printSubtree(root, k):
#     if root == None or k < 0:
#         return
#     if k == 0:
#         print(root.value, end=" ")
#         return
#     printSubtree(root.left, k-1)
#     printSubtree(root.right, k-1)

# #Case2 Ancestor
# def printAtKNodes(root, target, k):
#     if root == None:
#         return -1
#     if root == target:
#         printSubtree(root, k)
#         return 0
#     dl = printAtKNodes(root.left, target, k)
#     if(dl != -1):
#         if(dl+1 == k):
#             print(root.value, end=" ")
#         else:
#             printSubtree(root.left, k-dl-2)
#         return 1+dl
#     dr = printAtKNodes(root.right, target, k)
#     if(dr != -1):
#         if(dr+1 == k):
#             print(root.value, end=" ")
#         else:
#             printSubtree(root.right, k-dr-2)
#         return 1+dr
#     return -1

# #Lowest Commen Ancestor of 2 nodes - better method
# def lcac(root, n1, n2):
#     if root is None:
#         return None

#     if root.value == n1 or root.value == n2:
#         return root

#     left_lca = lcac(root.left, n1, n2)
#     right_lca = lcac(root.right, n1, n2)

#     if left_lca and right_lca:
#         return root

#     return left_lca if left_lca is not None else right_lca

# #other method - O(n)
# def findPath(root, path, k):
#     if root is None:
#         return False
#     path.append(root)
#     if root.value == k:
#         return True
#     if (root.left and findPath(root.left, path, k)) or (root.right and findPath(root.right, path, k)):
#         return True
#     path.pop()
#     return False

# def findLCA(root, n1, n2):
#     path1 = []
#     path2 = []
#     if not findPath(root, path1, n1) or not findPath(root, path2, n2):
#         return None
#     i = 0
#     while i < len(path1) and i < len(path2):
#         if path1[i].value != path2[i].value:
#             break
#         i += 1

#     return path1[i - 1]

# #Maximum path sum
# def maxPathSum(root):
#     def maxPathUtil(node):
#         nonlocal max_sum
#         if not node:
#             return 0
        
#         left = max(maxPathUtil(node.left), 0)
#         right = max(maxPathUtil(node.right), 0)
        
#         current_sum = node.value + left + right
#         max_sum = max(max_sum, current_sum)
        
#         return node.value + max(left, right)

#     max_sum = float('-inf')
#     maxPathUtil(root)
#     return max_sum

# # Example usage:
# if __name__ == "__main__":
#     # Create a simple binary tree
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     # root.left.right = TreeNode(5)
#     # root.right.left = TreeNode(6)
#     root.right.right = TreeNode(5)
#     #printLevelOrder(root)
#     # print(sumatK(root, 2))
#     #print(countNodes(root))
#     #print(sumNodes(root))
#     #print(heightTree(root))
#     #print(diameterTree(root))
#     #print(diameter_optimized(root))
#     # sumReplace(root)
#     # print()
#     # printLevelOrder(root)
#     #print(isBalanced(root))
#     #rightView(root)
#     #leftView(root)
#     #print(distanceBtw(root, 2, 3))
#     # Flatten(root)
#     # inorder_traversal(root)
#     #printAtKNodes(root, root.left, 1)
#     # node = lcac(root, 5, 6)
#     # print(node.value)
#     # node = findLCA(root, 5, 6)
#     # print(node.value)
#     print(maxPathSum(root))
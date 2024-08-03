# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_head(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     def insert_at_tail(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node
#             new_node.prev = last

#     def delete_node(self, key):
#         current = self.head

#         # If the list is empty
#         if current is None:
#             return

#         # If the node to be deleted is the head
#         if current.data == key:
#             self.head = current.next
#             if self.head:
#                 self.head.prev = None
#             return

#         # Traverse the list to find the node to delete
#         while current and current.data != key:
#             current = current.next

#         # If the node to be deleted is not found
#         if current is None:
#             return

#         # If the node to be deleted is the last node
#         if current.next is None:
#             current.prev.next = None
#         else:
#             # Delete the node
#             current.prev.next = current.next
#             current.next.prev = current.prev

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" <-> ")
#             current = current.next
#         print("None")

# # Example usage
# dll = DoublyLinkedList()
# dll.insert_at_head(1)
# dll.insert_at_head(2)
# dll.insert_at_tail(3)
# dll.insert_at_tail(4)
# dll.display()  # Output: 2 <-> 1 <-> 3 <-> 4 <-> None

# dll.delete_node(1)
# dll.display()  # Output: 2 <-> 3 <-> 4 <-> None

# dll.delete_node(2)
# dll.display()  # Output: 3 <-> 4 <-> None

# dll.delete_node(4)
# dll.display()  # Output: 3 <-> None

# dll.delete_node(3)
# dll.display()  # Output: None
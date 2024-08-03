# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class CircularLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_head(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             # New node points to itself, making it a circular list
#             new_node.next = new_node
#             self.head = new_node
#         else:
#             # Insert new node before the current head
#             new_node.next = self.head
#             # Find the last node to point to the new head
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             self.head = new_node

#     def insert_at_tail(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             # New node points to itself, making it a circular list
#             new_node.next = new_node
#             self.head = new_node
#         else:
#             # Insert new node at the end
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head

#     def delete_node(self, key):
#         if self.head is None:
#             return

#         # If the node to be deleted is the head
#         if self.head.data == key:
#             if self.head.next == self.head:
#                 # Only one node in the list
#                 self.head = None
#             else:
#                 # Find the last node
#                 current = self.head
#                 while current.next != self.head:
#                     current = current.next
#                 # Update the last node to skip the head
#                 current.next = self.head.next
#                 self.head = self.head.next
#             return

#         # Traverse the list to find the node to delete
#         current = self.head
#         while current.next != self.head and current.next.data != key:
#             current = current.next

#         # If the node to be deleted is not found
#         if current.next.data != key:
#             return

#         # Delete the node
#         current.next = current.next.next

#     def display(self):
#         if self.head is None:
#             print("List is empty")
#             return

#         current = self.head
#         while True:
#             print(current.data, end=" -> ")
#             current = current.next
#             if current == self.head:
#                 break
#         print("... (circular)")

# # Example usage
# cll = CircularLinkedList()
# cll.insert_at_tail(1)
# cll.insert_at_tail(2)
# cll.insert_at_tail(3)
# cll.insert_at_tail(4)
# cll.insert_at_tail(5)
# cll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> ... (circular)

# cll.insert_at_head(0)
# cll.display()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> ... (circular)

# cll.delete_node(3)
# cll.display()  # Output: 0 -> 1 -> 2 -> 4 -> 5 -> ... (circular)

# cll.delete_node(0)
# cll.display()  # Output: 1 -> 2 -> 4 -> 5 -> ... (circular)
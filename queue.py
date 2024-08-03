#Queue using array
# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             return None

#     def front(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             return None

#     def size(self):
#         return len(self.items)

# # Example usage
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# print("Front of the queue:", q.front())
# print("Dequeued item:", q.dequeue())
# print("Queue size:", q.size())

#Queue using Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.size = 0

#     def is_empty(self):
#         return self.size == 0

#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.is_empty():
#             self.front = new_node
#         else:
#             self.rear.next = new_node
#         self.rear = new_node
#         self.size += 1
#         print(f"Enqueued {data}")

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty!")
#             return None
#         data = self.front.data
#         self.front = self.front.next
#         if self.front is None:
#             self.rear = None
#         self.size -= 1
#         print(f"Dequeued {data}")
#         return data

#     def display(self):
#         if self.is_empty():
#             print("Queue is empty!")
#             return
#         current = self.front
#         print("Queue:", end=" ")
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()

# # Example usage
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.display()
# queue.dequeue()
# queue.dequeue()
# queue.display()
# queue.enqueue(5)
# queue.enqueue(6)
# queue.display()

#Queue using stack - 2 stack approch
# class Queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#     def push(self, v):
#         self.s1.append(v)
#     def qpop(self):
#         if not self.s1 and not self.s2:
#             print("Empty Queue")
#             return
#         if not self.s2:
#             while(self.s1):
#                 self.s2.append(self.s1.pop())
#         return self.s2.pop()
# q = Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# print(q.qpop())
# print(q.qpop())

#Queue using stack - recursion
# class Queue:
#     def __init__(self):
#         self.s1 = []
#     def push(self, v):
#         self.s1.append(v)
#     def qpop(self):
#         if not self.s1:
#             print("Empty Queue")
#             return
#         x = self.s1.pop()
#         if not self.s1:
#             return x
#         item = self.qpop()
#         self.s1.append(x)
#         return item
# q = Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# print(q.qpop())
# print(q.qpop())

#Stack using queue - push costly
# from collections import deque
# class StackUsingQueues:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, data):
#         # Enqueue the new element into q2
#         self.q2.append(data)

#         # Transfer all elements from q1 to q2
#         while self.q1:
#             self.q2.append(self.q1.popleft())

#         # Swap the names of q1 and q2
#         self.q1, self.q2 = self.q2, self.q1
#         print(f"Pushed {data}")

#     def pop(self):
#         if not self.q1:
#             print("Stack is empty!")
#             return None

#         # Dequeue from q1, which is the most recent element added
#         return self.q1.popleft()

#     def peek(self):
#         if not self.q1:
#             print("Stack is empty!")
#             return None
        
#         # Peek the front of q1
#         return self.q1[0]

#     def is_empty(self):
#         return not self.q1

#     def display(self):
#         print("Stack:", end=" ")
#         for item in self.q1:
#             print(item, end=" ")
#         print()

# # Example usage
# stack = StackUsingQueues()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.display()
# print("Popped:", stack.pop())
# stack.display()
# print("Peek:", stack.peek())

#Stack using queue - pop costly
# from collections import deque
# class StackUsingQueues:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, data):
#         # Enqueue the new element into q1
#         self.q1.append(data)
#         print(f"Pushed {data}")

#     def pop(self):
#         if not self.q1:
#             print("Stack is empty!")
#             return None
        
#         # Transfer elements from q1 to q2, except the last one
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.popleft())
        
#         # The last element in q1 is the one to be popped
#         popped_item = self.q1.popleft()
        
#         # Swap q1 and q2
#         self.q1, self.q2 = self.q2, self.q1
#         print(f"Popped {popped_item}")
#         return popped_item

#     def peek(self):
#         if not self.q1:
#             print("Stack is empty!")
#             return None
        
#         # To peek, we need to access the last element of q1
#         # Transfer elements from q1 to q2, except the last one
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.popleft())
        
#         # The last element in q1 is the one to be peeked
#         peeked_item = self.q1[0]
        
#         # Move the element back to q1
#         self.q2.append(self.q1.popleft())
#         self.q1, self.q2 = self.q2, self.q1
        
#         print(f"Peeked {peeked_item}")
#         return peeked_item

#     def is_empty(self):
#         return not self.q1

#     def display(self):
#         print("Stack:", end=" ")
#         for item in self.q1:
#             print(item, end=" ")
#         print()

# # Example usage
# stack = StackUsingQueues()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.display()
# print("Popped:", stack.pop())
# stack.display()
# print("Peek:", stack.peek())
# stack.display()
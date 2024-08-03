class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def insert_at_head(self, head, data):
        new_node = Node(data)
        new_node.next = head
        head = new_node
        return head

    # def insert_at_tail(self, data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     last = self.head
    #     while last.next:
    #         last = last.next
    #     last.next = new_node

    # def search(self, key):
    #     current = self.head
    #     while current:
    #         if current.data == key:
    #             return True
    #         current = current.next
    #     return False

    # def delete(self, key):
    #     current = self.head
    #     prev = None

    #     if current and current.data == key:
    #         self.head = current.next
    #         current = None
    #         return

    #     while current and current.data != key:
    #         prev = current
    #         current = current.next

    #     if current is None:
    #         return

    #     prev.next = current.next
    #     current = None

    def print_list(self, head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # def reverse_list(self):
    #     curr = self.head
    #     prevp = None
    #     nextp = None
    #     while(curr != None):
    #         nextp = curr.next
    #         curr.next = prevp
    #         prevp = curr
    #         curr = nextp
    #     self.head = prevp

    # def reverse_k(self, head, k):
    #     curr = head
    #     prevp = None
    #     nextp = None
    #     count = 0
    #     while(curr != None and count < k):
    #         nextp = curr.next
    #         curr.next = prevp
    #         prevp = curr
    #         curr = nextp
    #         count += 1
    #     if nextp != None:
    #         head.next = self.reverse_k(nextp, k)
    #     return prevp


    # def reverse_recur(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     new_node = self.reverse_recur(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return new_node

    # def reverse_list_recursive(self):
    #     self.head = self.reverse_recur(self.head)

#     def detect_cycle(self, head):
#         slow = head
#         fast = head

#         while(fast is not None and fast.next is not None):
#             slow = slow.next 
#             fast = fast.next.next 
#             if slow == fast:
#                 return True
#         return False
    
#     def make_cycle(self, head, pos):
#         if head is None:
#             return
        
#         cycle_start = None
#         curr = head
#         index = 0
#         while curr.next is not None:
#             if index == pos:
#                 cycle_start = curr
#             curr = curr.next
#             index += 1
#         curr.next = cycle_start

#     def remove_cycle(self, head):
#         slow = head
#         fast = head

#         slow = slow.next 
#         fast = fast.next.next 
#         while(fast != slow):
#             slow = slow.next 
#             fast = fast.next.next 
        
#         fast = head
#         while(slow.next != fast.next):
#             slow = slow.next 
#             fast = fast.next
        
#         slow.next = None

    def lenght(self, head):
        if head is None:
            return 0
        if head.next is None:
            return 1
        temp = head
        l = 0
        while(temp != None):
            temp = temp.next
            l += 1
        return l

    def intersect(self, head1, head2, pos):
        temp1 = head1
        pos -= 1
        while(pos):
            pos -= 1
            temp1 = temp1.next
        
        temp2 = head2
        while(temp2.next is not None):
            temp2 = temp2.next
        temp2.next = temp1

    def intersection(self, head1, head2):
        l1 = self.lenght(head1)
        l2 = self.lenght(head2)
        d = 0
        if l1 > l2:
            d = l1 - l2
            ptr1 = head1
            ptr2 = head2
        else:
            d = l2 - l1
            ptr1 = head2
            ptr2 = head1

        while(d):
            ptr1 = ptr1.next
            if ptr1 == None:
                return -1
            d -= 1
        
        while(ptr1 != None and ptr2 != None):
            if ptr1 == ptr2:
                return ptr1.data
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return -1
    
    def merge2sorted(self, head1, head2):
        p1 = head1
        p2 = head2
        dummy = Node(-1)
        p3 = dummy
        while(p1 != None and p2 != None):
            if p1.data < p2.data:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next

        while(p1 != None):
            p3.next = p1
            p1 = p1.next
            p3 = p3.next
        while(p2 != None):
            p3.next = p2
            p2 = p2.next
            p3 = p3.next
        return dummy.next
    
    def merge_recur(self, head1, head2):
        if head1 is None or head2 is None:
            return head1 if head1 else head2
        
        if(head1.data < head2.data):
            result = head1
            result.next = self.merge_recur(head1.next, head2)
        else:
            result = head2
            result.next = self.merge_recur(head1, head2.next)

        return result
        
    def evenAfterOdd(self, head):
        odd = head
        even = head.next
        evenStart = even

        while(odd.next != None and even.next != None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenStart
        if(odd.next == None):
            even.next = None

ll = LinkedList()
head = None
head =ll.insert_at_head(head, 7)
head =ll.insert_at_head(head, 6)
head =ll.insert_at_head(head, 5)
head =ll.insert_at_head(head, 4)
head =ll.insert_at_head(head, 3)
head =ll.insert_at_head(head, 2)
head =ll.insert_at_head(head, 1)
ll.print_list(head) 
ll.evenAfterOdd(head)
ll.print_list(head) 
# head2 = None
# head2 =ll.insert_at_head(head2, 6)
# head2 =ll.insert_at_head(head2, 6)
# head2 =ll.insert_at_head(head2, 2)
# ll.print_list(head2) 
# ll.print_list(ll.merge_recur(head, head2))
# ll.intersect(head, head2, 3)
# ll.print_list(head)
# ll.print_list(head2)
# print(ll.intersection(head, head2))
# ll.insert_at_tail(head, 5)
# print(ll.search(3))  
# print(ll.search(4))  
# ll.delete(3)
# ll.print_list() 
# ll.delete(2)
# ll.print_list()  
# ll.delete(5)
# ll.print_list()  
# ll.reverse_list_recursive()
# head =ll.reverse_k(head,2)
# ll.print_list(head) 
# ll.make_cycle(head, 1)
# print(ll.detect_cycle(head))
# ll.remove_cycle(head)
# print(ll.detect_cycle(head))
# ll.print_list(head)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_head(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_tail(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node

    # def append_k_nodes(self, k):
    #     if self.head is None or k == 0:
    #         return

    #     # Find the length of the linked list
    #     length = 1
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #         length += 1

    #     if k >= length:
    #         return  # No change if k is greater than or equal to the length of the list

    #     # Find the (length-k)th node
    #     split_point = length - k
    #     current = self.head
    #     for _ in range(split_point - 1):
    #         current = current.next

    #     # current is now at the (length-k)th node
    #     new_head = current.next
    #     current.next = None

    #     # Find the last node of the k nodes
    #     last_node = new_head
    #     while last_node.next:
    #         last_node = last_node.next

    #     # Append the last k nodes to the end
    #     last_node.next = self.head
    #     self.head = new_head

    # def print_list(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")

# Example usage
# ll = LinkedList()
# ll.insert_at_tail(1)
# ll.insert_at_tail(2)
# ll.insert_at_tail(3)
# ll.insert_at_tail(4)
# ll.insert_at_tail(5)
# ll.insert_at_tail(6)
# ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# ll.append_k_nodes(3)
# ll.print_list()  # Output: 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> None

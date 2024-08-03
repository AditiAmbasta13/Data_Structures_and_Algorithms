#Heapify
# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     left = 2 * i + 1 
#     right = 2 * i + 2

#     if left < n and arr[largest] < arr[left]:
#         largest = left

#     if right < n and arr[largest] < arr[right]:
#         largest = right

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # swap

#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)

#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # swap
#         heapify(arr, i, 0)

# arr = [12, 11, 13, 5, 6, 7]
# heap_sort(arr)
# print("Sorted array is:", arr)

#Min_heap Max_heap using libs
# import heapq

# # Creating a max-heap
# max_heap = []

# # Function to push an element onto the max-heap
# def push_max_heap(heap, item):
#     heapq.heappush(heap, -item)

# # Function to pop the largest element from the max-heap
# def pop_max_heap(heap):
#     return -heapq.heappop(heap)

# # Adding elements to the max-heap
# push_max_heap(max_heap, 12)
# push_max_heap(max_heap, 11)
# push_max_heap(max_heap, 13)
# push_max_heap(max_heap, 5)
# push_max_heap(max_heap, 6)
# push_max_heap(max_heap, 7)

# # Printing the max-heap (in negative form)
# print("Max-Heap (negative values):", max_heap)

# # Popping elements from the max-heap
# print("Popped element:", pop_max_heap(max_heap))
# print("Max-Heap after pop (negative values):", max_heap)

# import heapq
 
# # Initialize a list with some values
# values = [5, 1, 3, 7, 4, 2]
 
# # Convert the list into a heap
# heapq.heapify(values)
 
# # Print the heap
# print("Heap:", values)
 
# # Add a new value to the heap
# heapq.heappush(values, 6)
 
# # Print the updated heap
# print("Heap after push:", values)
 
# # Remove and return the smallest element from the heap
# smallest = heapq.heappop(values)
 
# # Print the smallest element and the updated heap
# print("Smallest element:", smallest)
# print("Heap after pop:", values)
 
# # Get the n smallest elements from the heap
# n_smallest = heapq.nsmallest(3, values)
 
# # Print the n smallest elements
# print("Smallest 3 elements:", n_smallest)
 
# # Get the n largest elements from the heap
# n_largest = heapq.nlargest(2, values)
 
# # Print the n largest elements
# print("Largest 2 elements:", n_largest)

#Median of Running Stream
# import heapq
# pq_min = []
# pq_max = []

# def insert(x):
#     if len(pq_min) == len(pq_max):
#         if len(pq_max) == 0 or x < -pq_max[0]:
#             heapq.heappush(pq_max, -x)
#         elif x < -pq_max[0]:
#             heapq.heappush(pq_max, -x)
#         else:
#             heapq.heappush(pq_min, x)
#     else:
#         if len(pq_max) > len(pq_min): # we want diff of only 1
#             if x >= -pq_max[0]:
#                 heapq.heappush(pq_min, x)
#             else:
#                 temp = -heapq.heappop(pq_max)
#                 heapq.heappush(pq_min, temp)
#                 heapq.heappush(pq_max, -x)
#         elif len(pq_min) > len(pq_max):
#             if x <= pq_min[0]:
#                 heapq.heappush(pq_max, -x)
#             else:
#                 temp = heapq.heappop(pq_min)
#                 heapq.heappush(pq_max, -temp)
#                 heapq.heappush(pq_min, x)

# def findMedian():
#     if len(pq_min) == len(pq_max):
#         return (pq_min[0]-pq_max[0])/2.0
#     elif len(pq_max) > len(pq_min):
#         return -pq_max[0]
#     else:
#         return pq_min[0]
    
# insert(10)
# print("Median:", findMedian())
# insert(15)
# print("Median:", findMedian())
# insert(21)
# print("Median:", findMedian())
# insert(30)
# print("Median:", findMedian())
# insert(18)
# print("Median:", findMedian())
# insert(19)
# print("Median:", findMedian())

#Merge K sorted Arrays
# import heapq
# def mergeKSortedArrays(arrays):
#     # Create a min-heap
#     min_heap = []
#     result = []

#     # Initialize the heap with the first element from each array
#     for i in range(len(arrays)):
#         if arrays[i]:
#             heapq.heappush(min_heap, (arrays[i][0], i, 0))

#     # Extract the smallest element from the heap and add the next element from the same array
#     while min_heap:
#         val, array_index, element_index = heapq.heappop(min_heap)
#         result.append(val)
#         next_element_index = element_index + 1
        
#         # If there are more elements in the same array, add the next element to the heap
#         if next_element_index < len(arrays[array_index]):
#             next_val = arrays[array_index][next_element_index]
#             heapq.heappush(min_heap, (next_val, array_index, next_element_index))
    
#     return result

# # Example usage
# arrays = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]

# merged_array = mergeKSortedArrays(arrays)
# print("Merged Array:", merged_array)

#Heap -Smallest Sequence with sum >= K
# import heapq
# a = [3, 2, 1, 8, 1]
# k = 12
# pq = []
# for i in a:
#     heapq.heappush(pq, -i)
# sum = 0
# cnt = 0
# while(pq):
#     sum = sum - heapq.heappop(pq)
#     cnt += 1
#     if sum >= k:
#         break
# if sum < k:
#     print(-1)
# else:
#     print(cnt)
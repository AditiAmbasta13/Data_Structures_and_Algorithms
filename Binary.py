#Place Elements to Maximize Minimum Distance
# def can_place_elements(positions, n, elements, min_dist):
#     elements_placed = 1
#     last_position = positions[0]
    
#     for i in range(1, n):
#         if positions[i] - last_position >= min_dist:
#             elements_placed += 1
#             last_position = positions[i]
#             if elements_placed == elements:
#                 return True
    
#     return False

# def max_min_distance(positions, n, elements):
#     positions.sort()
    
#     low = 1
#     high = positions[-1] - positions[0]
#     result = -1
    
#     while low <= high:
#         mid = (low + high) // 2
        
#         if can_place_elements(positions, n, elements, mid):
#             result = mid
#             low = mid + 1  # Try to find a larger distance
#         else:
#             high = mid - 1  # Try a smaller distance
    
#     return result

# # Test the function
# positions = [1, 2, 4, 8, 9]
# n = len(positions)
# elements = 3

# result = max_min_distance(positions, n, elements)
# print(f"Largest minimum distance: {result}")

#Page Allocation Problem
# def is_valid_allocation(arr, n, m, max_pages):
#     students = 1
#     pages = 0
#     for i in range(n):
#         if arr[i] > max_pages:
#             return False
#         if pages + arr[i] > max_pages:
#             students += 1
#             pages = arr[i]
#             if students > m:
#                 return False
#         else:
#             pages += arr[i]
#     return True

# def find_pages(arr, n, m):
#     if n < m:
#         return -1  # Not enough books for all students
    
#     total_pages = sum(arr)
#     start = max(arr)
#     end = total_pages
#     result = -1
    
#     while start <= end:
#         mid = (start + end) // 2
#         if is_valid_allocation(arr, n, m, mid):
#             result = mid
#             end = mid - 1
#         else:
#             start = mid + 1
    
#     return result

# # Test the function
# arr = [12, 34, 67, 90]
# n = len(arr)
# m = 2  # Number of students

# result = find_pages(arr, n, m)
# print(f"Minimum number of pages: {result}")

#Painters Partition Problem
# def is_valid_partition(arr, n, k, max_time):
#     painters = 1
#     time = 0
#     for i in range(n):
#         if arr[i] > max_time:
#             return False
#         if time + arr[i] > max_time:
#             painters += 1
#             time = arr[i]
#             if painters > k:
#                 return False
#         else:
#             time += arr[i]
#     return True

# def partition_painters(arr, n, k):
#     if n < k:
#         return max(arr)  # More painters than boards
    
#     total_length = sum(arr)
#     start = max(arr)
#     end = total_length
#     result = -1
    
#     while start <= end:
#         mid = (start + end) // 2
#         if is_valid_partition(arr, n, k, mid):
#             result = mid
#             end = mid - 1
#         else:
#             start = mid + 1
    
#     return result

# # Test the function
# arr = [10, 20, 30, 40]
# n = len(arr)
# k = 2  # Number of painters

# result = partition_painters(arr, n, k)
# print(f"Minimum time to paint all boards: {result}")

#Search in Sorted and Rotated Array
# def search_rotated(arr, target):
#     left, right = 0, len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#             return mid
        
#         # Check if the left half is sorted
#         if arr[left] <= arr[mid]:
#             if arr[left] <= target < arr[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         # Right half must be sorted
#         else:
#             if arr[mid] < target <= arr[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
    
#     return -1  # Target not found

# # Test the function
# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# result = search_rotated(arr, target)
# print(f"Index of {target}: {result}")

# target = 3
# result = search_rotated(arr, target)
# print(f"Index of {target}: {result}")

#Peak of an array
# def find_peak_element(nums):
#     left, right = 0, len(nums) - 1
    
#     while left < right:
#         mid = (left + right) // 2
        
#         if nums[mid] < nums[mid + 1]:
#             left = mid + 1
#         else:
#             right = mid
    
#     return left  
# nums1 = [1, 2, 3, 1]
# print(f"Peak element index in {nums1}: {find_peak_element(nums1)}")
# nums2 = [1, 2, 1, 3, 5, 6, 4]
# print(f"Peak element index in {nums2}: {find_peak_element(nums2)}")

# def find_peak(nums):
#     low, high = 0, len(nums) - 1
    
#     while low < high:
#         mid = (low + high) // 2
#         if mid == 0 or nums[mid] > nums[mid - 1]:
#             if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
#                 return mid
#             low = mid + 1
#         else:
#             high = mid - 1
    
#     return low

# nums1 = [1, 2, 3, 1]
# print(f"Peak element index in {nums1}: {find_peak(nums1)}")

#Multiple peaks
# def find_peaks_binary(nums):
#     def find_peak_in_range(start, end):
#         if start > end:
#             return []
#         mid = (start + end) // 2
#         peaks = []
#         is_peak = (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1])
        
#         if is_peak:
#             peaks.append(mid)# Recursively search left and right halves
#         peaks.extend(find_peak_in_range(start, mid-1))
#         peaks.extend(find_peak_in_range(mid+1, end))
        
#         return peaks

#     return sorted(find_peak_in_range(0, len(nums)-1))
# nums1 = [1, 3, 2, 4, 1, 5, 3, 6, 2]
# print(f"Peaks in {nums1}: {find_peaks_binary(nums1)}")

# nums2 = [1, 2, 3, 4, 5]
# print(f"Peaks in {nums2}: {find_peaks_binary(nums2)}")

# nums3 = [5, 4, 3, 2, 1]
# print(f"Peaks in {nums3}: {find_peaks_binary(nums3)}")
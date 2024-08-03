#Count Sort
# a = [1, 3, 2, 3, 4, 1, 6, 4, 3]
# m = max(a)
# countarr = [0] * (m + 1)
# for i in range(len(a)):
#     countarr[a[i]] += 1
# for i in range(1, len(countarr)):
#     countarr[i] += countarr[i - 1]
# output = [0] * len(a)
# for i in range(len(a) - 1, -1, -1):
#     countarr[a[i]] -= 1
#     output[countarr[a[i]]] = a[i]
# print(output)

#DNF Sort
# a = [ 1, 0, 1, 2, 1, 2, 0, 1, 2]
# n = len(a)
# low = 0
# mid = 0
# high = n-1
# while(mid <= high):
#     if a[mid] == 0:
#         a[low], a[mid] = a[mid], a[low]
#         low += 1
#         mid += 1
#     elif a[mid] == 1:
#         mid += 1
#     else:
#         a[mid], a[high] = a[high], a[mid]
#         high -= 1
# print(a)

#Wave Sort - google, amazon --alternate elements smaller than its neighbouring elements
# a = [1, 3, 4, 7, 5, 6, 2]
# n = len(a)
# for i in range(1, n-1, 2):
#     if a[i]>a[i-1]:
#         a[i], a[i-1] = a[i-1], a[i]
#     if a[i]>a[i+1] and i <= n-2:
#         a[i], a[i+1] = a[i+1], a[i]
# print(a)

#Count Inversions
# def merge(a, l, mid, r):
#     inv = 0
#     n1 = mid-l
#     n2 = r - mid
#     b = [0] * (len(a))
#     k = 0
#     i = l
#     j = mid
#     while(i < mid and j < r):
#         if a[i] <= a[j]:
#             b[k] = a[i]
#             i+=1
#         else:
#             b[k] = a[j]
#             inv += mid - i
#             j+=1
#         k += 1
#     while(j < r):
#             b[k] = a[j]
#             j+=1
#             k+=1
#     while(i < mid):
#             b[k] = a[i]
#             i+=1
#             k+=1
#     for i in range(n1 + n2):
#         a[l + i] = b[i]
#     return inv
# def mergeSort(a, l, r):
#     inv = 0
#     if(l < r-1):
#         mid = (l+r)//2
#         inv += mergeSort(a, l, mid)
#         inv += mergeSort(a, mid+1, r)
#         inv += merge(a, l, mid, r)
#     return inv
# a = [3, 5, 6, 9, 1, 2, 7, 8]
# n = len(a)
# print(mergeSort(a, 0, n))
#max till i
# a = [2, 5, 4, 6, 1, 4, 7, 3, 8]
# m = 0
# s = []
# for i in range(len(a)):
#     m = max(m, a[i])
#     s.append(m)
# print(s)

#subarry - continous same order subsequence - same order need not continuos
# 1 sec - 10**8

#sum of all subarrays
# a = [1,2,0,7,2]
# ans = []
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         ans.append(sum(a[i:j+1]))
# print(ans)

#Longest arithmetic subarray - google kickstart
# a = [10, 7, 4, 6, 8, 10, 11]
# pd = a[0] - a[1]
# ans = 2
# curr = 2
# for i in range(2, len(a)):
#     if(pd == a[i] - a[i-1]):
#         curr += 1
#     else:
#         pd = a[i] - a[i-1]
#         curr = 2
#     ans = max(ans, curr)
# print(ans)

#Record Breaker - google kickstart
# a = [1, 2, 0, 7, 2, 0, 2, 10, -1] #extra -1 at the end
# mx = 0
# for i in range(len(a)):
#     if a[i] > mx and a[i] > a[i+1]:
#         print(a[i], "Record breaking")
#     mx = max(mx, a[i])

#First Repeating Element
# idx = [-1 for _ in range(10)]
# minidx = float('inf')
# a = [1, 2, 0, 7, 2, 0, 2]
# for i in range(len(a)):
#     if idx[a[i]] != -1:
#         minidx = min(minidx, idx[a[i]])
#     else:
#         idx[a[i]] = i
# print(minidx)

#Subarray with given sum - google -----2 pointer approach
# a = [1, 2, 3, 7, 5]
# i, j = 0, 0
# target = 12
# sum = 0
# n = len(a)
# found = False
# while j < n:
#     sum += a[j]
#     while sum > target and i < j:
#         sum -= a[i]
#         i += 1
#     if sum == target:
#         print(f"Found subarray from index {i+1} to {j+1}")
#         found = True
#     j += 1
# if not found:
#     print("No subarray found with the given sum")

#Smallest missing prime number - amazon
# a = [0, -9, 1, 3, -4, 5]
# ans = -1
# check = [False for _ in range(len(a))]
# for i in range(len(a)):
#     if a[i] >= 0:
#         check[a[i]] = True
# for i in range(len(check)):
#     if check[i] == False:
#         ans = i
#         break
# print(ans)

#Print all possible subarrays
# a = [1, 2, 3, 7, 5]
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         print(a[i:j+1])

#Maximum subarray sum
# a = [1, 2, 3, 7, 5]
# s = 0
# maxs = float('-inf')
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         s = sum(a[i:j+1])
#         maxs = max(s, maxs)
# print(maxs)

#Maximum subarray sum - cummulative sum approach
# a = [1, 2, 3, 7, 5]
# cumm = [0 for _ in range(len(a)+1)]
# for i in range(1, len(a)+1):
#     cumm[i] = cumm[i-1] + a[i-1]
# maxs = float('-inf')
# for i in range(1, len(a)+1):
#     s = 0
#     for j in range(i):
#         s = cumm[i] - cumm[j]
#         maxs = max(s, maxs)
# print(maxs)

#Maximum subarray sum - Kadane's Algorithm
# a = [-1, 4, -6, 7, -4]
# def kadane(a):
#     currsum = 0
#     maxsum = float("-inf")
#     for i in range(len(a)):
#         currsum += a[i]
#         if currsum < 0:
#             currsum = 0
#         maxsum = max(maxsum, currsum)
#     return (maxsum)

#Maximum circular subarray sum - Kadane's Algorithm
# a = [4, -4, 6, -6, 10, -11, 12]
# totalsum = sum(a)
# nowrapsum = kadane(a)
# for i in range(len(a)):
#     a[i] = -a[i]
# wrapsum = totalsum + kadane(a)
# print(max(wrapsum, nowrapsum))

#Pair sum problem
# a = [2, 4, 7, 11, 1, 16, 20, 21, 10]
# n = len(a)
# k = 5
# sum = 0
# low, high = 0, n - 1
# while(low < high):
#     sum = a[low] + a[high]
#     if sum == k:
#         print(low, high)
#         break 
#     elif sum > k:
#         high -= 1
#     else:
#         low += 1
# else:
#     print("Not Found")
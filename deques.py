#Sliding Window maximum
# from collections import deque
# a = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# q = deque()
# ans = []
# for i in range(k):
#     q.append(a[i])
# ans.append(max(q))
# for i in range(k, len(a)):
#     q.popleft()
#     q.append(a[i])
#     ans.append(max(q))
# print(ans)

#Sliding Window maximum - efficient
# from collections import deque
# def maxSlidingWindow(nums, k):
#     result = []
#     window = deque()
    
#     for i, num in enumerate(nums):
#         # Remove indices that are out of the current window
#         if window and window[0] <= i - k:
#             window.popleft()
        
#         # Remove all smaller elements from the back of the deque
#         while window and nums[window[-1]] < num:
#             window.pop()
        
#         window.append(i)
        
#         # Start adding to result once we have our first window
#         if i >= k - 1:
#             result.append(nums[window[0]])
#     return result
# a = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# print(maxSlidingWindow(a, k))

#Largest Rectangle in Histogram
# heights = [2, 1, 5, 6, 2, 3]
# stack = []
# max_area = 0
# heights.append(0)  
# for i, h in enumerate(heights):
#     while stack and stack[-1][1] > h:
#         index, height = stack.pop()
#         max_area = max(max_area, height * (i - index))
#     stack.append((i, h))
# print(max_area)

#Trapping Rainwater
# a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# stack = []
# ans = 0
# for i in range(len(a)):
#     while stack and a[stack[-1]] < a[i]:
#         curr = stack.pop()
#         if not stack:
#             break
#         diff = i - stack[-1] - 1
#         ans += (min(a[stack[-1]], a[i]) - a[curr]) * diff
#     stack.append(i)
# print(ans)

#Redundant Parenthesis
# a = "((a+b))"
# st = []
# ans = False
# for i in a:
#     if i == "(":
#         st.append(i)
#     if i in "+-*/":
#         st.append(i)
#     if i == ")":
#         if st[-1] == "(":
#             ans = True
#         while(st[-1] in "+-*/" and st[-1] != "("):
#             st.pop()
#         st.pop()
# print(ans)

#Stock Span Problem
# a = [100, 80, 60, 70, 60, 75, 85]
# stack = []
# ans = []
# for i in a:
#     d = 1
#     while stack and i > stack[-1][0]:
#         d += stack[-1][1]
#         stack.pop()
#     stack.append((i, d))
#     ans.append(d)
# print(ans)

#Three sum problem
# a = [12, 3, 7, 1, 6, 9]
# a.sort()
# n = len(a)
# t = 24
# ans = False
# for i in range(n):
#     j = i + 1
#     k = n - 1
#     while(j < k):
#         sum = a[i] + a[j] + a[k]
#         if sum == t:
#             ans = True
#             break
#         elif sum > t:
#             k -= 1
#         elif sum < t:
#             j += 1
#     if ans:
#         break
# print(ans)

#Maximum consecutive 1s subarray and change upto k 0s to 1s
# a = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0]
# k = 2
# zerocnt = 0
# i, ans = 0, 0
# for j in range(len(a)):
#     if(a[j] == 0):
#         zerocnt += 1
#     while(zerocnt > k):
#         if a[i] == 0:
#             zerocnt -= 1
#         i += 1
#     ans = max(ans, j-i+1)
# print(ans)

#Longest Substring without repeating characters
# s = "abcabcbb"
# n = len(s)
# h = set()
# ans = 0
# i, j = 0, 0
# while j < n:
#     if s[j] not in h:
#         h.add(s[j])
#         ans = max(ans, j - i + 1)
#         j += 1
#     else:
#         h.remove(s[i])
#         i += 1
# print(ans)
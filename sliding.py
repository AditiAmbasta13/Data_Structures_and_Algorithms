#Maximum sum subarray with len K and sum < X
# k = 3
# a = [7, 5, 4, 6, 8, 9]
# x = 20
# n = 6
# maxsum = float("-inf")
# ksum = sum(a[:k])
# if ksum < x:
#     maxsum = max(ksum, maxsum)
# for i in range(k, n):
#     ksum -= a[i-k]
#     ksum += a[i]
#     if ksum < x:
#         maxsum = max(ksum, maxsum)
# print(maxsum)

#Smallest subarray with sum > x
# sum = 0
# a = [1, 4, 45, 6, 10, 19]
# n = 6
# x = 51
# min_length = n + 1
# start, end = 0, 0
# while(end < n):
#     while(sum <= x and end < n):
#         sum += a[end]
#         end += 1
#     while(sum > x and start < n):
#         if end - start < min_length:
#             min_length = end - start
#         sum -= a[start]
#         start += 1
# print("No such subarray") if min_length == n+1 else print(min_length)

#Number formed by subarray of size k divisible by 3
# a = [84, 23, 45, 12, 56, 82]
# k = 3
# found = False
# ans = []
# ksum = sum(a[:k])
# if ksum%3 == 0:
#     ans = [0, k-1]
#     found = True
# for i in range(k, len(a)):
#     if found:
#         break
#     ksum = ksum + a[i] - a[i-k]

#     if ksum%3 == 0:
#         ans = [i-k+1, i]
#         found = True
# if(not found):
#     ans = [-1, 0]
# if ans[0] == -1:
#     print("Ans not found")
# else:
#     print(a[ans[0]:ans[1]+1])

#Subarray of size k with palindromic concatenation
# def isPal(num):
#     num = str(num)
#     if num == num[::-1]:
#         return True
#     return False
# a = [2, 3, 5, 1, 1, 5]
# k = 4
# num = 0
# for i in range(k):
#     num = num*10 + a[i]
# if isPal(num):
#     print(a[0:k])
# for i in range(k, len(a)):
#     num = (num%pow(10, k-1))*10 + a[i]
#     if isPal(num):
#         print(a[i-k+1:(i-k+1)+k]).

#Maximum perfect nums in len k
# def is_perfect_number(num):
#     if num < 2:
#         return False
#     divisors_sum = 1  # 1 is a divisor for all numbers
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             divisors_sum += i
#             if i != num // i:  # Avoid adding the square root twice for perfect squares
#                 divisors_sum += num // i
#     return divisors_sum == num
# def maxSum(a, n, k):
#     if n < k:
#         print("Invalid")
#         return -1
#     res = sum(a[:k])

#     ksum = res
#     for i in range(k, n):
#         ksum += a[i] - a[i-k]
#         res = max(res, ksum)
#     return res
# def maxPerfects(a, n, k):
#     for i in range(n):
#         if(is_perfect_number(a[i])):
#             a[i] = 1
#         else:
#             a[i] = 0
#     return maxSum(a, n, k)

# a = [28, 2, 3, 6, 496, 99, 8128, 24]
# k = 4
# n = 8
# print(maxPerfects(a, n, k))
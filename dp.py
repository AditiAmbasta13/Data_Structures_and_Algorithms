# Fibonacci Numbers
# n = 8
# dp = list(range(n+1))
# dp[0] = 0
# dp[1] = 0
# dp[2] = 1
# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])

#Minimum number of squares needed whose sum is n
# n = 26
# dp = [float('inf')] * (n + 1)
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# for i in range(1, int(n**0.5) + 1):
#     for j in range(n - i * i + 1):
#         dp[i * i + j] = min(dp[i * i + j], 1 + dp[j])
# print(dp[n])

#Coin Change Problem - No. of ways
# def coin_change_ways_2d(amount, coins):
#     dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
#     for i in range(len(coins) + 1):
#         dp[i][0] = 1
    
#     for i in range(1, len(coins) + 1):
#         for j in range(1, amount + 1):
#             dp[i][j] = dp[i-1][j] 
#             if j >= coins[i-1]:
#                 dp[i][j] += dp[i][j - coins[i-1]]  
#     return dp[len(coins)][amount]

# amount = 5
# coins = [1, 2, 5]
# print(f"The number of ways to make the amount {amount} is {coin_change_ways_2d(amount, coins)}.")

#0-1 Knapsack
# def knapsack_2d(weights, values, capacity):
#     n = len(weights)
#     dp = [[0] * (capacity + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, capacity + 1):
#             if weights[i-1] <= j:
#                 dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - weights[i-1]])
#             else:
#                 dp[i][j] = dp[i-1][j]
    
#     return dp[n][capacity]

# weights = [1, 3, 4, 5]
# values = [1, 4, 5, 7]
# capacity = 7
# print(f"The maximum value that can be obtained is {knapsack_2d(weights, values, capacity)}.")

#Longest Increasing Subsequence - Dynamic Programming
# def length_of_lis(nums):
#     if not nums:
#         return 0
    
#     n = len(nums)
#     dp = [1] * n
    
#     for i in range(1, n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
    
#     return max(dp)

# # Example usage:
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# print(f"The length of the longest increasing subsequence is {length_of_lis(nums)}.")

#Longest Common Subsequence - Dynamic Programming
# def longest_common_subsequence(X, Y):
#     m = len(X)
#     n = len(Y)
    
#     # Create a 2D array to store lengths of longest common subsequence.
#     L = [[0] * (n + 1) for _ in range(m + 1)]
    
#     # Fill the L array according to the rules described.
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if X[i - 1] == Y[j - 1]:
#                 L[i][j] = L[i - 1][j - 1] + 1
#             else:
#                 L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
#     # L[m][n] contains the length of LCS.
#     return L[m][n]

# # Example usage
# X = "ABCBDAB"
# Y = "BDCAB"
# print("Length of Longest Common Subsequence:", longest_common_subsequence(X, Y))

#Matrix Chain Multiplication - Dynamic Programming
# def matrix_chain_order(p):
#     n = len(p) - 1  # Number of matrices is len(p) - 1
#     # m[i][j] will be the minimum number of multiplications needed to compute A_i x A_{i+1} x ... x A_j
#     m = [[0] * n for _ in range(n)]
#     # s[i][j] will be the index of the matrix after which the optimal split occurs
#     s = [[0] * n for _ in range(n)]

#     for length in range(2, n + 1):  # length of the chain
#         for i in range(n - length + 1):
#             j = i + length - 1
#             m[i][j] = float('inf')
#             for k in range(i, j):
#                 q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
#                 if q < m[i][j]:
#                     m[i][j] = q
#                     s[i][j] = k

#     return m, s

# p = [10, 20, 30, 40, 30]  # Dimensions of matrices (p_0 x p_1), (p_1 x p_2), (p_2 x p_3), (p_3 x p_4)
# m, s = matrix_chain_order(p)
# print("Minimum number of multiplications:", m[0][len(p) - 2])

#Minimum Jumps to Reach End - Dynamic Programming
# def min_jumps(arr):
#     n = len(arr)
#     if n == 0 or arr[0] == 0:
#         return float('inf')  # If the first element is 0 or array is empty, return infinity

#     # dp[i] will hold the minimum number of jumps to reach index i
#     dp = [float('inf')] * n
#     dp[0] = 0  # Starting point requires 0 jumps

#     for i in range(1, n):
#         for j in range(i):
#             if j + arr[j] >= i and dp[j] != float('inf'):
#                 dp[i] = min(dp[i], dp[j] + 1)
#                 break  # No need to check further once we find a valid jump

#     return dp[-1] if dp[-1] != float('inf') else -1

# # Example usage
# arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
# print("Minimum number of jumps required:", min_jumps(arr))

#Optimal Game Strategy - Dynamic Programming
# a = [1,2,3,4]
# n = 4
# dp = [[-1]*100]*100
# def solve(i, j):
#     if i == j:
#         return a[i]
#     if i > j:
#         return 0
#     if dp[i][j] != -1:
#         return dp[i][j]
#     l = a[i] + min(solve(i+2, j), solve(i+1, j-1))
#     r = a[j] + min(solve(i, j-2), solve(i+1, j-1))
#     dp[i][j] = max(l, r)
#     return dp[i][j]

# print(solve(0, n-1))

#Number of Subsequences
# s = "ac?b?c"
# e, a, ab, abc = 1, 0, 0, 0
# n = 6
# for i in range(n):
#     if s[i] == 'a':
#         a += e
#     elif s[i] == "b":
#         ab += a
#     elif s[i] == "c":
#         abc += ab
#     elif s[i] == "?":
#         abc = 3*abc + ab
#         ab = 3*ab + a
#         a = 3*a + e
# print(abc)

#Count Number of Binary Strings w/o cons 1 - Dynamic Programming
# n = 5
# fib = [0]*(n+2)
# fib[0] = 0
# fib[1] = 1
# for i in range(2, n+2):
#     fib[i] = fib[i-1] + fib[i-2]
# print(fib[n+1])

#0-N Knapsack - Dynamic Programming
# W = 11
# n = 5
# wt = [3,2,4,5,1]
# val = [4,3,5,6,1]
# dp = [0]*(W+1)
# for j in range(W+1):
#     for i in range(n):
#         if j - wt[i] >= 0:
#             dp[j] = max(dp[j], val[i]+dp[j-wt[i]])
# print(dp[W])

#Kadane Algorithm - Dynamic Programming
# def kadane_algorithm(arr):
#     if not arr:
#         return 0
    
#     max_ending_here = max_so_far = arr[0]
    
#     for num in arr[1:]:
#         max_ending_here += num
#         max_so_far = max(max_so_far, max_ending_here)
#         if max_ending_here < 0:
#             max_ending_here = 0
    
#     return max_so_far
# arr = [-5, -1, 5, -3, -1, 2, 3, -6]
# print("Maximum sum of contiguous subarray:", kadane_algorithm(arr))

#Maximum Length of Bitonic Subsequence - Dynamic Programming
# def bitonic(nums):
#     if not nums:
#         return 0
    
#     n = len(nums)
#     f = [1] * n
#     b = [1] * n
    
#     for i in range(n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 f[i] = max(f[i], f[j] + 1)
    
#     for i in range(n-1, -1, -1):
#         for j in range(n-1, i-1, -1):
#             if nums[i] > nums[j]:
#                 b[i] = max(b[i], b[j] + 1)

#     ans = 0
#     for i in range(n):
#         ans = max(ans, f[i]+b[i]-1)

#     return ans

# nums = [1,11,2,10,4,5,2,1]
# print(bitonic(nums))

#Friends Paring Problem - Dynamic Programming
# def countFriendsPairings(n):
#     dp = [0] * (n + 1)
    
#     # base cases
#     dp[0] = 1
#     dp[1] = 1
    
#     for i in range(2, n + 1):
#         dp[i] = dp[i-1] + (i-1) * dp[i-2]
    
#     return dp[n]

# # Test the function
# n = 3
# print(f"Number of ways for {n} friends:", countFriendsPairings(n))

#Ugly Numbers - Dynamic Programming
# def nthUglyNumber(n):
#     ugly = [1]*n
#     i2, i3, i5 = 0, 0, 0
    
#     for i in range(1, n):
#         next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
#         ugly[i] = next_ugly
        
#         if next_ugly == ugly[i2] * 2:
#             i2 += 1
#         if next_ugly == ugly[i3] * 3:
#             i3 += 1
#         if next_ugly == ugly[i5] * 5:
#             i5 += 1
    
#     return ugly[-1]

# # Test the function
# n = 10
# print(f"The {n}th ugly number is:", nthUglyNumber(n))

#LCS in 3 strings
# def LCS(s1, s2, s3):
#     l, m, n = len(s1), len(s2), len(s3)
    
#     # Initialize the 3D DP table with -1
#     dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l+1)]
    
#     def lcs_helper(i, j, k):
#         # Base case
#         if i == 0 or j == 0 or k == 0:
#             return 0
        
#         # If already computed, return the stored value
#         if dp[i][j][k] != -1:
#             return dp[i][j][k]
        
#         # If characters match
#         if s1[i-1] == s2[j-1] == s3[k-1]:
#             dp[i][j][k] = 1 + lcs_helper(i-1, j-1, k-1)
#         else:
#             # If characters don't match, try all possibilities
#             dp[i][j][k] = max(lcs_helper(i-1, j, k),
#                               lcs_helper(i, j-1, k),
#                               lcs_helper(i, j, k-1))
        
#         return dp[i][j][k]
    
#     return lcs_helper(l, m, n)

# # Example usage
# s1 = "AGGT12"
# s2 = "12TXAYB"
# s3 = "12XBA"

# result = LCS(s1, s2, s3)
# print(f"Length of LCS is {result}")

#K-Ordered LCS - Dynamic Programming
# def k_ordered_lcs(A, B, k):
#     m, n = len(A), len(B)
    
#     # Initialize 3D DP table with -1
#     dp = [[[-1 for _ in range(k+1)] for _ in range(n+1)] for _ in range(m+1)]
    
#     def lcs_helper(i, j, p):
#         # Base cases
#         if i == 0 or j == 0:
#             return 0
#         if p < 0:
#             return 0
        
#         # If already computed, return the stored value
#         if dp[i][j][p] != -1:
#             return dp[i][j][p]
        
#         # If characters match
#         if A[i-1] == B[j-1]:
#             dp[i][j][p] = 1 + lcs_helper(i-1, j-1, p)
#         else:
#             # Try without changing
#             dp[i][j][p] = max(lcs_helper(i-1, j, p), lcs_helper(i, j-1, p))
            
#             # Try changing if we have changes left
#             if p > 0:
#                 dp[i][j][p] = max(dp[i][j][p], 1 + lcs_helper(i-1, j-1, p-1))
        
#         return dp[i][j][p]
    
#     return lcs_helper(m, n, k)

# # Test the function
# A = "abcde"
# B = "acfde"
# k = 1
# print(f"Length of {k}-Ordered LCS is {k_ordered_lcs(A, B, k)}")
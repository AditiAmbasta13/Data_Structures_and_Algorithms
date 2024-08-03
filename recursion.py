#check if an array is sorted or not
# a = [1, 2, 3, 7, 5, 6]
# n = len(a)
# def check_sort(a, n):
#     if n == 1:
#         return True 
#     restarr = check_sort(a[1:], n-1)
#     return (a[0] < a[1] and restarr)
# print(check_sort(a,n))

#print nums till n decreasing
# n = 5
# def dec(n):
#     if n == 0:
#         return
#     print(n)
#     dec(n-1)
# dec(n)
#print nums till n increasing
# n = 5
# def inc(n):
#     if n == 0:
#         return
#     inc(n-1)
#     print(n)
# inc(n)

#find first occurence of a num
# a = [2, 9, 3, 1, 5, 6]
# n = len(a)
# def firstocc(a, i, n, k):
#     if i == n:
#         return False
#     if a[i] == k:
#         return i
#     return firstocc(a, i+1, n, k)
# print(firstocc(a, 0, n, 1))
#find last occurence of a num
# a = [2, 1, 3, 5, 1, 6]
# n = len(a)
# def lastocc(a, i, n, k):
#     if i == n:
#         return False
#     if a[i] == k:
#         return n - i
#     return lastocc(a, i-1, n, k)
# print(lastocc(a, n-1, n, 1))

#reverse string using recursion
# a = "ambasta"
# n = len(a)
# def revs(a, i, n):
#     if i == n:
#         return
#     revs(a, i+1, n)
#     print(a[i], end='')
# revs(a, 0, n)
#reverse string using recursion
# a = "ambasta"
# def revs(a):
#     if len(a) == 0:
#         return
#     new = a[1:]
#     revs(new)
#     print(a[0], end="")
# revs(a)

#Replace "pi" with "3.14"
# a = "piabcdpipibcdefpicdef"
# def repla(a):
#     if len(a) == 0:
#         return
#     if a[0] == 'p' and a[1] == 'i':
#         print("3.14",end="")
#         repla(a[2:])
#     else:
#         print(a[0],end="")
#         repla(a[1:])
# repla(a)

#Tower Of Hanaoi
# def toh(n, src, dest, helper):
#     if n == 0:
#         return
#     toh(n-1, src, helper, dest)
#     print(f"Move from {src} to {dest}")
#     toh(n-1, helper, dest, src)
# toh(3, 'A', 'C', 'B')

#Remove all duplicates from string
# a = "aaaabbccccddeeeee"
# def remodup(a):
#     if len(a) == 0:
#         return ""
#     ch = a[0]
#     if len(a) == 1:
#         return ch
#     new = remodup(a[1:])
#     if ch == new[0]:
#         return new
#     return ch + new
# print(remodup(a))

#Move all x to the end of string
# a = "axbxcdefxxeh"
# def movex(a):
#     if len(a) == 0:
#         return ""
#     ch = a[0]
#     new = movex(a[1:])
#     if ch == 'x':
#         return new+ch
#     return ch+new
# print(movex(a))

#Print all substring of a string
# a ="abc"
# def substri(a, ans):
#     if len(a) == 0:
#         print(ans)
#         return
#     ch = a[0]
#     ros = a[1:]
#     substri(ros, ans)
#     substri(ros, ans+ch)
# substri(a, "")

#Generate substring with ASCII
# a ="AB"
# def subasc(a, ans):
#     if len(a) == 0:
#         print(ans)
#         return
#     ch = a[0]
#     code = ord(ch)
#     ros = a[1:]
#     subasc(ros, ans)
#     subasc(ros, ans+ch)
#     subasc(ros, ans+str(code))
# subasc(a, "")

#Print all possible words from phone digits
# keyarr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
# a = "23"
# def keypad(a, ans, keyarr):
#     if len(a) == 0:
#         print(ans)
#         return
#     ch = a[0]
#     code = keyarr[int(ch)]
#     ros = a[1:]
#     for i in range(len(code)):
#         keypad(ros, ans + code[i], keyarr)
# keypad(a, "", keyarr)

#Print all permutations of a string
# a = "ABC"
# def permute(a, ans):
#     if len(a) == 0:
#         print(ans)
#         return
#     for i in range(len(a)):
#         ch  = a[i]
#         ros = a[0:i]+a[i+1:]
#         permute(ros, ans+ch)
# permute(a, "")

#Number of Paths possible from start point to end point in a gameboard
# def countPath(s, e):
#     if s == e:
#         return True
#     if s > e:
#         return False
#     count = 0
#     for i in range(1, 6): #dice 1 - 6
#         count += countPath(s+i, e)
#     return count
# print(countPath(0, 3))

#Count all possible paths in a maze/matrix - all paths from 0, 0 to n-1, n-1
# def allPaths(n, i, j):
#     if i == n-1 and j == n-1:
#         return 1
#     if i >= n or j >=n:
#         return 0
#     return allPaths(n, i+1, j) + allPaths(n, i, j+1)
# print(allPaths(3, 0, 0))

#2 x n Tile-ing problem
# def tiling(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return tiling(n-1) + tiling(n-2)
# print(tiling(4))

#Friends Pairing Problem
# def friendPairing(n):
#     if n == 0 or n == 1 or n == 2:
#         return n
#     return friendPairing(n-1) + friendPairing(n-2)*(n-1)
# print(friendPairing(4))

#0/1 Knapsack using recursion
# wt = [10, 20, 30]
# value = [100, 50, 150]
# W = 50
# n = len(value)
# def knapsack(value, wt, n, W):
#     if n == 0 or W == 0:
#         return 0
#     if wt[n-1] > W:
#         return knapsack(value, wt, n-1, W)
#     return max(knapsack(value, wt, n-1, W-wt[n-1])+value[n-1], knapsack(value, wt, n-1, W))
# print(knapsack(value, wt, n, W))
import math

#1. prime number
# n = 7
# def isPrime(n):
#     flag = 0
#     sqroot = int(math.sqrt(n))
#     for i in range(2, sqroot+1):
#         if n % i == 0:
#             flag = 1
#     if flag == 0:
#         return True
#     else:
#         return False
#2. Reverse number
# n = 173
# rev = 0
# while (n > 0):
#     dig = n%10
#     rev = (rev * 10) + dig
#     n = n//10
# print(rev)
# 3. Prime no.s in a range
# a = 4
# b = 10
# p = []
# for i in range(a, b+1):
#     if isPrime(i):
#         print(i, end=" ")
#4.Armstrong nums
# n = 153
# a = n
# sum = 0
# while (n > 0):
#     dig = n%10
#     sum += pow(dig, 3)
#     n = n//10
# print("Arm") if sum == a else print("No")
#5. Fibonacci Series
# a = 0
# b = 1
# n = 10
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#6. Factorial
# n = 5
# def fact(n):
#     m = 1
#     for i in range(2,n+1):
#         m *= i
#     return m
#7.nCr
# n = 5
# r = 2
# def ncr(n, r):
#     return (fact(n)//(fact(n-r)*fact(r)))
#8. Pascals Triangle
# n = 5
# for i in range(0, n):
#     for j in range(0, i+1):
#         print(ncr(i,j), end=' ')
#     print(" ")
#9. Sum of n natural nos
# n = 3
# print((n*(n+1))//2)
#10. Check Pythagorean triplet
# x, y, z = 3, 4, 5
# a = max(x, max(y, z))
# if a == x:
#     b, c = y, z
# elif a == y:
#     b, c = x, z
# else:
#     b, c = x, y
# if a*a == (b*b) + (c*c):
#     print("Yes")
# else:
#     print("No")

#sieve of eratosthenes - prime numbers between a range
# n = 10
# prime = [0 for _ in range(n)]
# for i in range(2, n):
#     if prime[i] == 0:
#         for j in range(i*i, n, i):
#             prime[j] = 1
# for i in range(2, n):
#     if prime[i] == 0:
#         print(i, end=" ")

#prime factorization using sieve
# n = 20
# spf = [0 for _ in range(n + 1)] 
# for i in range(2, n + 1):
#     spf[i] = i
# for i in range(2, int(n**0.5) + 1):
#     if spf[i] == i:  
#         for j in range(i * i, n + 1, i):
#             if spf[j] == j:  
#                 spf[j] = i
# factor = n
# factors = []
# while factor != 1:
#     factors.append(spf[factor])
#     factor //= spf[factor]
# print(" ".join(map(str, factors)))


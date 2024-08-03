#1. Binary to decimal
# n = 101
# x = 1
# ans = 0
# while(n > 0):
#     dig = n%10
#     ans+= dig * x
#     x *= 2
#     n = n//10
# print(ans)
#2. Octal to decimal
# n = 101
# x = 1
# ans = 0
# while(n > 0):
#     dig = n%10
#     ans+= dig * x
#     x *= 8
#     n = n//10
# print(ans)
#3. Hexadecimal to decimal
# n = "ABC"
# s = len(n)
# x = 1
# ans = 0
# for i in range(s-1, -1, -1):
#     if n[i] >= '0' and n[i] <= '9':
#         ans += x * (ord(n[i]) - ord('0'))
#     else:
#         ans += x * (ord(n[i]) - ord('A') + 10)
#     x *= 16
# print(ans)
#4. Decimal to Binary
# n = 4
# s = []
# while(n > 0):
#     s.append(n%2)
#     n = n//2
# print(s[::-1])
#5. Decimal to Octal
# n = 149
# s = []
# while(n > 0):
#     s.append(n%8)
#     n = n//8
# print(s[::-1])
#6. Decimal to Hexadecimal
# n = 42
# s = []
# while n > 0:
#     rem = n % 16
#     if rem < 10:
#         s.append(str(rem))
#     else:
#         s.append(chr(rem - 10 + ord('A')))
#     n = n // 16

# ans = ''.join(s[::-1])
# print(ans)
#7. Add to binary nums
# a = 110101
# b = 1101
# ans = 0
# p = 0
# place = 1

# while a > 0 or b > 0 or p > 0:
#     a_bit = a % 10
#     b_bit = b % 10

#     sum_bits = a_bit + b_bit + p
#     if sum_bits == 0:
#         ans += 0 * place
#         p = 0
#     elif sum_bits == 1:
#         ans += 1 * place
#         p = 0
#     elif sum_bits == 2:
#         ans += 0 * place
#         p = 1
#     else:
#         ans += 1 * place
#         p = 1

#     a = a // 10
#     b = b // 10
#     place *= 10

# print(ans)

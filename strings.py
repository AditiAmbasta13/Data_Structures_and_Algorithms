#Palindrome
# w = "rotator"
# n = len(w)
# for i in range(n):
#     if w[i] != w[n - i - 1]:
#         print("Not Palindrome")
# else:
#     print("Palindrome")

#Largest word in a sentence
# a = "Hi I am Aditi Ambasta"
# maxl = 0
# currl = 0
# st, maxst = 0, 0
# for i in range(len(a)):
#     if a[i] == ' ':
#         if currl > maxl:
#             maxl = currl
#             maxst = st
#         currl = 0
#         st = i + 1
#     else:
#         currl += 1
# if currl > maxl:
#     maxl = currl
#     maxst = st
# for i in range(maxl):
#     print(a[i + maxst], end="")

# Convert lowercase to uppercase
# def up(s):
#     upper_s = ""
#     for i in s:
#         if 'a' <= i <= 'z':
#             upper_s += chr(ord(i) - 32)
#         else:
#             upper_s += i
#     print(upper_s)
# up("aditi")
# Convert uppercase to lowercase
# def low(s):
#     lower_s = ""
#     for i in s:
#         if 'A' <= i <= 'Z':
#             lower_s += chr(ord(i) + 32)
#         else:
#             lower_s += i
#     print(lower_s)
# low("ADITI")

#Biggest number from numeric string
# n = "45629027"
# m = sorted(n)
# print(''.join(m[::-1]))

#Max frequency in string
# from collections import defaultdict
# s = "aaabcdadcca"
# d = defaultdict(int)
# for i in s:
#     d[i] += 1
# max_char = max(d, key=d.get)
# max_freq = d[max_char]
# print(f"Character with max frequency: {max_char}")
# print(f"Frequency: {max_freq}")
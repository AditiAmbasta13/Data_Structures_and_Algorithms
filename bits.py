#Get Bit
# def getbit(n, pos):
#     return (n & (1<<pos))!=0
# print(getbit(1001001, 4))

#Set Bit
# def setBit(n, pos):
#     return n | (1 << pos)
# n = 0b1001001  
# pos = 2
# result = setBit(n, pos)
# print(bin(result))  

#Clear Bit
# def clearbit(n, pos):
#     mask = ~(1 << pos)
#     return (n & mask)
# n = 0b1001111  
# pos = 2
# result = clearbit(n, pos)
# print(bin(result)) 

#Update Bit
# def updatebit(n, pos, value):
#     mask = ~(1 << pos)
#     n = n & mask
#     return (n | (value << pos))
# n = 0b1001111  
# pos = 5
# result = updatebit(n, pos, 1)
# print(bin(result))  

#Check if given num is a power of 2
# def pow2(n):
#     return n and not (n & n-1)
# print(pow2(16))

#count 1s in binary digit
# n = 0b101101
# count = 0
# while(n):
#     n = n & n-1
#     count += 1
# print(count)

#Generate all possible subsets of a set
# a = ["a", "b", "c"]
# n = len(a)
# all_subsets = []
# for i in range(1 << n):  # 2**n
#     subset = []
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(a[j])
#     all_subsets.append(subset)
# for subset in all_subsets:
#     print(subset)

#Find unique num in arr where all nums are present twice except one
# a = [2, 4, 4, 5, 5]
# xorsum = 0
# for i in range(len(a)):
#     xorsum = xorsum ^ a[i]
# print(xorsum)

#Find unique num in arr where all nums are present twice except two
# a = [2, 4, 4, 5, 5, 7]
# xorsum = 0
# for i in range(len(a)):
#     xorsum = xorsum ^ a[i]
# tempxor = xorsum
# setbit = 0
# pos = 0
# while(setbit != 1):
#     setbit = xorsum & 1 #get last digit
#     xorsum = xorsum >> 1
#     pos+=1
# newxor = 0
# for i in range(len(a)):
#     if (getbit(a[i], pos-1)):
#         newxor = newxor ^ a[i]
# print(newxor)
# print(tempxor ^ newxor)

#Find unique num in arr where all nums are present thrice except one
# a = [1,1,1,2,2,2,3,3,3,4]
# result = 0
# for i in range(64):
#     sum = 0
#     for j in range(len(a)):
#         if(getbit(a[j], i)):
#             sum += 1
#     if sum%3 != 0:
#         result = setBit(result, i)
# print(result)
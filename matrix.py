#spiral order matrix traversal
# m = [[1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]]
# rs, cs = 0, 0
# re, ce = len(m)-1, len(m[0])-1
# while(rs <= re and cs <= ce):
#     for i in range(cs, ce+1):
#         print(m[rs][i], end=" ")
#     rs += 1
#     for i in range(rs, re+1):
#         print(m[i][ce], end=" ")
#     ce -= 1
#     for i in range(ce, cs-1, -1):
#         print(m[re][i], end=" ")
#     re -= 1
#     for i in range(re, rs-1, -1):
#         print(m[i][cs], end=" ")
#     cs += 1

#matrix multiplication
# a = [[1, 2, 3],
#     [6, 7, 8],
#     [11, 12, 13]]
# b = [[1, 2, 3],
#     [6, 7, 8],
#     [11, 12, 13]]
# ans = [[0, 0, 0],
#        [0, 0, 0],
#        [0, 0, 0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         for k in range(len(a[0])):
#             ans[i][j] += a[i][k] * b[k][j]
# print(ans)

#matrix transpose
# a = [[1, 2, 3],
#     [6, 7, 8],
#     [11, 12, 13]]
# for i in range(len(a)):
#     for j in range(i, len(a[0])):
#         a[i][j], a[j][i] = a[j][i], a[i][j]
# print(a)

#matrix search
# m = [[1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]]
# target = 13
# n = len(m)
# r, c = 0, len(m[0])-1
# while( r < n and c >= 0):
#     if m[r][c] == target:
#         print("Found")
#         break
#     elif m[r][c] > target:
#         c -= 1
#     else:
#         r += 1
# else:
#     print("Not found")
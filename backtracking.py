#Rat in a maze
# n = 5
# arr = [[1, 0, 1, 0, 1],
#        [1, 1, 1, 1, 1],
#        [0, 1, 0, 1, 0],
#        [1, 0, 0, 1, 1],
#        [1, 1, 1, 0, 1]]
# solarr = [[0]*n for _ in range(n)]
# def isSafe(arr, x, y, n):
#     if x<n and y<n and arr[x][y] == 1:
#         return True
#     return False
# def ratInAMaze(arr, x, y, n, solarr):
#     if x == n-1 and y == n-1:
#         solarr[x][y] = 1
#         return True
#     if isSafe(arr, x, y, n):
#         solarr[x][y] = 1
#         if ratInAMaze(arr, x+1, y, n, solarr):
#             return True
#         if ratInAMaze(arr, x, y+1, n, solarr):
#             return True
#         solarr[x][y] = 0
#         return False
#     return False
# if ratInAMaze(arr, 0, 0, n, solarr):
#     print(solarr)
# else:
#     print("Path not found")

#NQueen
# def isSafe(board, r, c, n):
#     for row in range(n):
#         if board[row][c] == 1:
#             return False
#     row = r
#     col = c
#     while(row>=0 and col>=0):
#         if board[row][col] == 1:
#             return False
#         row -= 1
#         col -= 1
#     row = r
#     col = c
#     while(row>=0 and col<n):
#         if board[row][col] == 1:
#             return False
#         row -= 1
#         col += 1
#     return True
# def nQueen(board, r, n):
#     if r >= n:
#         return True
#     for col in range(n):
#         if isSafe(board, r, col, n):
#             board[r][col] = 1  
#             if nQueen(board, r+1, n):
#                 return True
#             board[r][col] = 0
#     return False
# n = 4
# board = [[0]*n for _ in range(n)]
# if(nQueen(board, 0, n)):
#     for row in board:
#         print(row)
# else:
#     print("Not possible")


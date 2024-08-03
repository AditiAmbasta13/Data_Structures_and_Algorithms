#array with distinct integers permute unique integers
# a = [1, 2, 3]
# ans = []
# def permute(a, idx):
#     if idx == len(a):
#         ans.append(a[:])  # Append a copy of the list
#         return
#     for i in range(idx, len(a)):
#         a[i], a[idx] = a[idx], a[i]
#         permute(a, idx+1)
#         a[i], a[idx] = a[idx], a[i]  # Backtrack
# permute(a, 0)
# print(ans)

#array with duplicate integers permute unique integers
# a = [1, 2, 2]
# a.sort()
# ans = []
# def permute(a, idx):
#     if idx == len(a):
#         ans.append(a[:])
#         return
#     seen = set() 
#     for i in range(idx, len(a)):
#         if a[i] in seen:
#             continue
#         seen.add(a[i])
#         a[i], a[idx] = a[idx], a[i]
#         permute(a, idx + 1)
#         a[i], a[idx] = a[idx], a[i] 
# permute(a, 0)
# print(ans)

def nextPermutation( nums):
    n = len(nums)
    if not nums:
        return []

    ans = []
    def helper(idx):
        if idx == n:
            ans.append(nums[:])
            return
        for i in range(idx, n):
            nums[i], nums[idx] = nums[idx], nums[i]
            helper(idx+1)
            nums[i], nums[idx] = nums[idx], nums[i]

    helper(0)
    return ans

nextPermutation()
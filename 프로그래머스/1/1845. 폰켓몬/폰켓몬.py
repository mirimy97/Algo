from collections import Counter
def solution(nums):
    cnts = dict()
    N = len(nums)
    for num in nums:
        if num in cnts:
            cnts[num] += 1
        else:
            cnts[num] = 1
    return min(N/2, len(cnts))
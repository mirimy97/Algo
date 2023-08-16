import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
answer = set()
for i in combinations(nums, M):
    answer.add(i)
for arr in sorted(list(answer)):
    print(*arr)
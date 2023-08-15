import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
memo = [0]
for a in arr:
    if memo[-1] < a:
        memo.append(a)
    else:
        memo[bisect_left(memo, a)] = a

print(len(memo) - 1)
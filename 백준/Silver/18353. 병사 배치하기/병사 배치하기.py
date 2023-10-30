import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]
for a in arr[::-1]:
    if dp[-1] < a:
        dp.append(a)
    else:
        dp[bisect_left(dp, a)] = a
print(N - (len(dp) - 1))
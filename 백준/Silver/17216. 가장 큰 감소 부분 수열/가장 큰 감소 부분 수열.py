import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [A[0]]

for i in range(1, N):
    max_sum = A[i]
    for j in range(i):
        if A[j] > A[i]:
            max_sum = max(max_sum, dp[j] + A[i])
    dp.append(max_sum)

print(max(dp))
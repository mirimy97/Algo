import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]
dp[0][nums[0]] = 1
for i in range(1, N - 1):
    for j in range(0, 21):
        if dp[i - 1][j]:
            if 0 <= j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i - 1][j]
            if 0 <= j - nums[i] <= 20:
                dp[i][j - nums[i]] += dp[i - 1][j]
print(dp[N - 2][nums[-1]])
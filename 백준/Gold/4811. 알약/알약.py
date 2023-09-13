import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
dp[0][0] = 1

for w in range(30):
    for h in range(30):
        if h > 0:
            dp[w + 1][h - 1] += dp[w][h]
        dp[w][h + 1] += dp[w][h]
dp[30][0] += 1
while 1:
    n = int(input())
    if not n:
        break

    print(dp[n][0])
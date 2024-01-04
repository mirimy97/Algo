import sys
input = sys.stdin.readline

N, K = map(int, input().split())
T = [0]  # 시간
V = [0]  # 중요도
for i in range(K):
    v, t = map(int, input().split())
    T.append(t)
    V.append(v)

dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(1, K + 1):
    for j in range(1, N + 1):
        if j >= T[i]:    # dp table에서 고른 강의 이상의 시간
            dp[i][j] = max(dp[i - 1][j], V[i] + dp[i - 1][j - T[i]])   # 추가 x , o
        else:    # (이 강의 추가 불가능)
            dp[i][j] = dp[i - 1][j]

print(dp[K][N])

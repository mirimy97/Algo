import sys
input = sys.stdin.readline

N = int(input())
cost = [0] * N
for i in range(N):
    cost[i] = list(map(int, input().split()))
min_value = 1000 * N
for c in range(3):
    memo = [[1000 * N] * 3] + [[0] * 3 for _ in range(N-1)]
    memo[0][c] = cost[0][c]
    for i in range(1, N):
        memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + cost[i][0]
        memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + cost[i][1]
        memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + cost[i][2]
    for j in range(3):
        if j != c:
            min_value = min(min_value, memo[N-1][j])
print(min_value)
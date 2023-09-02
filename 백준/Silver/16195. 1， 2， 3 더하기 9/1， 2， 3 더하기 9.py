import sys
input = sys.stdin.readline

memo = [[0] * 1001 for _ in range(1001)]
memo[1][1] = 1
memo[2][1] = 1
memo[2][2] = 1
memo[3][1] = 1
memo[3][2] = 2
memo[3][3] = 1
for i in range(4, 1001):
    for j in range(1, i + 1):
        memo[i][j] = (memo[i - 1][j - 1] + memo[i - 2][j - 1] + memo[i - 3][j - 1]) % 1000000009

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(sum(memo[n][:m + 1]) % 1000000009)
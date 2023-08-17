import sys
input = sys.stdin.readline

N = int(input())
nodes = input()
map= {'B':'O', 'O':'J', 'J':'B'}
dp = [1000000] * N
dp[0] = 0
for i in range(1, N):
    for j in range(i, -1, -1):
        if map[nodes[j]] == nodes[i]:
            dp[i] = min(dp[i], dp[j] + ((i - j) ** 2))
if dp[-1] == 1000000:
    print(-1)
else:
    print(dp[-1])
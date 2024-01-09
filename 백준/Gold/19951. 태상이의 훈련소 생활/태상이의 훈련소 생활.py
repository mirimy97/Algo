import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 연병장 [] N칸, 조교 M명
H = [0] + list(map(int, input().split()))
memo = [0] * (N + 2)
for _ in range(M):
    a, b, k = map(int, input().split())
    memo[a] += k
    memo[b + 1] -= k
for i in range(1, N + 1):
    memo[i] += memo[i - 1]
for i in range(1, N + 1):
    print(H[i] + memo[i], end=" ")
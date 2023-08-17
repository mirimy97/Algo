import sys
from collections import deque
input = sys.stdin.readline

def node_input(n):
    return int(n) - 1

N, M = map(int, input().split())
Si, Sj = map(node_input, input().split())
E = [0] * M
for i in range(M):
    E[i] = list(map(node_input, input().split()))
D = [(-2, -1), (-2, 1), (-1, -2), (-1, +2), (1, -2), (1, 2), (2, -1), (2, 1)]
q = deque([[Si, Sj]])
v = [[0] * N for _ in range(N)]
v[Si][Sj] = 1
while q:
    si, sj = q.popleft()
    for di, dj in D:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:
            v[ni][nj] = v[si][sj] + 1
            q.append([ni, nj])
for Ei, Ej in E:
    print(v[Ei][Ej] - 1, end=" ")
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
E = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            E.append((i, j))
D = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
memo = [[2500] * M for _ in range(N)]
for Si, Sj in E:
    v = [[0] * M for _ in range(N)]
    v[Si][Sj] = 1
    q = deque([[Si, Sj]])
    while q:
        si, sj = q.popleft()
        for di, dj in D:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                v[ni][nj] = v[si][sj] + 1
                q.append([ni, nj])
    for i in range(N):
        for j in range(M):
            memo[i][j] = min(memo[i][j], v[i][j] - 1)
answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, memo[i][j])
print(answer)
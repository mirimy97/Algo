import sys
from collections import deque
N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
S = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            S.append((i, j))
answer = 0
D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for Si, Sj in S:
    v = [[0] * M for _ in range(N)]
    q = deque([[Si, Sj]])
    v[Si][Sj] = 1
    while q:
        si, sj = q.popleft()
        for di, dj in D:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and arr[ni][nj] == 'L':
                q.append([ni, nj])
                v[ni][nj] = v[si][sj] + 1
    for i in range(N):
        for j in range(M):
            answer = max(answer, v[i][j] - 1)
print(answer)
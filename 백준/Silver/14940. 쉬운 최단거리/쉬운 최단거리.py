import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
Si, Sj = -1, -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            Si, Sj = i, j
            break
    if Sj != -1:
        break
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque([[Si, Sj]])
v = [[0] * m for _ in range(n)]
while q:
    si, sj = q.popleft()
    for di, dj in d:
        ni, nj = si + di, sj + dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and not v[ni][nj]:
            q.append([ni, nj])
            v[ni][nj] = v[si][sj] + 1
for i in range(n):
    for j in range(m):
        if v[i][j] == 0 and arr[i][j] == 1:
            v[i][j] = -1
for i in v:
    print(*i)
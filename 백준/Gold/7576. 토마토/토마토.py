import sys
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque()
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1
if not q:
    maxD = -1
else:
    maxD = 0
    while True:
        si, sj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1 and (not visited[ni][nj] or visited[ni][nj] > visited[ni][nj] + 1):
                visited[ni][nj] = visited[si][sj] + 1
                q.append((ni, nj))
                if visited[ni][nj] - 1 > maxD:
                    maxD = visited[ni][nj] - 1

        if not q:
            break
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] == 0:
                maxD = -1
print(maxD)
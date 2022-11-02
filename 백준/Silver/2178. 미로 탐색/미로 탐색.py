import sys
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

q = deque()
visited = [[-1] * M for _ in range(N)]
si, sj = 0, 0
visited[si][sj] = 1

while visited[N-1][M-1] == -1:
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1 and arr[ni][nj]:
            q.append([ni, nj])
            visited[ni][nj] = visited[si][sj] + 1

    if q:
        si, sj = q.popleft()
    else:
        break
print(visited[N-1][M-1])

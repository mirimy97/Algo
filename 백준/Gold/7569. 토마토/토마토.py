import sys
from collections import deque

def max_date(v):
    max_d = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if v[h][i][j] == 0:
                    return -1
                elif v[h][i][j] - 1 > max_d:
                    max_d = v[h][i][j] - 1
    return max_d


M, N, H = map(int, input().split())
arr =[[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

q = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
d = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append((h, i, j))
                visited[h][i][j] = 1
            elif arr[h][i][j] == -1:
                visited[h][i][j] = 1

while q:
    sh, si, sj = q.popleft()
    for dh, di, dj in d:
        nh, ni, nj = sh + dh, si + di, sj + dj
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0 and not visited[nh][ni][nj]:
            visited[nh][ni][nj] = visited[sh][si][sj] + 1
            q.append((nh, ni, nj))
print(max_date(visited))
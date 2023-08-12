import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
exist = True
cnt = 0
while exist:
    cnt += 1
    v = [[0] * M for _ in range(N)]
    q = deque([[0, 0]])
    while q:
        si, sj = q.popleft()
        for di, dj in d:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not arr[ni][nj] and not v[ni][nj]:
                    q.append([ni, nj])
                    v[ni][nj] = 1
                elif arr[ni][nj]:
                    v[ni][nj] += 1
    exist = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if v[i][j] >= 2:
                    arr[i][j] = 0
                else:
                    exist = True

print(cnt)
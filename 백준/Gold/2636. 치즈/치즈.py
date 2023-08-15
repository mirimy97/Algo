import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cnt += 1
time, pre_cnt = 0, 0
while cnt:
    pre_cnt = cnt
    time += 1
    v = [[0] * M for _ in range(N)]
    q = deque([[0, 0]])
    # 치즈가 공기에 닿는 면적 count -> v[i][j] 가 0이 아닐 때
    while q:
        si, sj = q.popleft()
        for di, dj in d:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not v[ni][nj]:
                    if not arr[ni][nj]:
                        q.append([ni, nj])
                    v[ni][nj] = 1
    # 녹은 치즈 없애기, 다음 반복 필요한지? -> exist
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if v[i][j] == 1:
                    arr[i][j] = 0
                else:
                    cnt += 1
print(time)
print(pre_cnt)
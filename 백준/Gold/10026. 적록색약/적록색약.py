import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy):
    v = [[0] * N for _ in range(N)]
    D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    num = 0
    for Si in range(N):
        for Sj in range(N):
            if v[Si][Sj]: continue
            num += 1  # 해당 구역 number 지정
            cur = arr[Si][Sj]
            q = deque([[Si, Sj]])
            v[Si][Sj] = num
            while q:
                si, sj = q.popleft()
                for di, dj in D:
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if not sy:    # 색약 아님
                            if arr[ni][nj] == cur and not v[ni][nj]:
                                q.append([ni, nj])
                                v[ni][nj] = num
                        else:    # 색약
                            if not cur == 'B':
                                if arr[ni][nj] != 'B' and not v[ni][nj]:
                                    q.append([ni, nj])
                                    v[ni][nj] = num
                            else:
                                if arr[ni][nj] == 'B' and not v[ni][nj]:
                                    q.append([ni, nj])
                                    v[ni][nj] = num
    return num

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
print(bfs(False), bfs(True))

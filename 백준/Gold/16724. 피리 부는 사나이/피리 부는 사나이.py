import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
D = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}
V = [[0] * M for _ in range(N)]
cnt = 0
num = 0
# 시작 위치 결정
for Si in range(N):
    for Sj in range(M):
        if V[Si][Sj]: continue
        num += 1    # safe zone 위치 count
        cnt += 1
        q = deque([[Si, Sj]])
        V[Si][Sj] = num
        while q:
            si, sj = q.popleft()
            di, dj = D[arr[si][sj]]
            ni, nj = si + di, sj + dj
            if not V[ni][nj]:
                q.append([ni, nj])
                V[ni][nj] = num
            elif V[ni][nj] != num:
                cnt -= 1
                break
print(cnt)
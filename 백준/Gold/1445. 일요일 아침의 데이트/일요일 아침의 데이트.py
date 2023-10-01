import sys
from collections import deque
input = sys.stdin.readline

def gb(si, sj, ni, nj):
    g, n = v[si][sj]
    if arr[ni][nj] == 'g':
        g += 1
        return (g, n)
    if arr[ni][nj] == '.':
        for di, dj in D:
            i, j = ni + di, nj + dj
            if 0 <= i < N and 0 <= j < M and arr[i][j] == 'g':
                n += 1
                break
    return (g, n)

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            Si, Sj = i, j
        if arr[i][j] == 'F':
            Ei, Ej = i, j

# F 꽃 g 쓰레기 S 시작 . 빈칸
q = deque([[Si, Sj]])
v = [[(2500, 2500)] * M for _ in range(N)]
v[Si][Sj] = (0, 0)
while q:
    si, sj = q.popleft()
    for di, dj in D:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M:
            # v에 저장될 new val = (쓰레기통과, 쓰레기옆지나감)
            val = gb(si, sj, ni, nj)
            if v[ni][nj] > val:
                v[ni][nj] = val
                q.append([ni, nj])
print(*v[Ei][Ej])
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [input().rstrip() for _ in range(N)]
go = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
rev = {'U': (1, 0), 'R': (0, -1), 'D': (-1, 0), 'L': (0, 1)}
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
E = set()
# 탈출 위치 검사
for i in range(N):
    for j in (0, M-1):
        di, dj = go[maze[i][j]]
        ni, nj = i + di, j + dj
        if not(0 <= ni < N and 0 <= nj < M):
            E.add((i, j))
for j in range(M):
    for i in (0, N-1):
        di, dj = go[maze[i][j]]
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < M):
            E.add((i, j))
memo = [[0] * M for _ in range(N)] # 검사 한 위치
cnt = 0
for Si, Sj in E:
    q = deque([[Si, Sj]])
    v = [[0] * M for _ in range(N)]
    v[Si][Sj] = 1
    while q:
        si, sj = q.pop()
        for di, dj in D:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if rev[maze[ni][nj]] != (di, dj):
                    continue
                if not v[ni][nj]:
                    q.append([ni, nj])
                    v[ni][nj] = 1

    # Si, Sj 에서 방문 가능한 위치 -> 탈출 가능 메모
    for vi in range(N):
        for vj in range(M):
            if v[vi][vj] and not memo[vi][vj]:
                cnt += 1
                memo[vi][vj] = 1
print(cnt)
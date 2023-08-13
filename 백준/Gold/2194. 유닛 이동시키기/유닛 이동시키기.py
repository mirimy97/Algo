import sys
from collections import deque
input = sys.stdin.readline

def arr_input(n):
    return int(n) - 1

N, M, A, B, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    i, j = map(arr_input, input().split())
    arr[i][j] = 1
Si, Sj = map(arr_input, input().split())
Ei, Ej = map(arr_input, input().split())
v = [[0] * M for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque([[Si, Sj]])
v[Si][Sj] = 1
while q and not v[Ei][Ej]:
    si, sj = q.popleft()
    for di, dj in d:
        ni, nj = si + di, sj + dj
        is_possible = True
        # 1. 이미 간 곳인지 확인
        if 0 <= ni < N and 0 <= nj < M and v[ni][nj]:
            continue
        # 2. 갈 수 있는 위치인지 확인
        for a in range(A):
            for b in range(B):
                # 유닛 중 일부분이 범위 벗어나면 out
                if not (0 <= ni + a < N) or not (0 <= nj + b < M):
                    is_possible = False
                    break
                # 장애물이 유닛과 겹치는 곳이면 out
                if arr[ni + a][nj + b]:
                    is_possible = False
                    break
            if not is_possible:
                break
        if not is_possible:
            continue
        # 1. 2. 통과했으면 q에 추가, visited
        q.append([ni, nj])
        v[ni][nj] = v[si][sj] + 1
print(v[Ei][Ej] - 1)
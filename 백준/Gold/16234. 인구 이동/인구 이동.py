import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [(0, 1), (1, 0), (-1, 0), (0, -1)]

day = 0
while 1: # 하루 += 1, 연합 할 곳 없을때까지
    v = [[0] * N for _ in range(N)]   # 다음 위치 검색해봄
    unions = []   # 연합할 나라 집합
    for Si in range(N):
        for Sj in range(N):
            # 연합 만들 시작 위치 결정
            if v[Si][Sj]: continue
            union = []
            q = deque([[Si, Sj]])
            while q:
                si, sj = q.popleft()
                for di, dj in D:
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and L <= abs(arr[ni][nj] - arr[si][sj]) <= R:
                        q.append([ni, nj])
                        union.append((ni, nj))
                        v[ni][nj] = 1
            if union:
                unions.append(union)
    if not unions: break
    else:
        day += 1
        for u in unions:
            val = 0
            for i, j in u:
                val += arr[i][j]
            for i, j in u:
                arr[i][j] = val // len(u)
print(day)
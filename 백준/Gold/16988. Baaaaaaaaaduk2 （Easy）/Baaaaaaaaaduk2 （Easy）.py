import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [(1, 0), (0, 1), (0, -1), (-1, 0)]

# 내 돌을 둘만한 곳은 2에 인접해 있는 0 자리 => S set에 저장
S = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 2:
                    S.add((i, j))
                    break
# S에서 2개씩 뽑아 탐색
max_cnt = 0
if len(S) < 2:
    S.add((-1, -1))
for s in combinations(S, 2):
    if s[0][0] != -1:
        arr[s[0][0]][s[0][1]] = 1
    if s[1][0] != -1:
        arr[s[1][0]][s[1][1]] = 1
    # 2 주변 탐색 했을 때 1이나 2만 만난다. 0을 만나면 갇힌게아님
    V = [[0] * M for _ in range(N)]
    cnt_sum = 0
    for Si in range(N):
        for Sj in range(M):
            possible = True
            if arr[Si][Sj] == 2:
                if V[Si][Sj] : continue
                cnt = 1
                q = deque([[Si, Sj]])
                v = [[0] * M for _ in range(N)]
                v[Si][Sj] = 1
                while q:
                    si, sj = q.popleft()
                    for di, dj in D:
                        ni, nj = si + di, sj + dj
                        if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                            if not arr[ni][nj]:   # 갇힌거아님
                                # print(ni, nj, "놉ㅋ")
                                possible = False
                            v[ni][nj] = 1
                            if arr[ni][nj] == 2:
                                q.append([ni, nj])
                                cnt += 1
                                V[ni][nj] = 1
                    if not possible:
                        break

                if possible:
                    cnt_sum += cnt
    max_cnt = max(max_cnt, cnt_sum)

    arr[s[0][0]][s[0][1]] = 0
    arr[s[1][0]][s[1][1]] = 0
print(max_cnt)

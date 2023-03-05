import sys
from itertools import combinations
from collections import deque
import copy

N, M = list(map(int, sys.stdin.readline().split()))
array = []
zero = []
two = []
one = 3
for i in range(N):
    new = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if new[j] == 0:
            zero.append((i, j))
        elif new[j] == 2:
            two.append((i, j))
        else:
            one += 1
    array.append(new)

comb = list(combinations(zero, 3))
min_cnt = N * M

for c in comb:
    # array 복사
    c_array = copy.deepcopy(array)
    # visited 생성
    v = [[0] * M for _ in range(N)]
    # 벽 3개 세움
    for i, j in c:
        c_array[i][j] = 1
        v[i][j] = 1
    # q 생성
    q = deque(copy.deepcopy(two))

    cnt = len(two)
    while q:
        si, sj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and c_array[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
        if min_cnt < cnt :
            break
    if min_cnt > cnt:
        min_cnt = cnt
print((N * M) - one - min_cnt)
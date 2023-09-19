import sys
from itertools import combinations
input = sys.stdin.readline

arr = [[0] * 102 for _ in range(102)]
N = int(input().rstrip())
set_i = set()
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    set_i.add(a)
    set_i.add(a + 10)
    for j in range(a, a + 10):
        for i in range(b, b + 10):
            arr[i][j] = 1
max_cnt = 0
set_i = sorted(list(set_i))
for c in combinations(set_i, 2):
    si, ei = c
    len_i = ei - si
    is_count = False
    cnt = 0
    for j in range(102):
        if not is_count:
            if len_i == sum(arr[j][si:ei]):
                is_count = True
                cnt += 1
        else:
            if len_i == sum(arr[j][si:ei]):
                cnt += 1
            else:
                is_count = False
                max_cnt = max(max_cnt, cnt * len_i)
                cnt = 0
print(max_cnt)
import sys
from collections import Counter

N, M, BB = map(int, input().split())
arr = []
for _ in range(N):
    arr += list(map(int, sys.stdin.readline().strip().split()))


cnt = Counter(arr).most_common()
cnt_sort = sorted(cnt, reverse=True)

min_t = [256 * N * M * 2, 0]
for i in range(min(arr), max(arr) + 1):
    t = 0
    B = BB
    for j in range(len(cnt)):
        bk = cnt_sort[j]
        if i == bk[0]:
            continue
        else:
            if bk[0] > i:
                B += (bk[0] - i) * bk[1]
                t += ((bk[0] - i) * bk[1]) * 2
            else:
                B -= (i - bk[0]) * bk[1]
                t += (i - bk[0]) * bk[1]
        if B < 0:
            t = -1
            break
    if t != -1:
        if t == min_t[0] and i > min_t[1]:
            min_t = [t, i]
        elif t < min_t[0]:
            min_t = [t, i]

print(min_t[0], min_t[1])
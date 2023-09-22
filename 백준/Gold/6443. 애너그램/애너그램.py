import sys
from collections import Counter
input = sys.stdin.readline

def perm(i, n, cnt):
    if i == n:
        print(''.join(new))
        return
    else:
        for apb in cnt:
            if cnt[apb]:
                cnt[apb] -= 1
                new[i] = apb
                perm(i + 1, n, cnt)
                cnt[apb] += 1


N = int(input())
for _ in range(N):
    word = list(input().rstrip())
    word.sort()
    cnt = Counter(word)
    new = [0] * len(word)
    perm(0, len(word), cnt)


import sys

N, K, M = map(int, sys.stdin.readline().split())
L = []
for i in range(N):
    long = int(sys.stdin.readline())
    if long <= K:
        continue
    elif long < 2 * K:
        L.append(long - K)
    else:
        L.append(long - (2 * K))

P = -1
l, r = 1, sum(L) // M    # 김밥 길이의 범위

while l <= r:

    m = (l+r)//2 #조각 김밥의 최대 길이
    total = sum([i//m for i in L])

    if total < M:
        r = m-1
    else:
        l = m+1
        P = m

print(P)
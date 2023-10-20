import sys
from bisect import bisect_left
input = sys.stdin.readline

N, C = map(int, input().split())  # N 집 수 C 공유기 수
X = [0] * N
for i in range(N):
    X[i] = int(input())
X.sort()

left = 1
right = X[-1] - X[0]
ans = 1
middle = (left + right) // 2
while left <= right:
    middle = (left + right) // 2
    target = X[0]
    cnt = 1
    for i in range(1, len(X)):
        if X[i] >= target + middle:
            cnt += 1
            target = X[i]

    if cnt >= C:
        left = middle + 1
        ans = middle
    else:
        right = middle - 1
print(ans)
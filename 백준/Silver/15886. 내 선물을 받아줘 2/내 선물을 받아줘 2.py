import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = input()
v = [0] * N
num, cnt = 0, 0
for S in range(N):
    if v[S]: continue
    cnt += 1
    num += 1
    q = deque([S])
    v[S] = num
    while q:
        s = q.popleft()
        if arr[s] == 'E':
            e = s + 1
        elif arr[s] == 'W':
            e = s - 1
        if 0 <= e < N and v[e] != num:
            if v[e]:
                cnt -= 1
            else:
                q.append(e)
                v[e] = num

print(cnt)
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

v = [0] * (N + 1)
q = [1]
v[1] = 1
cnt = 0
while q:
    s = q.pop()
    for e in arr[s]:
        if not v[e]:
            q.append(e)
            v[e] = 1
            cnt += 1
print(cnt)

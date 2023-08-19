import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    S, E = map(int, input().split())
    arr[E].append(S)
X = int(input())
q = [X]
v = [0] * (N + 1)
cnt = -1
while q:
    cnt += 1
    s = q.pop()
    for e in arr[s]:
        if not v[e]:
            q.append(e)
            v[e] = 1
print(cnt)
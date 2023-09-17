import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    S = input().rstrip()
    q = []
    for c in S:
        if not q or q[-1] != c:
            q.append(c)
        else:
            q.pop()
    if not q:
        ans += 1
print(ans)
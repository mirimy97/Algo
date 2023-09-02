import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
dk = list(range(G + 1))
cnt = 0
for _ in range(P):
    g = int(input())
    while dk[g] != g:
        next = dk[g]
        dk[g] -= 1
        g = next
    if g == 0:
        break
    dk[dk[g]] -= 1
    cnt += 1
print(cnt)
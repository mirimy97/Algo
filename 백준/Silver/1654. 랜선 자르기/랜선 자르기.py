K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]

div = sum(L) // N
cnt = N
for l in L:
    cnt -= l // div
while cnt > 0:
    maxdiv = 0
    for l in L:
        if l // ((l // div) + 1) > maxdiv:
            maxdiv = l // ((l // div) + 1)
            maxcnt = 1
        elif l // ((l // div) + 1) == maxdiv:
            maxcnt += 1
    div = maxdiv
    cnt -= maxcnt
print(div)
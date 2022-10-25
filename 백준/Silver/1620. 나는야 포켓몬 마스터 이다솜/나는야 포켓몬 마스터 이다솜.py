import sys

N, M = map(int, input().split())
dogam = dict()
dogam2 = dict()
for i in range(N):
    poke = sys.stdin.readline().strip()
    dogam[i+1] = poke
    dogam2[poke] = i+1

for i in range(M):
    txt = sys.stdin.readline().strip()
    try:
        idx = int(txt)
        print(dogam[idx])
    except:
        print(dogam2[txt])
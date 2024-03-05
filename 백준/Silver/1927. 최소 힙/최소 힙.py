import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(h, x)
    elif h and x == 0:
        print(heappop(h))
    else:
        print(0)
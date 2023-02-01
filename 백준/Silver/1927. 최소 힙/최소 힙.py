import sys

from heapq import heappush, heappop

N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heappush(heap, x)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)
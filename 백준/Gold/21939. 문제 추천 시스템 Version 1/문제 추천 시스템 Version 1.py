import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# recommend 1 : 어려운->문제번호 큰 / recommend -1: 쉬운 -> 문제번호 작은
# add (번호) (난이도) : 문제 추가
# solved (번호) : 제거
N = int(input())
maxh = []
minh = []
exist = {}
for _ in range(N):
    P, L = map(int, input().split())
    heappush(minh, (L, P))
    heappush(maxh, (-L, -P))
    exist[P] = L

M = int(input())
for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == 'recommend':
        if cmd[1] == '1':
            P = heappop(maxh)
            while -P[1] not in exist or exist[-P[1]] != -P[0]:
                P = heappop(maxh)
            print(-P[1])
            heappush(maxh, P)
        else:
            P = heappop(minh)
            while P[1] not in exist or exist[P[1]] != P[0]:
                P = heappop(minh)
            print(P[1])
            heappush(minh, P)
    elif cmd[0] == 'add':
        L, P = int(cmd[2]), int(cmd[1])
        heappush(minh, (L, P))
        heappush(maxh, (-L, -P))
        exist[P] = L
    elif cmd[0] == 'solved':
        del exist[int(cmd[1])]

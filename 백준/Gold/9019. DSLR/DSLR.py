import sys
from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    short = [0] * 10000
    short[A] = ''
    q = deque([A])
    while short[B] == 0:
        S = q.popleft()
        # D
        E = (S * 2) % 10000
        if short[E] == 0:
            short[E] = short[S] + 'D'
            q.append(E)
        # S
        if S == 0:
            E = 9999
        else:
            E = S - 1
        if short[E] == 0:
            short[E] = short[S] + 'S'
            q.append(E)
        # L
        strS = str(S)
        while len(strS) != 4:
            strS = '0' + strS
        E = int(strS[1] + strS[2] + strS[3] + strS[0])
        if short[E] == 0:
            short[E] = short[S] + 'L'
            q.append(E)
        # R
        E = int(strS[3] + strS[0] + strS[1] + strS[2])
        if short[E] == 0:
            short[E] = short[S] + 'R'
            q.append(E)
    print(short[B])
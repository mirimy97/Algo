import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    i = 0
    curr = 'A'
    target = 'A'
    fin = False
    possible = True
    while i < len(S):
        if i == 0:
            if S[i] not in ['A', 'B', 'C', 'D', 'E', 'F']:
                possible = False
            if S[i] == 'A':
                curr = 'A'
                target = 'F'
        elif fin:
            if S[i] not in ['A', 'B', 'C', 'D', 'E', 'F']:
                possible = False
        else:
            if S[i] == target:
                curr = target
                if curr == 'A':
                    target = 'F'
                elif curr == 'F':
                    target = 'C'
                elif curr == 'C':
                    fin = True
            if S[i] != curr and S[i] != target:
                possible = False
        i += 1
    if possible:
        print('Infected!')
    else:
        print('Good')


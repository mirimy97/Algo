import sys

M = int(input())
S = set()
for _ in range(M):
    txt = sys.stdin.readline().strip()
    if txt[:3] == 'add':
        S.add(int(txt[4:]))
    elif txt[:6] == 'remove':
        if int(txt[7:]) in S:
            S.remove(int(txt[7:]))
    elif txt[:5] == 'check':
        if int(txt[6:]) in S:
            print(1)
        else:
            print(0)
    elif txt[:6] == 'toggle':
        if int(txt[7:]) in S:
            S.remove(int(txt[7:]))
        else:
            S.add(int(txt[7:]))
    elif txt == 'all':
        S = set(range(1, 21))
    elif txt == 'empty':
        S = set()
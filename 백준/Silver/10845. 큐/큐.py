import sys
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    txt = sys.stdin.readline().strip()
    if txt[:4] == 'push':
        q.append(int(txt[5:]))
    elif txt == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif txt == 'size':
        print(len(q))
    elif txt == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif txt == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif txt == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

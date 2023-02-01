import sys
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    txt = sys.stdin.readline()
    if txt[:4] == 'push':
        q.append(int(txt[5:]))
    elif txt == 'pop\n':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif txt == 'size\n':
        print(len(q))
    elif txt == 'empty\n':
        if not q:
            print(1)
        else:
            print(0)
    elif txt == 'top\n':
        if q:
            print(q[-1])
        else:
            print(-1)

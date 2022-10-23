import sys
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    txt = sys.stdin.readline().strip()
    if txt[:10] == 'push_front':
        q.appendleft(txt[11:])
    elif txt[:9] == 'push_back':
        q.append(txt[10:])
    elif txt == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif txt == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif txt == 'size':
        print(len(q))
    elif txt == 'empty':
        if q:
            print(0)
        else:
            print(1)
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
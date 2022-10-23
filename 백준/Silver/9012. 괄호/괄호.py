from collections import deque

T = int(input())
for _ in range(T):
    txt = input()

    q = deque()
    result = 'yes'
    for t in txt:
        if t == '(':
            q.append(t)
        elif t == ')':
            if not q:
                result = 'no'
                break
            else:
                q.pop()

    if result != 'no' and not q:
        print('YES')
    else:
        print('NO')
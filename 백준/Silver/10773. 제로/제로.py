from collections import deque

K = int(input())
q = deque()
for _ in range(K):
    m = int(input())
    if m != 0:
        q.append(m)
    else:
        q.pop()
print(sum(q))
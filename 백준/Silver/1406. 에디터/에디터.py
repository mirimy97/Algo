import sys
from collections import deque
left = deque(list(input()))
T = int(input())
cs = len(left)
right = deque()
for _ in range(T):
    c = list(sys.stdin.readline().split())

    if c[0] == 'L' and left:
        right.append(left.pop())
    elif c[0] == 'D' and right:
        left.append(right.pop())
    elif c[0] == 'B' and left:
        left.pop()
    elif c[0] == 'P':
        left.append(c[1])

right.reverse()
print("".join(left), end="")
print("".join(right))

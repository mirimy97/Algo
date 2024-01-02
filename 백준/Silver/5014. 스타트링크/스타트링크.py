import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
arr = [sys.maxsize] * F
arr[S - 1] = 0
q = deque([S - 1])
# 0층 -> 9층
while q and arr[G - 1] == sys.maxsize:
    s = q.popleft()
    if s + U < F and arr[s + U] > arr[s] + 1:
        arr[s + U] = arr[s] + 1
        q.append(s + U)
    if s - D >= 0 and arr[s - D] > arr[s] + 1:
        arr[s - D] = arr[s] + 1
        q.append(s - D)
if arr[G - 1] != sys.maxsize:
    print(arr[G - 1])
else:
    print("use the stairs")

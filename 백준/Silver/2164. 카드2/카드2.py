from collections import deque

N = int(input())
arr = deque(range(1, N+1))
cnt = 0
while len(arr) > 1:
    if cnt % 2 == 0:
        arr.popleft()
    else:
        arr.append(arr.popleft())
    cnt += 1

print(arr[0])
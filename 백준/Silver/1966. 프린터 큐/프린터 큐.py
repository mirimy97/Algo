from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    idx = deque([i for i in range(N)])
    i = 0
    cnt = 0
    a = -1
    while a != M:
        if arr[i] == max(arr):
            arr.popleft()
            a = idx.popleft()
            cnt += 1
        else:
            arr.append(arr.popleft())
            idx.append(idx.popleft())
    print(cnt)
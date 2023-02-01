from collections import deque
N, K = map(int, input().split())
lst = deque(range(1, N+1))
answer = deque()
cnt = 1
while len(lst) != 0:
    if cnt % K != 0:
        lst.append(lst.popleft())
    else:
        answer.append(str(lst.popleft()))
    cnt += 1
print('<', end='')
print(', '.join(answer), end='')
print('>')
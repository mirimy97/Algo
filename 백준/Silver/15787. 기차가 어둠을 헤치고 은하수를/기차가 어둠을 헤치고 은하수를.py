import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * 21 for _ in range(N + 1)]
result = set()
for _ in range(M):
    cmd = list(map(int, input().split()))
    if len(cmd) == 3:
        n, i, x = cmd
    else: n, i = cmd

    if n == 1:
        arr[i][x] = 1
    elif n == 2:
        arr[i][x] = 0
    elif n == 3:
        arr[i] = [0, 0] + arr[i][1:20]
    else:
        arr[i] = [0] + arr[i][2:21] + [0]

for a in arr[1:]:
    result.add(''.join(map(str,a)))
print(len(result))
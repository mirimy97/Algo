N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

K -= 1
i = K
print('<', end='')
while len(arr) > 1:
    print(arr.pop(i), end=', ')
    i = (i + K) % len(arr)

print(arr[0], end='>')
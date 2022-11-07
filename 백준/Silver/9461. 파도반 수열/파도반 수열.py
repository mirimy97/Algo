T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] * (N+1)
    arr[1] = 1
    if N > 1:
        arr[2] = 1
    if N > 2:
        arr[3] = 1
    i = 4
    while arr[N] == 0:
        arr[i] = arr[i-3] + arr[i-2]
        i += 1
    print(arr[N])
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        X = N // H
        Y = H
    else:
        X = N // H + 1
        Y = N % H

    if X >= 10:
        print(str(Y) + str(X))
    else:
        print(str(Y)+ '0' + str(X))
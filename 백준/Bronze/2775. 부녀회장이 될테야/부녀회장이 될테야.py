T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    I = [i for i in range(1, n+1)]
    new_I = [0] * n

    while k != 0:
        for i in range(n):
            new_I[i] = sum(I[:i+1])
        k -= 1
        I = new_I[:]

    print(I[n-1])
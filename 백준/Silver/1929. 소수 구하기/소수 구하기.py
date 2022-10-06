from collections import deque

M, N = map(int, input().split())

prime = deque()
for i in range(2, int(N**(1/2)) + 1):
    if i == 2:
        prime.append(i)
    else:
        is_prime = True
        for p in prime:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
for i in range(M, N+1):
    is_prime = True
    for p in prime:
        if i == p:
            is_prime = True
            break
        if i != p and i % p == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        print(i)
A, B = map(int, input().split())

if A < B:
    A, B = B, A

for N in range(B, 0, -1):
    if A % N == 0 and B % N == 0:
        print(N)
        break

M = (A // N) * (B // N) * N
print(M)
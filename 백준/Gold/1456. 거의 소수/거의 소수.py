import sys
import math

A, B = map(int, sys.stdin.readline().split())

# 범위 2 ~ B**(1/2)
S = 2
E = int(B ** (1/2))

# S~E까지 소수 찾기 - 에라토스테네스의 체
sosu = [i for i in range(E+1)]
sosu[1] = 0

idx = 2
while idx <= E:
    if sosu[idx] != 0:
        n = 2
        while (idx * n) <= E:
            sosu[idx * n] = 0
            n += 1
    idx += 1

# A ~ B 전체 count 에서 -하면서 for문
# 중복 신경 안 써도 됨 (소수의 n승이기 때문에)
cnt = 0
for s in list(set(sosu)):
    if s != 0:
        n = math.ceil(math.log(A, s))
        if n < 2:
            n = 2
        while s ** n <= B:
            cnt += 1
            n += 1
print(cnt)

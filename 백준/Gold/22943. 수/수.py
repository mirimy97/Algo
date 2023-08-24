import sys
from itertools import permutations
input = sys.stdin.readline

def to_num(arr):
    return int(''.join(map(str, arr)))
K, M = map(int, input().split())
prime = [0] + [1] * (10**K)
prime[1] = 0
for i in range(2, int((10**K) ** (1/2)) + 1):
    if prime[i] == 1:
        n = i * 2
        while n <= (10**K):
            prime[n] = 0
            n += i
prime_nums = []
for i in range(len(prime)):
    if prime[i] == 1:
        prime_nums.append(i)
result = [0] * (10**K)
# 조건 0 (K가지 숫자 한번씩 사용)
for c in permutations(range(10), K):
    if c[0] == 0:
        continue
    n = to_num(c)
    result[n] = 1
# 조건 2
temp = [0] * (10**K)
for i in range(len(prime_nums)):
    for j in range(i, len(prime_nums)):
        base = prime_nums[i] * prime_nums[j]
        if base % M != 0:
            while base < (10**K):
                temp[base] += 1
                base *= M
for i in range(len(temp)):
    if temp[i] != 0:
        result[i] += 1
# 조건 1
temp = [0] * (10**K)
for i in range(len(prime_nums) - 1):
    for j in range(i+1, len(prime_nums)):
        if prime_nums[i] + prime_nums[j] >= (10**K):
            break
        temp[prime_nums[i] + prime_nums[j]] += 1
for i in range(len(temp)):
    if temp[i] != 0:
        result[i] += 1

print(result.count(3))
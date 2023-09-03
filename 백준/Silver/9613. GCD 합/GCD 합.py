import sys
from math import gcd
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = 0
    nums = list(map(int, input().split()))
    for c in combinations(nums[1:], 2):
        a, b = c
        s += gcd(a, b)
    print(s)
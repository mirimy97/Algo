import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
card = [0] * n
for i in range(n):
    card[i] = int(input())

result = set()
for num in permutations(card, k):
    result.add(int(''.join(map(str, num))))
print(len(result))
import sys
from collections import deque

input = sys.stdin.readline
def char_to_num(c):
    c = ord(c)
    if 65 <= c <= 90:
        return c - 65
    else:
        return c - 71
def num_to_char(n):
    if 0 <= n <= 25:
        return chr(n + 65)
    else:
        return chr(n + 71)
N = int(input())
arr = [[0] * 52 for _ in range(52)]
# print(ord("A"))  65 -> 0
# print(ord("Z"))  90 -> 25
# print(ord("a"))  97 -> 26
# print(ord("z"))  122 -> 51
cnt = 0
for _ in range(N):
    a, b, c = input().split()
    if a == c:
        continue
    if not arr[char_to_num(a)][char_to_num(c)]:
        cnt += 1
        arr[char_to_num(a)][char_to_num(c)] = 1


for k in range(52):
    for i in range(52):
        for j in range(52):
            if i != j and not arr[i][j] and arr[i][k] and arr[k][j]:
                arr[i][j] = 1
                cnt += 1
result = f'{cnt}\n'
for i in range(52):
    for j in range(52):
        if arr[i][j]:
            result += f'{num_to_char(i)} => {num_to_char(j)}\n'
print(result)
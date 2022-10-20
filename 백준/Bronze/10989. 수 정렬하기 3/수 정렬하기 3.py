import sys

c = [0] * 10001
for _ in range(int(input())):
    c[int(sys.stdin.readline())] += 1
for i in range(10001):
    for _ in range(c[i]):
        print(i)
import sys

N = int(sys.stdin.readline())
word = sys.stdin.readline()
s = 0
M = 1234567891

for i in range(N):
    s += (ord(word[i]) - 96) * (31**i)

print(s%M)
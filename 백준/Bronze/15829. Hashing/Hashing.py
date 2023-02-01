N = int(input())
word = input()
s = 0

for i in range(N):
    s += (ord(word[i]) - 96) * (31**i)

print(s)
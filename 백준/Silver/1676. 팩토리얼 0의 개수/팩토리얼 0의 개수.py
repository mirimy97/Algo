import math

N = int(input())

num = str(math.factorial(N))

for i in range(len(num) - 1, -1, -1):
    if num[i] != '0':
        print(len(num) - i - 1)
        break
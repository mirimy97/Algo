import math

n = int(input())
T = n // 2  # 최대 2개짜리 개수
result = 0

facto = [0] * (n+1)
for i in range(1, n+1):
    facto[i] = math.factorial(i)
facto[0] = 1

for two in range(0, T+1):
    one = n - (2 * two)
    result += facto[one + two] * (2 ** (two)) // (facto[one] * facto[two])

print(result%10007)
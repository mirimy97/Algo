import math

n = int(input())
T = n // 2  # 최대 2개짜리 개수
result = 0
for two in range(0, T+1):
    one = n - (2 * two)
    result += math.factorial(one + two) * (2 ** (two)) // (math.factorial(one) * math.factorial(two))

print(result%10007)
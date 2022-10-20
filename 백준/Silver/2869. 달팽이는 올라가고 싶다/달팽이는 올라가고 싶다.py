import math
D, N, H = map(int, input().split())

day = math.ceil((H - N) / (D - N))

print(day)
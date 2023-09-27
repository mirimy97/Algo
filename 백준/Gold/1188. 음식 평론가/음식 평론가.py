import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
# 소세지 N개 평론가 M명
total = math.lcm(N, M)
piece = math.lcm(N, M) // N
per = math.lcm(N, M) // M

ssg = [0] * (total + 1)
i = piece
while i <= total:
    ssg[i] = 1
    i += piece
i = per
cnt = 0
while i < total + 1:
    if not ssg[i]:
        cnt += 1
    i += per
print(cnt)
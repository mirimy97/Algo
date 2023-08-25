import sys
import datetime as dt
input = sys.stdin.readline

S, E, Q = input().split()
# 시간 닉네임
map = {}
cnt = 0
while 1:
    try:
        T, name = input().split()
        if T <= S:    # 입장
            if name not in map:
                map[name] = 1
        elif E <= T <= Q:
            if name in map and map[name] == 1:
                cnt += 1
                map[name] += 1
    except:
        break
print(cnt)
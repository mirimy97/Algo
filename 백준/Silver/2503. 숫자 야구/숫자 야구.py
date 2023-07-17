import sys

N = int(sys.stdin.readline())
games = [0] * N
for i in range(N):
    num, s, b = map(int, sys.stdin.readline().split())
    games[i] = [str(num), s, b]

cnt = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a != b and b != c and c != a:
            # 정답 숫자 결정
                isPossible = True
                for i in range(N):
                    s = ball = 0
                    if int(games[i][0][0]) in (a, b, c):
                        if int(games[i][0][0]) == a:
                            s += 1
                        else:
                            ball += 1
                    if int(games[i][0][1]) in (a, b, c):
                        if int(games[i][0][1]) == b:
                            s += 1
                        else:
                            ball += 1
    
                    if int(games[i][0][2]) in (a, b, c):
                        if int(games[i][0][2]) == c:
                            s += 1
                        else:
                            ball += 1
                    if s != games[i][1] or ball != games[i][2]:
                        isPossible = False
                        break
                if isPossible:
                    cnt += 1

print(cnt)
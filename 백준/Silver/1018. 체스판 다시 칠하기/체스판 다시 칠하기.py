N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

WB = ['W', 'B']
min_cnt = -1
for si in range(N - 7):
    for sj in range(M - 7):
        for first in WB:
            cnt = 0
            for i in range(si, si + 8):
                if first == 'W':
                    if i % 2 == 0:
                        idx = 0
                    else:
                        idx = 1
                elif first == 'B':
                    if i % 2 == 0:
                        idx = 1
                    else:
                        idx = 0
                for j in range(sj, sj + 8):
                    if arr[i][j] != WB[idx]:
                        cnt += 1
                    idx = (idx + 1) % 2
            if min_cnt == -1:
                min_cnt = cnt
            elif cnt < min_cnt:
                min_cnt = cnt
print(min_cnt)
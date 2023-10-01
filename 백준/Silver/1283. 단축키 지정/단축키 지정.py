import sys
N = int(input())
sc = {}
for _ in range(N):
    S = list(input().split())

    save_sc = False
    # 첫글자  i, 0
    for i in range(len(S)):
        if S[i][0].upper() not in sc:
            sc[S[i][0].upper()] = 1
            n, m = i, 0
            save_sc = True
            break
    # 왼쪽부터 차례대로
    if not save_sc:
        for i in range(len(S)):
            for j in range(len(S[i])):
                if S[i][j].upper() not in sc:
                    sc[S[i][j].upper()] = 1
                    n, m = i, j
                    save_sc = True
                    break
            if save_sc:
                break

    if save_sc:
        for i in range(len(S)):
            if i == n:
                for j in range(len(S[i])):
                    if j == m:
                        print(f'[{S[i][j]}]', end="")
                    else:
                        print(S[i][j], end="")
            else:
                print(S[i], end="")
            print(' ', end="")
    else:
        print(' '.join(S), end="")
    print()


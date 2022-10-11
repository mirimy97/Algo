def perm(i, k):
    global bj
    if i != 3:
        for j in range(i, k):
            if i == 0:
                global s
                s = 0
            s += card[j]
            card[i], card[j] = card[j], card[i]
            if s <= M:
                perm(i+1, k)
            card[i], card[j] = card[j], card[i]
            s -= card[j]
    else:
        if bj < s <= M:
            bj = s
        return

N, M = map(int, input().split())
card = list(map(int, input().split()))
bj = 0
perm(0, N)
print(bj)
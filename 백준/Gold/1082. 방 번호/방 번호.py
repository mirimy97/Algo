import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
budget = int(input())   # budget
sorted_P = []
# 0, 1, 2, ... N-1 N-1 N-1
min_val = min(P)

for i in range(N):
    sorted_P.append((P[i] - min_val, i))    # 돈 / 번호
    if P[i] == min_val:
        first = i
sorted_P.sort()

room = [first] * (budget // P[first])
M = budget - ((budget // P[first]) * min_val)
while 1:
    for r in range(len(room)):
        cand = [-1, -1]  # 후보 돈 / 번호
        for p in range(N - 1, -1, -1):
            if M >= sorted_P[p][0]:
                if cand[0] == -1 or sorted_P[p][1] > cand[1]:
                    cand = [sorted_P[p][0], sorted_P[p][1]]
        if cand[0] != -1:
            room[r] = cand[1]
            M -= cand[0]
    if (room[0] and sum(room)) or len(room) == 1:
        break
    else:
        room.pop()
        M = budget - (len(room) * min_val)
print(''.join(map(str, room)))

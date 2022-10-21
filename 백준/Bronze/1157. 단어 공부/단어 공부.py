S = input().upper()
A = list(set(S))
max_c = 0
c = ''
cnt = 0
for a in A:
    if S.count(a) > max_c:
        max_c = S.count(a)
        c = a
        cnt = 0
    elif S.count(a) == max_c:
        cnt += 1

if cnt > 0:
    c = '?'
print(c)
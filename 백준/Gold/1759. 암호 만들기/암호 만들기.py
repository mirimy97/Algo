from itertools import combinations

L, C = map(int, input().split())
apb = sorted(list(input().split()))

ans = []
for password in combinations(apb, L):
    mo = ja = 0
    for i in password:
        if i in ("a", "e", "i", "o", "u"):
            mo += 1
        else:
            ja += 1
    if mo > 0 and ja > 1:
        ans.append(''.join(password))
for i in ans:
    print(i)
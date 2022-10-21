N = int(input())
words = [input() for _ in range(N)]
leng = [[] for _ in range(51)]
for word in words:
    leng[len(word)].append(word)

for l in leng:
    l = list(set(l))
    l.sort()
    for k in l:
        print(k)
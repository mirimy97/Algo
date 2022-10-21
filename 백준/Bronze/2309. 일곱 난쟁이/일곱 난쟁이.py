k = []

for i in range(1,10) :
    k.append(int(input()))


s = sum(k)

for i in k :
    for j in k :
        if j == i :
            continue
        if i + j == s - 100 :
             break
    if i + j == s - 100 :
        break

k.sort()


for b in k :
    if b == i or b == j :
        continue
    else :
        print(b)
  
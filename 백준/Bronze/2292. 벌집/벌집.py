N = int(input())
h = 1
k = 1
while N > h:
    h += 6 * k
    k += 1
print(k)
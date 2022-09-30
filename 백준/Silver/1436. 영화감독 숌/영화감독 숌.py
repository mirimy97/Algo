N = int(input())
nums = []
n666 = []
L = [0] * 5
for i1 in range(10):
    L[0] = str(i1)
    for i2 in range(10):
        L[1] = str(i2)
        for i3 in range(10):
            L[2] = str(i3)
            for i4 in range(10):
                L[3] = str(i4)
                for i5 in range(10):
                    L[4] = str(i5)
                    for idx in range(6):
                        L.insert(idx, '666')
                        # print(L)
                        n666.append(int(''.join(L)))
                        L.remove('666')
n666 = sorted(list(set(n666)))
print(n666[N-1])
T = int(input())
for _ in range(T):
    result = input()
    Ocnt = 1
    s = 0
    for OX in result:
        if OX == 'O':
            s += Ocnt
            Ocnt += 1
        elif OX == 'X':
            Ocnt = 1
    print(s)
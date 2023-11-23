import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int,input().split()))

for command in commands:
    new = []
    N = len(arr)
    M = len(arr[0])
    if command == 1:
        for i in range(N - 1, -1, -1):
            line = []
            for j in range(M):
                line.append(arr[i][j])
            new.append(line)
    elif command == 2:
        for i in range(N):
            line = []
            for j in range(M - 1, -1, -1):
                line.append(arr[i][j])
            new.append(line)
    elif command == 3:
        for j in range(M):
            line = []
            for i in range(N - 1, -1, -1):
                line.append(arr[i][j])
            new.append(line)
    elif command == 4:
        for j in range(M - 1, -1, -1):
            line = []
            for i in range(N):
                line.append(arr[i][j])
            new.append(line)
    elif command == 5:
        for i in range(N//2):
            line = []
            line.extend(arr[N//2 + i][:M//2])
            line.extend(arr[i][:M // 2])
            new.append(line)
        for i in range(N//2):
            line = []
            line.extend(arr[N//2 + i][M//2:])
            line.extend(arr[i][M // 2:])
            new.append(line)
    elif command == 6:
        for i in range(N//2):
            line = []
            line.extend(arr[i][M // 2:])
            line.extend(arr[N//2 + i][M//2:])
            new.append(line)
        for i in range(N//2):
            line = []
            line.extend(arr[i][:M // 2])
            line.extend(arr[N//2 + i][:M//2])
            new.append(line)
    arr = new
for a in arr:
    print(*a)
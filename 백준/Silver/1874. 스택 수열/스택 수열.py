import copy
n = int(input())
arr0 = [int(input()) for _ in range(n)]
arr = copy.deepcopy(arr0)
stack = []
new = []
pp = ''
for i in range(1, n+1):
    if i != arr[0]:
        pp += '+'
        stack.append(i)
    else:
        pp += '+-'
        new.append(i)
        arr.pop(0)
        while stack and stack[-1] == arr[0]:
            pp += '-'
            new.append(stack[-1])
            stack.pop()
            arr.pop(0)

if new != arr0:
    print('NO')
else:
    for p in pp:
        print(p)
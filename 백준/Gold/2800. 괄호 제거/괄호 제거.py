import sys
import copy

A = list(sys.stdin.readline().strip())
gual = []
stack = []

for i in range(len(A)):
    if A[i] == '(':
        stack.append(i)
    elif A[i] == ')':
        gual.append([stack.pop(), i])

answer = []
for i in range(1, 1<<len(gual)):
    A_copy = copy.deepcopy(A)
    for j in range(len(gual)):
        if i & (1<<j):
            A_copy[gual[j][0]] = ""
            A_copy[gual[j][1]] = ""
    answer.append(''.join(A_copy))
answer = sorted(list(set(answer)))
for a in answer:
    print(a)

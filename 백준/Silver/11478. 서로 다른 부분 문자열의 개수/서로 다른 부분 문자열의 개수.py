import sys
input = sys.stdin.readline

answer = set()
S = input().rstrip()
for a in range(len(S)):
    for i in range(len(S) - a):
        answer.add(S[i:i+a+1])
print(len(answer))

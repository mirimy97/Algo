import sys
input = sys.stdin.readline

S = input()
i, st, ed = 0, 0, -1
in_tag = False
new = []
while i < len(S):
    if S[i] == '<':
        st = i
        if not in_tag:
            temp = []
            for s in S[ed+1:st].split():
                temp.append(s[::-1])
            new.append(' '.join(temp))
        new.append('<')
        in_tag = True
    elif S[i] == '>':
        ed = i
        if in_tag:
            new.append(S[st+1:ed])
        new.append('>')
        in_tag = False
    i += 1
if not in_tag:
    temp = []
    for s in S[ed + 1:].split():
        temp.append(s[::-1])
    new.append(' '.join(temp))
print(''.join(new))
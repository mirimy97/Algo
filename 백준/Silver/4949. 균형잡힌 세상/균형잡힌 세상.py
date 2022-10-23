from collections import deque

while True:
    txt = input()
    if txt == '.':
        break
    q = deque()
    result = 'yes'
    for t in txt:
        if t == '(' or t == '[':
            q.append(t)
        elif t == ')':
            if not q or q[-1] != '(':
                result = 'no'
                break
            else:
                q.pop()
        elif t == ']':
            if not q or q[-1] != '[':
                result = 'no'
                break
            else:
                q.pop()

    if result != 'no' and not q:
        print('yes')
    else:
        print('no')
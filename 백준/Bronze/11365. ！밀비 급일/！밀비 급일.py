import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    if s == 'END':
        break
    print(s[::-1])
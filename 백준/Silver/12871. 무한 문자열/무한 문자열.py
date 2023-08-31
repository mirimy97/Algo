import sys
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
if len(s) > len(t):
    s, t = t, s
len_s, len_t = len(s), len(t)
idx = 0
while idx < (len_t * 2):
    if s[idx % len_s] != t[idx % len_t]:
        print(0)
        sys.exit(0)
    idx += 1
print(1)
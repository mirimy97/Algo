import sys  
input = sys.stdin.readline  

fs = input().strip()  
ft = input().strip()  
print(1 if fs*len(ft) == ft*len(fs) else 0)
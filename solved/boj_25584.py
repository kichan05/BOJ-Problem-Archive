import sys

input = sys.stdin.readline

N = int(input().strip())

times = {}

for i in range(N * 4):
    names = input().strip().split()
    
    if(i % 4 == 0 or i % 4 == 2):
        time = 4
    elif(i % 4 == 1):
        time = 6
    elif(i % 4 == 3):
        time = 10
    
    for n, name in enumerate(names):
        if(name == "-"):
            continue
        
        if(name in times):
            times[name] += time
        else:
            times[name] = time
            
max_ = max(times.values(), default=0)
min_ = min(times.values(), default=0)
gap = max_ - min_

if(gap > 12):
    print("No")
else:
    print("Yes")

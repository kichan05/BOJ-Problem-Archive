N = int(input())

log = set([])

count = 0

for _ in range(N):
    msg = input()
    
    if(msg == "ENTER"):
        count += len(log)
        log = set([])
        
    else:
        log.add(msg)
        
count += len(log)
print(count)

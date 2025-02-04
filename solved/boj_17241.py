import sys

N, M, Q = map(int, input().split())

graph = [[i] for i in range(N + 1)]
uses = [False for _ in range(N + 1)]
deliverd = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    
    graph[a].append(b)
    graph[b].append(a)
for _ in range(Q):
    q = int(sys.stdin.readline())
    
    if(deliverd[q]):
        print(0)
        continue
    
    count = 0
    for i in graph[q]:
        if(not uses[i]):
            count += 1
        uses[i] = True
    
    deliverd[q] = True
    print(count)

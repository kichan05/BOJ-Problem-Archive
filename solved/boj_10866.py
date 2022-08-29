import sys
input = sys.stdin.readline

N = int(input())

deque = []

for _ in range(N):
    cmd = input().split()
    
    if(cmd[0] == "push_front"):
        deque.insert(0, cmd[1])
        
    if(cmd[0] == "push_back"):
        deque.append(cmd[1])
        
    if(cmd[0] == "pop_front"):
        if(len(deque) != 0):
            print(deque.pop(0))
        else:
            print(-1)
        
    if(cmd[0] == "pop_back"):
        if(len(deque) != 0):
            print(deque.pop(-1))
        else:
            print(-1)
        
    if(cmd[0] == "size"):
        print(len(deque))
        
    if(cmd[0] == "empty"):
        print(int(len(deque) == 0))
        
    if(cmd[0] == "front"):
        if(len(deque) != 0):
            print(deque[0])
        else:
            print(-1)
        
    if(cmd[0] == "back"):
        if(len(deque) != 0):
            print(deque[-1])
        else:
            print(-1)

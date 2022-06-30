import sys
N = int(input())

stck = []

# print(N)

for i in range(N):
    # print(i, end=" : ")
    cmd = sys.stdin.readline().split()
    
    if(cmd[0] == "push"):
        # print("push")
        stck.append(int(cmd[1]))
        
    elif(cmd[0] == "pop"):
        # print("pop", end=", ")
        if(len(stck) == 0):
            print(-1)
        else:
            print(stck.pop(-1))
            
    elif(cmd[0] == "size"):
        # print("size", end=", ")
        print(len(stck))
        
    elif(cmd[0] == "empty"):
        # print("empty", end=", ")
        print(int(len(stck) == 0))
        
    elif(cmd[0] == "top"):
        # print("top", end=", ")
        if(len(stck) == 0):
            print(-1)
        else:
            print(stck[-1])

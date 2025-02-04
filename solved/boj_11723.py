import sys

N = int(input())

nums = set()

for i in range(N):
    input_ = sys.stdin.readline().strip()
    
    if(input_ != "all" and input_ != "empty" and input_ != "print"):
        cmd, num = tuple(input_.split())
        num = int(num)
    else:
        cmd = input_
        
    if(cmd == "add"):
        nums.add(num)
    elif(cmd == "remove"):
        if(num in nums):
            nums.remove(num)
    elif(cmd == "check"):
        print(int(num in nums))
    elif(cmd == "toggle"):
        if(num in nums):
            nums.remove(num)
        else:
            nums.add(num)
    elif(cmd == "all"):
        nums = set(list(range(1, 21)))
    elif(cmd == "empty"):
        nums = set()
    else:
        print("예외", cmd)

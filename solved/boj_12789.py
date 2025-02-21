N = int(input())
nums = list(map(int, input().split()))

stack = []
target = 1

while nums:
    num = nums[0]
    if(target == num):
        del nums[0]
        target += 1
        continue
    
    if(stack and stack[-1] == target):
        target += 1
        del stack[-1]
        continue
    
    del nums[0]
    stack.append(num)

while stack:
    num = stack[-1]
    del stack[-1]
    
    if(num == target):
        target += 1
    else:
        print("Sad")
        exit(0)
print("Nice")

N = int(input())
nums = []

for _ in range(N):
    nums.append(input())
    
k = 1
while True:
    check = []
    
    for i in nums:
        num = i[-k:]
        if(num not in check):
            check.append(num)
        else:
            k += 1
            break
        
    if(len(check) == N):
        print(k)
        break

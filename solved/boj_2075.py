N = int(input())

nums = []

for _ in range(N):
    row = input().split()
    row = map(int, row)
    
    for i in row:
        if(len(nums) < N):
            nums.append(i)
        elif(min(nums) < i):
            nums.remove(min(nums))
            nums.append(i)
    
print(min(nums))

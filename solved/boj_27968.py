import sys

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_nums = [0]

for n in nums:
    sum_nums.append(sum_nums[-1] + n)
    
def search(key):
    left = 1
    right = M
    
    while(True):
        center = (left + right) // 2
        if(sum_nums[center - 1] < key <= sum_nums[center]):
           return center
           
        if(key <= sum_nums[center - 1]):
            right = center - 1
        elif(sum_nums[center] < key):
            left = center + 1

for _ in range(N):
    b = int(sys.stdin.readline().strip())
    
    if(sum_nums[-1] < b):
        print("Go away!")
    else:
        print(search(b))

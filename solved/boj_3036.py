N = int(input())
nums = list(map(int, input().split()))

def get_max_yaksu(a, b):
    for i in range(min(a, b), 0, -1):
        if(a % i == 0 and b % i == 0):
            return i
            
for i in range(1, N):
    max_yaksu = get_max_yaksu(nums[0], nums[i])
    print(f"{nums[0] // max_yaksu}/{nums[i] // max_yaksu}")

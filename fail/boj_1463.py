import sys
sys.setrecursionlimit(1000000)

N = int(input())

nums = [-1] * (N + 1)

nums[1] = 0

def fun(n):
    n1 = n + 1
    n2 = n * 2
    n3 = n * 3
    
    if(n1 <= N):
        if(nums[n1] == -1 or nums[n1] > nums[n] + 1):
            nums[n1] = nums[n] + 1
        fun(n1)
    
    if(n2 <= N):
        if(nums[n2] == -1 or nums[n2] > nums[n] + 1):
            nums[n2] = nums[n] + 1
        fun(n2)
    
    if(n3 <= N):
        if(nums[n3] == -1 or nums[n3] > nums[n] + 1):
            nums[n3] = nums[n] + 1
        fun(n3)
        
fun(1)

if(nums[N] == -1):
    count = 0
    while True:
        count += 1
        if(nums[N - count] != -1):
            nums[N] = nums[N - count] + count
            break
        
print(nums[N])

# 틀린 이유 : 이건 DP가 아니라, 재귀, DFS이다.
# DP가 뭔지 더 공부해보자

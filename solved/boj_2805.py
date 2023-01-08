N, M = map(int, input().split())
nums = list(map(int, input().split()))

st, end = 0, max(nums)

while (st <= end):
    mid = (st + end) // 2
    sum_ = 0
    
    for i in nums:
        sum_ += max(0, i - mid)
        
    if(sum_ == M):
        break
    
    if(sum_ < M):
        end = mid - 1
    else:
        st = mid + 1
        


    # print(st, end)
    
print((st + end) // 2)

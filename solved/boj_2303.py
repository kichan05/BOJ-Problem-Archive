N = int(input())

nums = []

counts = []

maxIdx = 0

for i in range(N):
    nums.append(list(map(int, input().split())))
    
    counts.append(0)
    
    for j1 in range(5):
        for j2 in range(j1 + 1, 5):
            for j3 in range(j2 + 1, 5):
                
                sum_ = nums[i][j1] + nums[i][j2] + nums[i][j3]
                
                #print(f"{i} : {j1} {j2} {j3} -> {sum_}")
                
                if(sum_ % 10 > counts[i] % 10):
                    counts[i] = sum_
                    
    # print(f"count : {counts[i]}")
    # if(maxIdx == -1):
    #     maxIdx = 0;
    if(counts[maxIdx] % 10 <= counts[i] % 10):
        #print(f"{maxIdx} -> {i}")
        maxIdx = i
    # elif(counts[maxIdx] % 10 == counts[i] % 10):
    #     if(counts[maxIdx] < counts[i]):
    #         maxIdx = i
            
# print(counts)
print(maxIdx + 1)

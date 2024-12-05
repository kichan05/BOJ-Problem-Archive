import sys

input = sys.stdin.readline

N = int(input())
costList = [0 for _ in range(1002)]

jinju = 0


for _ in range(N):
    input_ = input().split()
    
    name = input_[0]
    cost = int(input_[1])
    
    if(name == "jinju"):
        jinju = cost
    costList[min(1001, cost)] += 1
    
print(jinju)
print(sum(costList[jinju + 1:]))

N = int(input())

sum_ = 0

for _ in range(N):
    C, K = map(int, input().split())
    
    sum_ += C * K
    
print(sum_)

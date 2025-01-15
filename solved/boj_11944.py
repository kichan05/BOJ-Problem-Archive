N, M = map(int, input().split())

def count_num_len(n):
    count = 0
    
    while(n):
        count += 1
        n //= 10
        
    return count
    
len_ = count_num_len(N)

if(len_ * N <= M):
    for i in range(N):
        print(N, end="")
else:
    for i in range(M // len_):
        print(N, end="")
    
    for i in range(1, M % len_ + 1):
        print(N // (10 ** (len_ - i)) % 10, end="")

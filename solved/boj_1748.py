sum_ = 0;

N = int(input())

for i in range(0, 10 ** 9):
    if(10 ** i <= N < 10 ** (i + 1)):
        for j in range(i + 1):
            if(9 * 10 ** j < N):
                sum_ += (j + 1) * (9 * 10 ** j)
            else:
                sum_ += (j + 1) * N;
                
            # print(sum_)
            # * min(9 * 10 ** j, N` % 10 ** (j + 1))
            
            #print(min(9 * 10 ** j, N % 10 ** (j + 1)))
            
            N -= 9 * 10 ** j
        
        break;

print(sum_)

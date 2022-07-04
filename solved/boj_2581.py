M = int(input())
N = int(input())


sosu = []
sum_ = 0;
min_ = -1


def isSosu(n):
    if(n == 1):
        return False
        
    for i in sosu:
        if(n % i == 0):
            return False
    return True

for i in range(1, N + 1):
    if(isSosu(i)):
        sosu.append(i)
        if(M <= i <= N):
            sum_ += i;
            if(min_ == -1):
                min_ = i
            
            
if(min_ != -1):
    print(sum_)

print(min_)
        

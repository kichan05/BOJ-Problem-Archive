M = int(input())
N = int(input())

i = 1
min_ = 10000 ** 2 + 1
sum_ = 0

while (i ** 2) <= N:
    if(M <= (i ** 2)):
        min_ = min(min_, i ** 2)
        sum_ += (i ** 2)
        
    i += 1

if(min_ == 10000 ** 2 + 1):
    print(-1)
else:
    print(sum_)
    print(min_)

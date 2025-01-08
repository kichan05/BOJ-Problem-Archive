import math

R, C, N = map(int, input().split())

min_ = min(R, C)
max_ = max(R, C)

if(N < min_):
    print(math.ceil(min_ / N) * math.ceil(max_ / N))
elif(min_ <= N < max_):
    print(math.ceil(max_ / N))
else:
    print(1)

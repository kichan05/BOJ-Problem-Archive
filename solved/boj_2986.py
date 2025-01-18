import math

N = int(input())
i = 2

div = 1

while(i <= math.sqrt(N)):
    if(N % i == 0):
        div = N // i
        break
    
    i += 1
    
print(N - div)

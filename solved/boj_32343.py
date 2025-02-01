N = int(input())
a, b = map(int, input().split())

if(a + b <= N):
    once = a + b
    zero = N - (a + b)
else:
    once = 2 * N - (a + b)
    zero = a + b - N
    
    
res = 0

for i in range(N):
    if(i >= zero):
        res += 2 ** i
        
print(res)

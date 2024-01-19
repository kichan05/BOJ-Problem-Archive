T = [0]

n = 1
while T[-1] < 1000:
    T.append(T[-1] + n)
    n += 1

dp = [False] * 1001

for i in T[1:]:
    for j in T[1:]:
        for k in T[1:]:
            num = i + j + k
            
            if(num <= 1000):
                dp[num] = True
                
            # print(num, i, j, k)



t = int(input())
for _ in range(t):
    K = int(input())
    
    print(int(dp[K]))

S = list(map(int, list(input())))
N = len(S)

pre = []

for i in range(N):
    if(i == 0):
        pre.append(S[i])
    else:
        pre.append(pre[i - 1] + S[i])
max_ = 0

if(N % 2 == 0):
    start_index = 0
else:
    start_index = 1

for s1 in range(start_index, N, 2):
    e1 = (s1 + N) // 2 - 1
    s2 = e1 + 1
    e2 = N - 1
    
    if(s1 == 0):
        sum1 = pre[e1]
    else:
        sum1 = pre[e1] - pre[s1 - 1]
    sum2 = pre[e2] - pre[s2 - 1]
    
    if(sum1 == sum2):
        max_ = (N - s1)
        break
        
print(max_)

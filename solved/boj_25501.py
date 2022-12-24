T = int(input())

for _ in range(T):
    S = input()
    
    isPa = int(S == S[::-1])
    
    if(isPa):
        count = len(S) // 2 + 1
        print(isPa, count)
        continue
    
    count = 0
    
    while(S[count] == S[len(S) - 1 - count]):
        count += 1
    
    print(0, count + 1)

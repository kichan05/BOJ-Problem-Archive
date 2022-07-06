n = int(input())

if(n == 1 or n == 3):
    print(-1)
else:
    count5 = n // 5
    mod = n % 5
    
    if(mod % 2 != 0):
        count5 -= 1
        mod += 5
    
    count2 = mod / 2
    
    print(int(count5 + count2))

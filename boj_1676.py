N = int(input())

count = 0
count2 = 0
count5 = 0


def powCount(n, p):
    c = 0
    while(n % p == 0):
        c += 1
        n /= p
    
    return (c, n)

for i in range(2, N + 1):
    c, i = powCount(i, 10)
    count += c
    
    c, i = powCount(i, 2)
    count2 += c
    
    c, i = powCount(i, 5)
    count5 += c
    
    if(count2 > 0 and count5 > 0):
        if(count2 > count5):
            count += count5
            count5 = 0
            count2 -= count5
        else:
            count += count2
            count2 = 0
            count5 -= count2

print(count)

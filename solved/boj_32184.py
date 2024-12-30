A, B = map(int, input().split())

total = 0
if(A % 2 == 0):
    A += 1
    total += 1


if(B % 2 == 1):
    B -= 1
    total += 1
    
total += (B - A + 1) // 2

print(total)

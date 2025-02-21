N = int(input())

if(N % 2 == 0 or N % 5 == 0):
    print(-1)
    exit(0)

length = 1
iiiii = 1

while (iiiii % N != 0):
    length += 1
    iiiii = (10 * iiiii % N + 1) % N
    
print(length)

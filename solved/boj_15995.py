a, m = map(int, input().split())

Q = 0

while(True):
    if((m * Q + 1) % a == 0):
        x = (m * Q + 1) // a
        
        break;
    Q += 1
print(x)

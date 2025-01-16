N = int(input())
A, Pa, B, Pb = map(int, input().split())

max_ = 0
max_x = 0
max_y = 0

x = 0
y = 0

while(True):
    y = (N  - Pa * x) // Pb

    if(Pa * x + Pb * y > N):
        break
    
    value = A * x + B * y;
    
    if(max_ < value):
        max_ = value
        max_x = x
        max_y = y
        
    x += 1
    
print(max_x, max_y)

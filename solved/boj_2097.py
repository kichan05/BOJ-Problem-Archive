import math

N = int(input())
if(N <= 3):
    print(4)
else:
    width = int(math.sqrt(N))
    height = int(math.sqrt(N))
    rest = N - width ** 2
    
    if(0 < rest <= width):
        width += 1
    elif(width < rest):
        width += 1
        height += 1
        
    width -= 1
    height -= 1
    
    print(2 * (width + height))

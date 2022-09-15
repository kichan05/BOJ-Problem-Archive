N = int(input())


i = 1

result = 0

# print(result)

while N % 10 ** i != N:
    front = N % (10 ** (i + 1))  // (10 ** i)
    back = N % (10 ** i) // (10 ** (i - 1))
    
    if(back >= 5):
        N += (10 - back) * 10 ** (i - 1)
    else:
        N -= back * 10 ** (i - 1)
    
    
    # print(front, back, N)
    
    i += 1
    
print(N)

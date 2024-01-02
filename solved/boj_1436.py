def isEndNum(num):
    num = str(num)
    
    return "666" in num

N = int(input())

i = 1
while N > 0:
    # print(i, N)
    if(isEndNum(i)):
        N -= 1
    
    i += 1
    
print(i - 1)
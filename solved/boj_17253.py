import sys
sys.setrecursionlimit(1000)

def isSamSam(num):
    # print(num)
    if(num == 1):
        return True
    if(num % 3 == 0 and isSamSam(num // 3)):
        return True
    if((num - 1) % 3 == 0 and isSamSam((num - 1) // 3)):
        return True
    
    return False

N = int(input())

if(N != 0 and isSamSam(N)):
    print("YES")
else:
    print("NO")

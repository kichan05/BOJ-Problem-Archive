sosu = [0] * 1_000_001

def isSosu(num):
    if sosu[num] != 0:
        return sosu[num] == 1
    
    for i in range(2, round(num ** (0.5)) + 1):
        if(num % i == 0):
            sosu[num] = -1
            return False
    
    sosu[num] = 1
    return True
    
def soinsubunhe(num):
    if(isSosu(num)):
        return [num]
        
    for i in range(2, num):
        if(num % i == 0):
            return [i] + soinsubunhe(num // i)

K = int(input())
sosus = soinsubunhe(K)
count = len(sosus)
T = 0
while count != 1:
    count = count // 2 + count % 2
    T += 1
print(T)

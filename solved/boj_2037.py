p, w = map(int, input().split())

def getNumber(ch):
    if(ch == " "):
        return 1, 0
        
    if(ord("P") <= ord(ch) <= ord("S")):
        return 7, ord(ch) - ord("P")
        
    if(ord("T") <= ord(ch) <= ord("V")):
        return 8, ord(ch) - ord("T")
        
    if(ord("W") <= ord(ch) <= ord("Z")):
        return 9, ord(ch) - ord("W")
        
    return (ord(ch) - 59) // 3, (ord(ch) - 59) % 3
    
    
str_ = input()

count = 0

last = -1

for i in str_:
    number, diff = getNumber(i)
    count += p * (diff + 1)
    
    if(number == last and number != 1):
        count += w
    
    
    last = number
    
    # print(count)
    
print(count)

num = 0
total = 0

try:
    while True:
        S = input()
        
        for s in S:
            if(s == ","):
                total += num
                num = 0
            else:
                num *= 10
                num += int(s)
    
except:
    total += num
    print(total)

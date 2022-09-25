T = int(input())

for t in range(1, T + 1):
    str_ = input().lower()
    count = {}
    
    for i in range(ord("a"), ord("z") + 1):
        count[chr(i)] = 0
    
    for j in str_:
        if j in count:
            count[j] += 1
            
    min_ = min(count.values())
    
    print(f"Case {t}: ", end = "")
    
    if(min_ == 0):
        print("Not a pangram")
        
    elif(min_ == 1):
        print("Pangram!")
        
    elif(min_ == 2):
        print("Double pangram!!")
        
    elif(min_ == 3):
        print("Triple pangram!!!")

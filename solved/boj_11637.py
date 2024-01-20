T = int(input())

for _ in range(T):
    max_id = 0
    max_ = 0
    total = 0
    n = int(input())
    
    same_count = 0
    
    for i in range(1, n + 1):
        k = int(input())
        total += k
        
        if(max_ < k):
            max_ = k
            max_id = i
            same_count = 0
        elif(max_ == k):
            same_count += 1
    
    if(same_count != 0):
        print("no winner")
        continue
    
    if(max_ > total // 2):
        print("majority winner", end=" ")
    else:
        print("minority winner", end=" ")
        
    print(max_id)

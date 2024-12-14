T = int(input())

for _ in range(T):
    K = int(input())
    student = list(map(int, input().split()))
    count = 0
    min_ = -1
    min_id = -1
    
    N = int(input())
    
    for _ in range(N):
        id_, m, s = map(int, input().split())
        
        s += m * 60
        
        if(id_ not in student):
            continue
        if(m == -1):
            continue
        
        if(min_ == -1 or min_ > s):
            min_ = s
            min_id = id_
            
        if(s <= 6 * 60):
            count += 1
            
    print(min_id, count)

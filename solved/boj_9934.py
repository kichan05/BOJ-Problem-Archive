K = int(input())

building = []

building.append(list(map(int, input().split())))
    
    
for i in range(1, K + 1):
    building_ = []
    for j in building:
        m = len(j) // 2
        
        print(j[m], end=" ")
        
        building_.append(j[ : m])
        building_.append(j[m + 1 : ])
        
        building = building_
    
    print()

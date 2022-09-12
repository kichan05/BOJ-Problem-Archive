N, ki, im = map(int, input().split())

list_ = []

for i in range(1, N + 1):
    if(i == ki or i == im):
        list_.append(1)
    else:
        list_.append(0)
        
round_ = 0

while(1):
    round_ += 1
    
    newList = []
    for i in range(0, len(list_)):
        if(i % 2 == 1):
            continue
        
        if(i == len(list_) - 1):
            newList.append(list_[i])
            continue
            
        if(list_[i] != list_[i + 1]):
            newList.append(1)
        elif(list_[i] == 0):
            newList.append(0)
        else:
            print(round_)
            exit(0)
            
    list_ = newList[::]

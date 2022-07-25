page = int(input())

while(page):
    que = input().split(",")
    pageList = set([])
    
    for i in que:
#         print(i.split("-"))
        if("-" in i):
            low, high = map(int, i.split("-"))

            for j in range(low, high + 1):
                if( j > page):
                    break
                pageList.add(j)
        else:
            if(int(i) <= page):
                pageList.add(int(i))
            
    print(len(pageList))
    
    
    page = int(input())
    
    

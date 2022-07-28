def f(x):
    return huboLike[x]

N = int(input())
c = int(input())

likeList = list(map(int, input().split()))

huboList = []
huboLike = {}

for i in likeList:
    if(i in huboList):
        # 사진틀에 후보 사진이 올라간 경우
        huboLike[str(i)] += 1 # 해당 후보의 추천수를 1 증가시킨다.
    else:
        # 없는 경우
        huboList.append(i)
        
        if(len(huboList) > N):
            # print(i, "초과", huboList)
            n = int(min(huboLike.keys(), key=f))
#             print(i, n)
            huboList.remove(n)
            del huboLike[str(n)]
        
        if(str(i) in huboLike):
            huboLike[str(i)] += 1
        else:
            huboLike[str(i)] = 1
            
        # print(i, huboLike)

huboList.sort()
for i in huboList:
    print(i, end = " ")
# print(huboList)
# print(huboLike)

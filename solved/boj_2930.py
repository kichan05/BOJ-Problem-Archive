R = int(input())
sangun = list(input())
N = int(input())

round_ = [[0, 0, 0] for _ in range(R)]

def toNum(i):
    if(i == "S"):
        return 0
    if(i == "R"):
        return 1
    if(i == "P"):
        return 2
        
def getScore(s, f):
    result = s - f
    
    if(result == 1 or result == -2):
        return 2
    elif(result == 0):
        return 1
        
    return 0
        
score = 0

for i in range(N):
    friend = list(input())
    
    for r in range(R):
        s = toNum(sangun[r])
        f = toNum(friend[r])
        
        score += getScore(s, f)
        
        for i in range(3):
            round_[r][i] += getScore(i, f)
        
        
max_score = 0
for r in range(R):
    max_score += max(round_[r])
print(score)
print(max_score)

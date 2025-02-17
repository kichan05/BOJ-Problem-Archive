S = input()

score = 0
max_score = 0


for s in S:
    if(s == "("):
        score += 1
    elif(s == "{"):
        score += 2
    elif(s == "["):
        score += 3
    elif(s == ")"):
        score -= 1
    elif(s == "}"):
        score -= 2
    elif(s == "]"):
        score -= 3
        
    if(ord("0") <= ord(s) <= ord("9")):
        max_score = max(max_score, score)
        
print(max_score)

R, C = map(int, input().split())

lefts = []

for _ in range(R):
    lefts.append(input())
    
A, B = map(int, input().split())
A -= 1
B -= 1
    
for r in range(R * 2):
    for c in range(C * 2):
        if(r < R and c < C):
            char_ = lefts[r][c]
            
        elif(r < R and c >= C):
            char_ = lefts[r][2 * C - 1 - c]
            
        elif(r >= R and c < C):
            char_ = lefts[2 * R - 1 - r][c]
        else:
            char_ = lefts[2 * R - 1 - r][2 * C - 1 - c]
            
        if(r == A and c == B):
            if(char_ == "."):
                print("#", end="")
            else:
                print(".", end="")
        else:
            print(char_, end="")
    
    print()

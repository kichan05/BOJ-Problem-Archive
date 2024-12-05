import math

str_ = input()
N = len(str_)

R = 0
C = 0

i = 1;
root = math.sqrt(N)

while(i <= root):
    if(N % i == 0):
        R = i
        C = N // R
        
    i += 1

for r in range(R):
    for c in range(C):
        # print(C * c + r, end=" ")
    # print()
        print(str_[R * c + r], end = "")

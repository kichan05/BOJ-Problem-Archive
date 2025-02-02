T = int(input())

zero = [list(range(15))]

for row in range(1, 15):
    for col in range(15):
        if(col == 0):
            zero.append([0])
            continue
        
        zero[row] = zero[row] + [zero[row][col - 1] + zero[row - 1][col]]

for _ in range(T):
    k = int(input())
    n = int(input())
    
    print(zero[k][n])

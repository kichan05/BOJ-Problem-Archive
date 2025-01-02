P = int(input())

sw = 0
eb = 0
ai = 0
nubi = 0

for _ in range(P):
    G, C, N = map(int, input().split())
    
    if(G == 1):
        nubi += 1
    elif(1 <= C <= 2):
        sw += 1
    elif(C == 3):
        eb += 1
    elif(C == 4):
        ai += 1
        
print(sw)
print(eb)
print(ai)
print(nubi)

N, K = map(int, input().split())

NFact = 1

for i in range(1, N + 1):
    NFact *= i
    
KFact = 1

for i in range(1, K + 1):
    KFact *= i
    
KKFact = 1

for i in range(1, N - K + 1):
    KKFact *= i
    
print(int(NFact / KFact / KKFact))

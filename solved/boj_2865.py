N, M, K = map(int, input().split())

abilitys = [0 for _ in range(N)]

for _ in range(M):
    input_ = list(map(float, input().split()))
    
    for i in range(N):
        id_ = int(input_[2  * i]) - 1
        ability = input_[2  * i + 1]
        
        if(abilitys[id_] < ability):
            abilitys[id_] = ability
        
abilitys.sort()
abilitys = abilitys[::-1]

print(round(sum(abilitys[:K]), 1))

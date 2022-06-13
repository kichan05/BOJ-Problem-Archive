Hs, Ms, Ss = tuple(map(int, input().split(":")))
He, Me, Se = tuple(map(int, input().split(":")))

if(Se < Ss):
    Se += 60
    Me -= 1
    
S = Se - Ss

if(Me < Ms):
    Me += 60
    He -= 1
    
M = Me - Ms

if(He < Hs):
    He += 24
    
H = He - Hs



    
print(f"{H :02d}:{M :02d}:{S :02d}")

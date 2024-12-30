N, M = map(int, input().split())

V, P, S = map(int, input().split())
my = V + P + S

stat = []

for i in range(1, N + 1):
    V, P, S = map(int, input().split())
    st = V + P + S
    if(st > my):
        continue
    
    stat.append({"id": i, "stat" : st})
   
   
stat = sorted(stat, key = lambda x : x["stat"])
stat = stat[::-1]

print(0, end=" "),

for i in range(M - 1):
    if(i >= len(stat)):
        break
    print(stat[i]["id"], end=" ")

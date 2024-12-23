R, C = map(int, input().split())
rank = [0] * (R + 1)
rank_count = [0] * (C - 2)

team_count = 0

for r in range(R):
    line = input()
    count = 0
    
    for c in range(C - 2, -1, -1):
        if(line[c] != "."):
            line_number = line[c]
            break
        else:
            count += 1
            
    if(line_number == "S"):
        continue
    
    team_count += 1
    
    rank[int(line_number)] = count
    rank_count[count] = 1
            
for t in range(1, team_count + 1):
    rank_ = rank[t]
    print(sum(rank_count[:rank_]) + 1)

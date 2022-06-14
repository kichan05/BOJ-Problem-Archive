name = input()

n = int(input())

teamName = "sdasd"
teamCount = 0

for i in range(n):
    team = input()
    
    L = name.count("L") + team.count("L")
    O = name.count("O") + team.count("O")
    V = name.count("V") + team.count("V")
    E = name.count("E") + team.count("E")
    
    
    sum_ = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    if(teamCount < sum_):
        teamName = team
        teamCount = sum_
        
    elif(teamCount == sum_):
        list_ = [team, teamName]
        list_.sort()
        teamName = list_[0]
    
print(teamName)

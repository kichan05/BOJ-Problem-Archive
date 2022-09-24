scien = []

for _ in range(4):
    scien.append(int(input()))
    
society = []

for _ in range(2):
    society.append(int(input()))
    
print(sum(scien) - min(scien) + max(society))

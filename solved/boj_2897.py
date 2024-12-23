R, C = map(int, input().split())

map_ = []
block_count = [0] * 5

def count_cell(r, c):
    count = 0
    for dr in range(2):
        for dc in range(2):
            cell = map_[r + dr][c + dc]
            if(cell == "#"):
                return -1
            elif(cell == "X"):
                count += 1
                
    return count

for _ in range(R):
    map_.append(list(input()))
    
for r in range(R - 1):
    for c in range(C - 1):
        count = count_cell(r, c)
        
        if(count == -1):
            continue
        else:
            block_count[count] += 1
            
for i in block_count:
    print(i)

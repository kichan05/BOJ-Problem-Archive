count = []

flag = []

vertical_count = [{} for _ in range(3)]
horizontal_count = [{} for _ in range(3)]

colors = set()

for i in range(6):
    row = input()
    flag.append(row)
    
for row in range(6):
    for col in range(9):
        ch = flag[row][col]
        
        colors.add(ch)
        
        if(ch not in vertical_count[row // 2]):
            vertical_count[row // 2][ch] = 0
        vertical_count[row // 2][ch] += 1
        
        if(ch not in horizontal_count[col // 3]):
            horizontal_count[col // 3][ch] = 0
        horizontal_count[col // 3][ch] += 1


max_count = 0

for c1 in colors:
    for c2 in colors:
        if(c1 == c2):
            continue
        for c3 in colors:
            if(c2 == c3):
                continue
            
            
            v_c1_count = vertical_count[0].get(c1, 0)
            v_c2_count = vertical_count[1].get(c2, 0)
            v_c3_count = vertical_count[2].get(c3, 0)
            max_count = max(max_count, v_c1_count + v_c2_count + v_c3_count)
            
            
            h_c1_count = horizontal_count[0].get(c1, 0)
            h_c2_count = horizontal_count[1].get(c2, 0)
            h_c3_count = horizontal_count[2].get(c3, 0)
            max_count = max(max_count, h_c1_count + h_c2_count + h_c3_count)
if(max_count != 0):
    print(54 - max_count)
else:
    print(18)

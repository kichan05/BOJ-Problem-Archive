N = int(input())
K = 0

move_list = []

def move(start, target, count):
    global K
    
    middle = 6 - start - target
    

    if(count != 1):
        move(start, middle, count - 1)
    move_list.append((start, target))
    K += 1
    if(count != 1):
        move(middle, target, count - 1)
    
move(1, 3, N)

print(K)
for s, t in move_list:
    print(s, t)

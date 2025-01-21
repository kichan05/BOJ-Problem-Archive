colors = set()

for i in range(2):
    c = input().split()
    colors.add(c[0])
    colors.add(c[1])
    
colors = list(colors)
colors = sorted(colors)

for c1 in colors:
    for c2 in colors:
        print(c1, c2)

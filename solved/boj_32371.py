keys = [list(input()) for _ in range(4)]

ota = input()

rowSum = 0
colSum = 0

for k in ota:
    for r in range(4):
        for c in range(10):
            if(k == keys[r][c]):
                rowSum += r;
                colSum += c;

# print(rowSum / 3, colSum / 3)
print(keys[int(rowSum / 9)][int(colSum / 9)])

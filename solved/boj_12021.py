a, b = map(int, input().split())
xList = [0, a]
yList = [0, b]

for i in range(2, 1000):
    xList.append((xList[i - 1] + yList[i - 1]) / 2)
    yList.append(2 * (xList[i - 1] * yList[i - 1]) / (xList[i - 1] + yList[i - 1]))

print(xList[-1], yList[-1])

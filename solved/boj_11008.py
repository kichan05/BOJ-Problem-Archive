t = int(input())

for i in range(t):
    s, p = tuple(input().split())
    overCount = 0
    
    while(p in s):
      s = s.replace(p, '', 1)
      overCount += 1

    print(overCount + len(s))

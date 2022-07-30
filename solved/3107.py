ip = input().split(":")
newIp = []

for n, i in enumerate(ip):
    if(i == ""):
        if(ip[n + 1] == ""):
            del ip[n + 1]
        
        newIp.extend((8 - len(ip) + 1) * ["0000"])
    else:
        newIp.append("{:>04s}".format(i))
    

print(":".join(newIp))

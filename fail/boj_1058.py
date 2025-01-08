N = int(input())

friends = []
friend_count = []

for i in range(N):
    f = list(map(lambda x : x == "Y", list(input())))
    
    friends.append(f)
    friend_count.append(sum(f))
    
for n, friend in enumerate(friends):
    for m, f in enumerate(friend):
        if(not f):
            continue
        
        for k, f_ in enumerate(friends[m]):
            if(f_ and not friend[k] and n != k):
                friend_count[n] += 1
                
print(max(friend_count))

N, M = map(int, input().split())

words = set([])

count = {}

for _ in range(N):
    word = input()
    
    if(len(word) >= M):
        words.add(word)
        
        if(word not in count):
            count[word] = 0
        count[word] += 1


words = sorted(words, key = lambda x : (N - count[x], 100000 - len(x), x))

for word in words:
    print(word)

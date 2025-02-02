import sys

N = int(input())

words = set()

def swap(left, right):
    global words
    
    temp = words[left]
    words[left] = words[right]
    words[right] = temp
    
def strcmp(str1, str2):
    same_count = 0
    for i in range(len(str1)):
        ch1 = ord(str1[i])
        ch2 = ord(str2[i])
        
        if(ch1 > ch2):
            return -1
        elif(ch1 == ch2):
            same_count += 1
    
    if(same_count == len(str1)):
        return 0
        
    return 1
        
for _ in range(N):
    word = sys.stdin.readline().strip()
    words.add(word)
    
words = sorted(words, key = lambda x: (len(x), x))

# for i in range(N):
#     for j in range(N - i - 1):
#         len1 = len(words[j])
#         len2 = len(words[j + 1])
        
#         if(len1 > len2):
#             swap(j, j + 1)
#             continue
        
#         if(len1 == len2):
#             cmp_ = strcmp(words[j], words[j + 1])
            
#             if(cmp_ == 0):
#                 del words[j + 1]
#             if(cmp_ == -1):
#                 swap(j, j + 1)
    
for w in words:
    print(w)

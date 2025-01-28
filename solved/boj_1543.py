text = input()
key = input()

text_size = len(text)
key_size = len(key)
left = 0

count = 0

while left <= text_size - key_size:
    if(text[left:left + key_size] == key):
        count += 1
        left = left + key_size
    else:
        left += 1
        
print(count)

T = int(input())

while(T):
    T -= 1
    
    
    N = int(input())
    
    N = N % 29 + (N // 30) % 30;
        
    if(N > 15):
        N = 30 - N
    
    text = "%s" % format(N, '04b')
    text = text.replace("1", "딸기")
    text = text.replace("0", "V")
    print(text)

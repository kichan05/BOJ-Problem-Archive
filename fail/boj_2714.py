T  = int(input())

while(T):
    T -= 1
    
    
    input_ = input().split()
    R = int(input_[0])
    C = int(input_[1])
    msg =  input_[2]
    
    msgList = [msg[i * C : i * C + C] for i in range(R)]
    
#     print(msgList)
#     continue
    
    sX = 0
    sY = 0
    x = 0
    y = 0
    state = 0
    
    msgRealList = ""
    
    msgReal = ""
    
    for i in range(R * C):
        msgReal += msgList[y][x]
        
        if(state == 0):
            x += 1
        elif(state == 1):
            y += 1
        elif(state == 2):
            x -= 1
        elif(state == 3):
            y -= 1
            
        
        if(state == 0 and x == C - 1):
            sY += 1
            state = 1
        elif(state == 1 and y == R - 1):
            R -= 1
            state = 2
        elif(state == 2 and x == sX):
            C -= 1
            state = 3
        elif(state == 3 and y == sY):
            sX += 1
            state = 0
        
        if(len(msgReal) == 5):
            int_ = int("0b" + msgReal, 2)
            
            if(int_ == 0):
                msgRealList += " "
            else:
                msgRealList += (chr(int_ + 64))
                
            msgReal = ""
            
    print(msgRealList)

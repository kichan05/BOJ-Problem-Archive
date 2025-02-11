T = int(input())

for _ in range(T):
    message = input().split()
    
    while True:
        input_ = input()
        
        if(input_[:4] == "what"):
            break
        
        say = input_.split()[-1]

        
        while say in message:
            message.remove(say)
    print(*message, sep=" ")

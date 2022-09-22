for _ in range(3):
    uit = input().split()
    count = uit.count("0")
    
    if(count == 0):
        print("E")
    else:
        print(chr(count + ord("A") - 1))

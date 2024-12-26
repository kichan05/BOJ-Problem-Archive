key_board = [
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
]

while True:
    try:
        text = input()
    except:
        break
    
    for t in text:
        row = 0
        col = 0
        if(t == " "):
            print(" ", end="")
        else:
            for n, key_list in enumerate(key_board):
                if(t in key_list):
                    row =  n
                    col = key_list.index(t)
                   
                    break
            
            print(key_board[row][col - 1], end="")
            
    print()

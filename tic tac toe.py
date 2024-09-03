import numpy 
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
player1='X'
player2='O'
def checks_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if (board[r][c]==symbol):
                count+=1
        if(count==3):
            print(symbol,'won')
            return True
    return False
def checks_columns(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if (board[r][c]==symbol):
                count+=1
        if(count==3):
            print(symbol,'won')
            return True
    return False
def checks_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False

    
def won(symbol):
    return checks_rows(symbol) or checks_columns(symbol) or checks_diagonals(symbol)
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row(1 or 2 or 3):"))
        column=int(input("Enter column(1 or 2 or 3):"))
        if row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]=='-':
            break
        else:
            print("Invalid input, please enetr again")
    board[row-1][column-1]=symbol
def play():
    for chance in range(9):
        if(chance%2==0):
            print("X's turn")
            place(player1)
            if won(player1):
                print(f"{player1} won")
                return
        else: 
            print("O's turn")
            place(player2)
            if won(player2):
                print(f"{player2} won")
                return
    if not(won(player1)) and not(won(player2)):
        print("DRAW")
            
play()

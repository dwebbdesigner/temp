def get_player():
    player = None
    print("Player 1, Choose your character!")
    while player == None or player != 'X' and player != 'O':
        player = input("X or O: ").upper()
        if player == '0':
            print("I'm sorry. You must choose either X or O. Note that 'O' is not a zero.")
        if player != 'X' and player != 'O':
            print("I'm sorry. You must choose either X or O.")
        return player

def display_board(board):
    print(board[1],'|',board[2],'|',board[3])
    print('\u2014'*9)
    print(board[4],'|',board[5],'|',board[6])
    print('\u2014'*9)
    print(board[7],'|',board[8],'|',board[9],'\n')

def get_position(player,taken_numbers):
    position = 0
    while position not in range(1,10) or position in taken_numbers:
        position = input(f"Enter a position 1-9, {player}: ")
        try:
            position = int(position)
        except:
            print("I'm sorry. You must enter an integer from 1-9.")
            continue
        if position not in range(1,10):
            print("I'm sorry. You must enter an integer from 1-9.")
        if position in taken_numbers:
            print("I'm sorry. That position is taken!")
            continue
    taken_numbers.append(position)
    return position

def populate_board(player, position, board):
    board[position] = player

def win_check(board):
    winrow1=[board[1],board[2],board[3]]
    winrow2=[board[1],board[4],board[7]]
    winrow3=[board[1],board[5],board[9]]
    winrow4=[board[2],board[5],board[8]]
    winrow5=[board[3],board[5],board[7]]
    winrow6=[board[4],board[5],board[6]]
    winrow7=[board[7],board[8],board[9]]
    winrow8=[board[3],board[6],board[9]]
    winrows=[winrow1,winrow2,winrow3,winrow4,winrow5,winrow6,winrow7]
    for x in winrows:
        wincount = 0
        for y in x:
            if y != 'X':
                wincount = 0
                break
            wincount +=1
            if wincount == 3:
                return True
        wincount = 0
        for y in x:
            if y != 'O':
                wincount = 0
                break
            wincount +=1
            if wincount == 3:
                return True
    return False

def player_update(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

def score_update(player):
    global x_wins
    global o_wins
    if player == 'X':
        x_wins +=1
    else:
        o_wins +=1

def newgame():
    global board
    global player
    position = 0
    player = ''
    turncount = 0
    board = create_board()
    taken_numbers = []
    game_over = False
    player = get_player()
    display_board(board)
    while game_over == False:
        position = get_position(player,taken_numbers)
        populate_board(player, position, board)
        display_board(board)
        turncount += 1
        if turncount == 9:
            return True
        game_over = win_check(board)
        if game_over == False:
            player = player_update(player)
    score_update(player)
    print(f"Congratulations, {player}! You win! Press Enter to see high scores.")
    input()
    print("Wins:")
    print(f"X: {x_wins}")
    print(f"O: {o_wins}")

x_wins = 0
o_wins = 0

tutorial = ''

while tutorial != 'Y' or tutorial != 'N':
    tutorial = input("Would you like to see a tutorial? (Y or N) ").upper()
    if tutorial == 'Y':
        print('\n 1 | 2 | 3 ')
        print('\u2014'*11)
        print(' 4 | 5 | 6 ')
        print('\u2014'*11)
        print(' 7 | 8 | 9 \n')
        print("During the game, simply type a number 1-9 and hit Enter to place your mark on the board.")
        print("To keep track of scores, ensure that the same player uses X throughout all games, and vice versa.")
        input("Simply press Enter to begin the game.")
        break
    elif tutorial == 'N':
        break
    else:
        print("Invalid input.")

tie = ''

tie = newgame()

if tie == True:
    print("It's a tie! Press Enter to see high scores.")
    input()
    print("Wins:")
    print(f"X: {x_wins}")
    print(f"O: {o_wins}")

tie = ''

again = ''
while again != 'Y' or again != 'N':
    again = input("Would you like to play again? (Y or N) ").upper()
    if again == 'Y':
        newgame()
    elif again == 'N':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input.")

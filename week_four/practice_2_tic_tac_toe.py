from termcolor import colored

## View Game Board:

def view_board(game_board):
  for row in game_board:
    matrix = []
    for i in row:
      matrix.append(i)
    print(colored(matrix,'blue'))

# Check for Lateral Win
def lateral_win(board,win_order):
  for i in win_order:
    sum = 0
    for x in win_order:
      if board[i][x] == 'x':
        sum += 1
      elif board[i][x] == 'o':
        sum += 10
    if sum == 3:
      print(colored('Player 1 wins 🎉','green'))
      print(colored('Winning table:','blue'))
      view_board(board)
      quit()
    elif sum == 30:
      print(colored('Player 2 wins 🎉','green'))
      print(colored('Winning table:','blue'))
      view_board(board)
      quit()

# Check for Vertical Win 
def vertical_win(board,win_order):
  for i in win_order:
    sum = 0
    for x in win_order:
      if board[x][i] == 'x':
        sum += 1
      elif board[x][i] == 'o':
        sum +=10
    if sum == 3:
      print(colored('Player 1 wins 🎉','green'))
      print(colored('Winning table:','blue'))
      view_board(board)
      quit()
    elif sum == 30:
      print(colored('Player 2 wins 🎉','green'))
      print(colored('Winning table:','blue'))
      view_board(board)
      quit()


# Check for Diagonal Win version 1
def diagonal_win_v1(board,win_order):
  sum = 0
  for i in win_order:
    if board[i][i] == 'x':
      sum += 1
    elif board[i][i] == 'o':
      sum += 10
  if sum == 3:
    print(colored('Player 1 wins 🎉','green'))
    print(colored('Winning table:','blue'))
    view_board(board)
    quit()
  elif sum == 30:
    print(colored('Player 2 wins 🎉','green'))
    print(colored('Winning table:','blue'))
    view_board(board)
    quit()

# Check for Diagonal Win version 2
def diagonal_win_v2(board,win_order):
  sum = 0
  for i in win_order:
    if board[i][-(i+1)] == 'x':
      sum += 1
    elif board[i][-(i+1)] == 'o':
      sum += 10
  if sum == 3:
    print(colored('Player 1 wins 🎉','green'))
    print(colored('Winning table:','blue'))
    view_board(board)
    quit()
  elif sum == 30:
    print(colored('Player 2 wins 🎉','green'))
    print(colored('Winning table:','blue'))
    view_board(board)
    quit()

# Check for any win
def win_check(board):
  win_order = [0,1,2]
  lateral_win(board,win_order)
  vertical_win(board,win_order)
  diagonal_win_v1(board,win_order)
  diagonal_win_v2(board,win_order)


# Track game
def next_step(board,not_available,play_choice,turn):
  all_numbers = [0,1,2,3,4,5,6,7,8]
  if play_choice.isalpha():
    print("Must choose an integer available in table")
    view_board(board)
    turns(board,not_available,turn)
  elif int(play_choice) not in all_numbers:
    print("Must choose a value available in table")
    view_board(board)
    turns(board,not_available,turn)
  elif int(play_choice) in not_available:
    print("Must choose a value that hasn't been taken yet")
    view_board(board)
    turns(board,not_available,turn)
  else:
    row_num = -1
    for row in board:
      row_num += 1
      for i in row:
        if i == int(play_choice):
          index_val = row.index(i)
          not_available.append(i)
          if turn == True:
            board[row_num][index_val] = 'x'
            turn = False
          else:
            board[row_num][index_val] = 'o'
            turn = True
          win_check(board)
          view_board(board)
          turns(board,not_available,turn)


# Shift turns from player to player
def turns(game_board,not_available,player_1_turn):
  if len(not_available) == 9:
    print(colored('Nobody wins!','red'))
    play_again = input('Want to play again? Y/N \n')
    if play_again.upper() == 'Y':
      start()
    else:
      quit()
  while player_1_turn== True:
      player_1_play = input("Player 1: Pick position ")
      next_step(game_board,not_available,player_1_play,player_1_turn)
      
  while player_1_turn== False:
      player_2_play = input("Player 2: Pick position ")
      next_step(game_board,not_available,player_2_play,player_1_turn)
  

# Start the game!
def start():
  game_board = [[0,1,2],[3,4,5],[6,7,8]]
  not_available = []
  
  turn = True
  print(colored('Welcome to Tic-Tac-Toe!','green'))
  print('Player 1 will be x, Player 2 will be o')
  print(colored("Here's your table:",'blue'))
  view_board(game_board)
  print("Let's play! 💫")
  turns(game_board,not_available,turn)


start()

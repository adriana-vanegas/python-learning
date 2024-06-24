from termcolor import colored

## View Game Board:

def view_board(game_board):
  print(colored("Here's your table:",'blue'))
  for row in game_board:
    matrix = []
    for i in row:
      matrix.append(i)
    print(colored(matrix,'blue'))

## Allow player to select value
# def player_value():
  
#   while True:
#     player_1_as = input("Player 1, do you want to play as x or o?\n")
#     if player_1_as.lower() == 'x':
#       player_2_as = 'o'
#       return player_1_as, player_2_as
#     elif player_1_as.lower() == 'o':
#       player_2_as = 'x'
#       return player_1_as, player_2_as
#     else: 
#       print('Choose a value that is either x or o')



def next_step(board,not_available,play_choice,x_or_o,turn):
  if int(play_choice) in not_available:
    print("Must choose a value that hasn't been taken yet")
    view_board(board)
  else:
    row_num = -1
    for row in board:
      row_num += 1
      for i in row:
        if i == int(play_choice):
          index_val = row.index(i)
          not_available.append(i)
          board[row_num][index_val] = x_or_o
          view_board(board)

# def check_score(board):
#   for rows in board:
#     if rows == ['x','x','x']:
#       print(colored('x wins!','green'))  
#       quit()
#     if rows == ['o','o','o']:
#       print(colored('o wins!','green'))
#       quit()
  


def start():
  game_board = [[0,1,2],[3,4,5],[6,7,8]]
  not_available = [2]
  print(colored('Welcome to Tic-Tac-Toe!','green'))
  player_1_as, player_2_as = player_value()
  print(f'Great! Player 1: {player_1_as}, Player 2: {player_2_as}')

  view_board(game_board)
  print("Let's play! 💫")

  turn = 2
  while True:
    if turn%2==0:
      turn+= 1
      player_1_play = input("Player 1: Pick position ")
      next_step(game_board,not_available,player_1_play,player_1_as,turn)
      
      
    elif turn%2!=0:
      turn+= 1
      player_2_play = input("Player 2: Pick position ")
      next_step(game_board,not_available,player_2_play,player_2_as,turn)

start()

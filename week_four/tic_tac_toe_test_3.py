

board = [['o',1,'o'],
         [3,'x','o'],
         ['x','x','o']]

# lateral_win_build = [[[0,0],[0,1],[0,2]],
#                [[1,0],[1,1],[1,2]],
#                [[2,0],[2,1],[2,2]]]

win_order = [0,1,2]


# vertical_win_build = [[[0,0],[1,0],[2,0]],
#                 [[0,1],[1,1],[2,1]],
#                 [[0,2],[1,2],[2,2]]]

# diagonal_win_build = [[[0,0],[1,1],[2,2]],
#                 [[0,2],[1,1],[2,0]]]



# Lateral Win
def lateral_win(board,win_order):
  for i in win_order:
    sum = 0
    for x in win_order:
      if board[i][x] == 'x':
        sum += 1
      elif board[i][x] == 'o':
        sum += 10
    if sum == 3:
      print('x wins')
      quit()
    elif sum == 30:
      print('o wins')
      quit()

# Vertical Win 
def vertical_win(board,win_order):
  for i in win_order:
    sum = 0
    for x in win_order:
      if board[x][i] == 'x':
        sum += 1
      elif board[x][i] == 'o':
        sum +=10
    if sum == 3:
      print('x wins')
      quit()
    elif sum == 30:
      print('o wins')
      quit()


# Diagonal Win version 1
def diagonal_win_v1(board,win_order):
  sum = 0
  for i in win_order:
    if board[i][i] == 'x':
      sum += 1
    elif board[i][i] == 'o':
      sum += 10
  if sum == 3:
    print('x wins')
    quit()
  elif sum == 30:
    print('o wins')
    quit()


def diagonal_win_v2(board,win_order):
  sum = 0
  for i in win_order:
    if board[i][-(i+1)] == 'x':
      sum += 1
    elif board[i][-(i+1)] == 'o':
      sum += 10
  if sum == 3:
    print('Player 1 Wins')
    quit()
  elif sum == 30:
    print('Player 2 wins')
    quit()

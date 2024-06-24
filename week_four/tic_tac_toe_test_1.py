game_board = [[0,1,2],[3,4,5],[6,7,8]]

not_available = [2,3]

choice = 5

row_num = -1



for row in game_board:
  row_num += 1
  for i in row:
    if i == choice and i in not_available:
      print('Position is already taken.')
    elif i == choice and i not in not_available:
      print(row_num)
      index_val = row.index(choice)
      print(index_val)
      not_available.append(i)
      game_board_updates = game_board[row_num][index_val] = 'x'
      
    
  
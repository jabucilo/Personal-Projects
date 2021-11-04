import sys, random
x = int(sys.argv[1])
y = int(sys.argv[2])


board = []
boardsize = 10
for i in range(boardsize):
  board.append([" "] * boardsize)

def draw_x(pos):
  global board
  
  pos_x, pos_y = pos

  for row_indx in range(len(board)):
    left = pos_x - (row_indx - pos_y)
    right = pos_x + (row_indx - pos_y)
    
    if len(board[row_indx]) > left >= 0:
        if board[row_indx][left] == " ":
          board[row_indx][left] = "X"
        else:
          board[row_indx][left] = " "

    if len(board[row_indx]) > right >= 0:
        if board[row_indx][right] == "X":
          board[row_indx][right] = " "
        else:
          board[row_indx][right] = "X"

"""
  if board[pos_y][pos_x] == "X":
    board[pos_y][pos_x] = " "
  else:
    board[pos_y][pos_x] = "X"

  # down
  for row_indx in range(pos_y + 1, len(board)):
    left = pos_x - (row_indx - pos_y)
    right = pos_x + (row_indx - pos_y)
    
    if left >= 0:
      if board[row_indx][left] == " ":
        board[row_indx][left] = "X"
      else:
        board[row_indx][left] = " "

    if right < len(board[row_indx]):
      if board[row_indx][right] == "X":
        board[row_indx][right] = " "
      else:
        board[row_indx][right] = "X"

  # up
  for row_indx in reversed(range(pos_y)):
    left = pos_x + (row_indx - pos_y)
    right = pos_x - (row_indx - pos_y)

    if left >= 0:
      if board[row_indx][left] == " ":
        board[row_indx][left] = "X"
      else:
        board[row_indx][left] = " "

    if right < len(board[row_indx]):
      if board[row_indx][right] == "X":
        board[row_indx][right] = " "
      else:
        board[row_indx][right] = "X"
"""


"""for i in range(1):

  draw_x((x, y))

  print(f"\nX = {x}, Y = {y}:")
  for row in board:
    print(row)
  
  x = random.choice(range(boardsize))
  y = random.choice(range(boardsize))
"""
def convert_coords(board_x, board_y):
        return (self.margin + (board_x * self.circle_size)), (self.margin + (board_y * self.circle_size))

print(convert_coords(3, 4))
import pprint
'''
Project 1: Chess
Written by Pratyush Chakraborty

EXAMPLE CHANGE
'''

'''
In this project, students will model a chess board and chess piece movements using Python. 
This will require using all of the concepts learned in Lessons 1-3. Students are
recommended to use a 2-D list to model the chess board, and functions to organize the logic for
the movement patterns of each type of chess piece (Queen, King, Rook, etc.). However, the
implementation is left up to the student.

After modeling the chess board and chess pieces, the student’s code will take simple user input
that will attempt to place chess pieces on the chess board. The student’s code should remember
which pieces have been placed so far and figure out whether the user’s current piece can be
placed at the indicated square. If the indicated square is empty, the student’s code will place the
new piece on that square and remember that the square is occupied for future user input. At this
point, the student’s code will also calculate and print how many squares the new piece can move
based on its location, its piece type, and the vacancy of other squares on the chess board.

User input will be received in this format:
"<Piece Color> <Piece Name> <Square>"

Possible Piece Colors: White, Black
Possible Piece Names: Pawn, Knight, Bishop, Rook, Queen, King
Possible Squares: E4, G5, A7, etc 
(read how Chess square names work: https://en.wikipedia.org/wiki/Algebraic_notation_(chess) )

Example of User's interaction with the chess program:

What piece would you like to place, and where? --> W Bishop F2
White Bishop at F2 can move to 9 unique squares.
What piece would you like to place, and where? --> B Pawn A2
White Bishop at A2 can move to 2 unique squares.
What piece would you like to place, and where? --> B Rook A1
Black Rook at A1 can move to 8 unique squares.
What piece would you like to place, and where? --> STOP
Thank you for playing!

Some more notes:
-You will always start off with an empty board every time the user starts your program.
-As you can see above, you need to factor in the cases where white pieces and black pieces
 can capture each other. Pieces with the same color can't capture each other. This will impact
 how many moves a given piece on the board can make. On an empty board, the Black Rook at A1
 should be able to move to 14 unique squares. However, the White Pawn on A2 is in its way,
 which limits the Rook's movement. However, the Rook can still capture the pawn, which should
 count as a move. If the Pawn was Black instead of White, the Rook would not be able to capture
 it, and would only have 7 possible moves.
-Read up on how Pawns move. They are the weirdest piece:
 -Pawns capture diagonally, but move straight forward. 
 -Pawns can not be placed on the top-most or bottom-most rows for this program, as that would
  involve promotion in some cases, which is more complex than we need to get.
 -https://en.wikipedia.org/wiki/Pawn_(chess)
-You can assume your user will always follow the format indicated above. They will either give
 a valid chess piece placement request, or type STOP.
-You don't need to worry about limiting the number of times a certain Piece is placed. In real
 chess, there can only be 2 White Rooks. In your program, it is fine if the user places more than
 2 White Rooks on the board.

CHALLENGE:
Add functionality for allowing users to move pieces that are already placed on the board.
You can decide how you want the user to format their input to indicate that they are moving an existing
piece instead of placing a new one. You can assume that the user will always follow your format.

Hint: It might be easier to ask for the Color, Piece Type, and Square of the piece that users would like
to add to the board in three separate user input prompts (meaning use the input() function 3 times).

Hint: If you want to get all the user input (Color, Piece Type, Square) with just one input() function call,
consider storing that user input in a string, using Python's built-in split() function on that string, 
and using the list of 3 elements that the split() function returns to extract the color, piece type, and square.
The split() function will return a list with this format: [Color, Piece Type, Square].
Google "Python split()" for more info.

'''


'''
Takes a king's row and column as input,
and returns the total number of squares it can move to
given the other pieces on the board and the king's color.
'''
def king(piece_r,piece_c, board, color):
  kingtotalmoves = 0

  #up 
  if piece_r > 0 and board[piece_r - 1][piece_c] != color:
    kingtotalmoves = kingtotalmoves + 1
  #right
  if piece_c < 7 and board[piece_r ][piece_c + 1] != color:
    kingtotalmoves = kingtotalmoves + 1
  #down
  if piece_r < 7 and board[piece_r + 1][piece_c ] != color:
    kingtotalmoves = kingtotalmoves + 1
  #left
  if piece_c > 0 and board[piece_r][piece_c -1] != color:
    kingtotalmoves = kingtotalmoves + 1
  #up and right
  if piece_r > 0 and piece_c < 7 and board[piece_r - 1][piece_c + 1] != color:
    kingtotalmoves = kingtotalmoves + 1
  #up and left
  if piece_r > 0 and piece_c > 0 and board[piece_r - 1][piece_c - 1] != color:
    kingtotalmoves = kingtotalmoves + 1
  #down and right
  if piece_r < 7 and piece_c < 7 and board[piece_r + 1][piece_c + 1] != color:
    kingtotalmoves = kingtotalmoves + 1
  #down and left
  if piece_r < 7 and piece_c > 0 and board[piece_r + 1 ][piece_c - 1] != color:
    kingtotalmoves = kingtotalmoves + 1
  
  return kingtotalmoves

def rook(piece_r, piece_c, board, color):
  rooktotalmoves = 0
  for i in range(piece_c + 1, 8): # right
    if board[piece_r][i] != "W" and board[piece_r][i] != "B":
      rooktotalmoves = rooktotalmoves + 1
    elif board[piece_r][i] == color:
      break
    else:
      rooktotalmoves = rooktotalmoves + 1
      break

    
  for i in range(piece_c - 1, -1, -1): # left
    if board[piece_r][i] != "W" and board[piece_r][i] != "B":
      rooktotalmoves = rooktotalmoves + 1
    elif board[piece_r][i] == color:
      break
    else:
      rooktotalmoves = rooktotalmoves + 1
      break
      

  for i in range(piece_r + 1, 8):     # up
    if board[i][piece_c] != "W" and board[i][piece_c] != "B":
      rooktotalmoves = rooktotalmoves + 1
    elif board[i][piece_c] == color:
      break
    else:
      rooktotalmoves = rooktotalmoves + 1
      break
      

  for i in range(piece_r - 1, -1, -1): # down
    if board[i][piece_c] != "W" and board[i][piece_c] != "B":
      rooktotalmoves = rooktotalmoves + 1
    elif board[i][piece_c] == color:
      break
    else:
      rooktotalmoves = rooktotalmoves + 1
      break
            
             
  
  return rooktotalmoves

def bishop(piece_r, piece_c, board, color):
  bishoptotalmoves = 0
  #four diagonals

  # up and right  
  distance_to_top_side = piece_r - 0
  distance_to_right_side = 7 - piece_c

  curr_r = piece_r
  curr_c = piece_c
  for i in range(min(distance_to_top_side, distance_to_right_side)):
    curr_r = curr_r - 1
    curr_c = curr_c + 1
    if board[curr_r][curr_c] != "W" and board[curr_r][curr_c] != "B":
      bishoptotalmoves = bishoptotalmoves + 1
    elif board[curr_r][curr_c] == color:
      break
    else:
      bishoptotalmoves = bishoptotalmoves + 1
      break
    
  #up and left
  distance_to_top_side = piece_r - 0
  distance_to_left_side = piece_c - 0

  curr_r = piece_r
  curr_c = piece_c
  for i in range(min(distance_to_top_side, distance_to_left_side)):
    curr_r = curr_r - 1
    curr_c = curr_c - 1
    if board[curr_r][curr_c] != "W" and board[curr_r][curr_c] != "B":
      bishoptotalmoves = bishoptotalmoves + 1
    elif board[curr_r][curr_c] == color:
      break
    else:
      bishoptotalmoves = bishoptotalmoves + 1
      break

  #down and left
  distance_to_bottom_side = 7 - piece_r
  distance_to_left_side = piece_c - 0 

  curr_r = piece_r
  curr_c = piece_c
  for i in range(min(distance_to_bottom_side, distance_to_left_side)):
    curr_r = curr_r + 1 
    curr_c = curr_c - 1
    if board[curr_r][curr_c] != "W" and board[curr_r][curr_c] != "B":
      bishoptotalmoves = bishoptotalmoves + 1
    elif board[curr_r][curr_c] == color:
      break
    else:
      bishoptotalmoves = bishoptotalmoves + 1
      break

  #down and right
  distance_to_bottom_side = 7 - piece_r
  distance_to_right_side = 7 - piece_c

  curr_r = piece_r
  curr_c = piece_c
  for i in range(min(distance_to_bottom_side,distance_to_right_side)):
    curr_r = curr_r + 1
    curr_c = curr_c + 1
    if board[curr_r][curr_c] != "W" and board[curr_r][curr_c] != "B":
      bishoptotalmoves = bishoptotalmoves + 1
    elif board[curr_r][curr_c] == color:
      break
    else:
      bishoptotalmoves = bishoptotalmoves + 1
      break

  
  return bishoptotalmoves

def knight(piece_r, piece_c, board, color):
  knighttotalmoves = 0
  #up
  if piece_r >= 2:
    curr_r = piece_r - 2
    
    # up and left
    curr_c = piece_c - 1
    if piece_c > 0 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

      
    # up and right
    curr_c = piece_c + 1
    if piece_c < 7 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1



  #down
  if piece_r <= 5:
    curr_r = piece_r + 2

    #down and left
    curr_c = piece_c - 1
    if piece_c > 0 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

    #down and right
    curr_c = piece_c + 1
    if piece_c < 7 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

  #left
  if piece_c >= 2:
    curr_c = piece_c - 2

    #left and up
    curr_r = piece_r - 1
    if piece_r > 0 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

    #left and down
    curr_r = piece_r + 1
    if piece_r < 7 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

  #right
  if piece_c <= 5:
    curr_c = piece_c + 2

    #right and up
    curr_r = piece_r - 1
    if piece_r > 0 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

    #right and down
    curr_r = piece_r + 1
    if piece_r < 7 and board[curr_r][curr_c] != color:
      knighttotalmoves = knighttotalmoves + 1

  return knighttotalmoves

def pawn(piece_r, piece_c, board, color):
  pawntotalmoves = 0

  if piece_r == 0 or piece_r == 7:
    print("Not allowed")
    return 0

  else:
    if color == "W":
      # ONLY FOR CHECKING 1 SQUARE STRAIGHT MOVE
      if board[piece_r - 1][piece_c] != "B" and board[piece_r - 1][piece_c] != "W":
        pawntotalmoves = pawntotalmoves + 1
        # CHECKING FOR 2 SQUARES UP
        if piece_r == 6 and board[piece_r - 2][piece_c] != "B" and board[piece_r - 2][piece_c] != "W":
          pawntotalmoves = pawntotalmoves + 1

      # diagonal attack
      if board[piece_r - 1][piece_c - 1] == "B":
        pawntotalmoves = pawntotalmoves + 1
      if board[piece_r - 1][piece_c + 1] == "B":
        pawntotalmoves = pawntotalmoves + 1
      

    elif color == "B":
      #only for 1 up
      if board[piece_r + 1][piece_c] != "B" and board[piece_r + 1][piece_c] != "W":
        pawntotalmoves = pawntotalmoves + 1
        if piece_r == 1 and board[piece_r + 2][piece_c] != "B" and board[piece_r + 2][piece_c] != "W":
          pawntotalmoves = pawntotalmoves + 1


      #diagonal attacks
      if board[piece_r + 1][piece_c + 1] == "W":
        pawntotalmoves = pawntotalmoves + 1
      if board[piece_r + 1][piece_c - 1] == "W": 
        pawntotalmoves = pawntotalmoves + 1
      
    
    return pawntotalmoves

  
  # if the pawn is placed on row index  or 6,
  # immediately print "not allowed" and return 0
  # (don't do any of the other logic for finding pawn moves)

  # if the pawn is black and on row index 1, it can move 
  # down 1 or 2 squares

  # if the pawn is white and on row index 6, it can move
  # up 1 or 2 squares

  # don't need to consider the en passant capture

  # The max # of moves a pawn can make is 4
  # (when the pawn is on the starting row and it can capture 2 pieces)

  # NO NEED TO USE FOR LOOPS

  return pawntotalmoves

def chess():
  playGame = True

  board = [["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
          ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
          ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
          ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
          ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
          ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
          ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
          ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]]
  while playGame == True:
    user_input = input("What piece would you like to place, and where? --> ")
    if user_input != "stop":
      #game logic
      user_input = user_input.split()

      color = user_input[0]
      piece_type = user_input[1]
      square = user_input[2]
      
      piece_r = -1
      piece_c = -1
      for r in range(len(board)):
        for c in range(len(board[r])):
          if board[r][c] == square:
            piece_c = c
            piece_r = r

      if piece_r == -1 and piece_c == -1:
        print("There is already a piece there!")
        continue

      if piece_type == "King":
        kingtotalmoves = king(piece_r, piece_c, board, color)
        print("The King can Move to ", kingtotalmoves," Squares")

      elif piece_type == "Rook":
        rooktotalmoves = rook(piece_r, piece_c, board, color)
        print("Rook can move to ", rooktotalmoves, " Squares.")
      
      elif piece_type == "Bishop":
        bishoptotalmoves = bishop(piece_r,piece_c, board, color)
        print("Bishop can move to ", bishoptotalmoves, " Squares.")

      elif piece_type == "Queen":
        queentotalmoves = rook(piece_r, piece_c, board, color) + bishop(piece_r, piece_c, board, color)
        print("Queen can move to ", queentotalmoves, " Squares.")

      elif piece_type == "Knight":
        knighttotalmoves = knight(piece_r, piece_c, board, color)
        print("Knight can move to ", knighttotalmoves, " Squares.")
      
      elif piece_type == "Pawn":
        pawntotalmoves = pawn(piece_r, piece_c, board, color)
        if pawntotalmoves > 1 or pawntotalmoves == 0:
          print("Pawn can move to", pawntotalmoves, "squares")
        elif pawntotalmoves == 1:
          print("Pawn can move to", pawntotalmoves, "square")



      board[piece_r][piece_c] = color

    
    else:
      playGame = False

chess()








#King("G4")
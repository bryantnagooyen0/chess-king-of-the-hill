# Author: Bryant Nguyen
# GitHub username: bryantnagooyen0
# Date:3/12/25
# Description: Creates ChessVar class, class creates chess board and "King of the Hill" version of chess can be played through the class

class ChessVar:
    """
    ChessVar class initializes game board,current turn, game state, and turn counter
    Allows user to play king of the hill chess game through class
    """

    def __init__(self):
        self._board = [
  ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]

        self._turn = "WHITE"
        self._game_state = "UNFINISHED"
        self._turn_counter = 0

    def get_game_state(self):
        """
        Retrieves current state of the game
        :return: state can be "UNFINISHED", "WHITE_WON", or "BLACK_WON"
        """
        return self._game_state

    def print_board(self):
        """
        Prints the current chess board
        :return: prints each row of the board to be aligned
        """
        for row in self._board:
            print(row)

    def get_board(self):
        """
        retrieves the current chess board
        :return: returns board
        """
        return self._board

    def get_turn(self):
        """
        retrieves the current turn
        :return: will return "WHITE" if white's turn, "BLACK" if black's turn
        """
        return self._turn

    def letter_to_number(self,letter):
        """
        Converts letter into number, function used to convert column coordinate into integer
        :param letter:Letter of position "B" in "B1"
        :return: returns number according to index of alphabet "B" = 2
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return alphabet.index(letter.lower()) +1

    def convert_pos(self,position):
        """
        Converts position coordinate such as "B1" into rows and columns pertaining to the chess board
        :param position:"B1" B being the column and 1 being the row
        :return:returns row and column in integers
        """

        row = 8 - int(position[1])          # Because row 1 starts at the bottom of the list, we must iterate 8 times through list to access the bottom row hence the 8 - position
        column = int(self.letter_to_number(position[0])) - 1

        return row, column

    def get_piece(self,position):
        """
        Retrieves chess piece when given a position on board
        :param position:position on chess board
        :return:Returns the character/piece, "k" for black king
        """

        #Retrieves the row and column of beginning position and saves to row/col
        row_col_coord = self.convert_pos(position)
        row = row_col_coord[0]
        col = row_col_coord[1]

        #Saves current piece under current_piece and replaces position with ' '
        current_piece = self._board[row][col]
        return current_piece

    def game_won(self):
        """
        Helper function, when called this function changes the game_state to WON depending on which side makes the winning move
        :return: returns True
        """
        current_turn = self.get_turn()
        self._game_state = current_turn + "_WON"
        return True

    def _is_straight(self, beg_pos, end_pos):
        """
        Helper function for validate_move(), checks if move is valid for pieces that can move straight (Rook/Queen)
        :param beg_pos: beginning position
        :param end_pos: end position
        :return: returns True if valid move, false if not
        """
        #Initializes beginning row/column and ending row/column
        beg_row, beg_col = self.convert_pos(beg_pos)
        end_row, end_col = self.convert_pos(end_pos)

        #if beginning row and end row are the same then the move is horizontal
        if beg_row == end_row:
            if end_col > beg_col:
                step = 1
            else:
                step = -1
            for column in range(beg_col + step, end_col, step):
                if self._board[beg_row][column] != ' ':
                    return False
            return True

        #if beginning column and end column are the same then move is vertical
        if beg_col == end_col:
            if end_row > beg_row:
                step = 1
            else:
                step = -1

            for row in range(beg_row + step, end_row, step):
                if self._board[row][beg_col] != ' ':
                    return False
            return True

        return False


    def is_diagonal(self, beg_pos, end_pos):
        """
        Helper function for validate_move(), checks if move is valid for pieces that can move diagonally (Bishop/Queen)
        :param beg_pos: beginning position
        :param end_pos: end position
        :return: returns True if valid move, false if not
        """
        beg_row,beg_col = self.convert_pos(beg_pos)
        end_row,end_col = self.convert_pos(end_pos)

        #If move is not diagonal return False
        if abs(beg_row - end_row) != abs(beg_col - end_col):
            return False

        row_step = 1 if beg_row < end_row else -1
        col_step = 1 if beg_col < end_col else -1

        current_row = beg_row + row_step
        current_col = beg_col + col_step

        while current_row != end_row and current_col != end_col:
            if self._board[current_row][current_col] != " ":
                return False

            current_row += row_step
            current_col += col_step

        return True



    def validate_move(self,beg_pos, end_pos):
        """
        Validates whether a move being made adheres to the chess rules and the ChessVar program
        :param beg_pos: beginning position of piece
        :param end_pos: end position of piece
        :return: returns False if move is invalid, True if move is valid
        """
        #Saves chess piece under current_piece and beginning row/beg_col
        row_col_coord = self.convert_pos(beg_pos)
        beg_row = row_col_coord[0]
        beg_col = row_col_coord[1]

        #Initializes the current piece and current turn
        current_piece = self.get_piece(beg_pos)
        current_turn = self.get_turn()


        #If the current piece being moved does not belong to current turn
        if current_turn == "WHITE":
            if current_piece.islower():
                return False

        if current_turn == "BLACK":
            if current_piece.isupper():
                return False



        #If there is no piece in beginning position then move is invalid
        if current_piece == " ":
            return False


        # If the current turn is white and the end position is occupied by a white piece
        if current_turn == "WHITE":
            end_piece = self.get_piece(end_pos)
            if end_piece.isupper():
                return False

        #If the current turn is black and the end position is occupied by a black piece
        if current_turn == "BLACK":
            end_piece = self.get_piece(end_pos)
            if end_piece.islower():
                return False

        #Saves end position row and column
        end_row_col_coord = self.convert_pos(end_pos)
        end_row = end_row_col_coord[0]
        end_col = end_row_col_coord[1]


        #Validates for Black Pawn
        if current_piece == "p":
            #Initialize end piece
            end_piece = self.get_piece(end_pos)

            #Checks to make sure black pawn is only moving forward
            if beg_row >= end_row:
                return False

            #Checks to see if there is an opposing piece diagonal to current spot, if so then capturing is valid
            if end_row - beg_row == 1 and abs(end_col - beg_col) == 1 and end_piece.isupper():
                return True
            #Make sure the pawn moves vertically
            if beg_col != end_col:
                return False

            # If pawn is at starting row, pawn can move two spaces
            if beg_row == 1:
                #If the move is larger than two spaces
                if end_row - beg_row > 2:
                    return False
                #If pawn is moving one space, check if space in front is empty
                if end_row - beg_row == 1:
                    if self._board[end_row][end_col] != " ":
                        return False
                #If pawn is moving two spaces, check if both spaces are empty
                if end_row - beg_row == 2:
                    #If there is a piece in two spaces in front of pawn move is invalid
                    if self._board[beg_row + 1][beg_col] != " " and self._board[beg_row + 2][beg_col] != " ":
                        return False

            #If pawn is not at starting row, can only move one space and the space in front must be empty
            else:
                if end_row - beg_row > 1 and self._board[end_row][end_col] != " ":
                    return False



        #Validates for White Pawn
        if current_piece == "P":
            #Initialize end piece
            end_piece = self.get_piece(end_pos)

            #Checks to make sure white pawn is only moving forward
            if beg_row <= end_row:
                return False

            #Checks to see if there is an opposing piece diagonal to current spot, if so then capturing is valid
            if beg_row - end_row == 1 and abs(end_col - beg_col) == 1 and end_piece.islower():
                return True

            #Make sure the pawn moves vertically
            if beg_col != end_col:
                return False

            # If pawn is at starting row, pawn can move two spaces
            if beg_row == 6:
                #If the move is larger than two spaces
                if beg_row - end_row > 2:
                    return False
                #If pawn is moving one space, check if space in front is empty
                if beg_row - end_row == 1:
                    if self._board[end_row][end_col] != " ":
                        return False
                #If pawn is moving two spaces, check if both spaces are empty
                if beg_row - end_row == 2:
                    #If there is a piece in two spaces in front of pawn move is invalid
                    if self._board[beg_row - 1][beg_col] != " " and self._board[beg_row -2][beg_col] != " ":
                        return False

            #If pawn is not at starting row, can only move one space and the space in front must be empty
            else:
                if beg_row - end_row > 1 or self._board[end_row][end_col] != " ":
                    return False



        #Validates move for Bishop
        if current_piece.lower() == "b":
            if self.is_diagonal(beg_pos,end_pos) is False:
                return False

        #Validates move for Rook
        if current_piece.lower() == "r":
            if self._is_straight(beg_pos,end_pos) is False:
                return False
            else: return True

        #Validates move for Knight
        if current_piece.lower() == "n":
            if abs(beg_row - end_row) == 2 and abs(beg_col - end_col) == 1:
                return True

            if abs(beg_row - end_row) == 1 and abs(beg_col - end_col) == 2:
                return True

            return False

        #Validates move for Queen
        if current_piece.lower() == "q":
            if self.is_diagonal(beg_pos, end_pos) is True:
                return True
            if self._is_straight(beg_pos, end_pos) is True:
                return True
            return False

        #Validates move for King
        if current_piece.lower() == "k":
            if abs(beg_row - end_row) > 1 or abs(beg_col - end_col) > 1:
                return False




    def make_move(self,beg_pos,end_pos):
        """
        Moves chess piece at beginning position to end position
        :param beg_pos: beginning position of piece
        :param end_pos: end position of piece
        :return: returns False is move was invalid, True if move was made
        """

        #Validate that coordinates are within chess board, must be a-h and 1-8
        if beg_pos[0].lower() > 'h':
            return False
        if end_pos[0].lower() > 'h':
            return False
        if int(beg_pos[1]) > 8 or int(beg_pos[1]) < 1 :
            return False
        if int(end_pos[1]) > 8 or int(end_pos[1]) < 1 :
            return False

        #Retrieves the row and column of beginning position and saves to row/col
        row_col_coord = self.convert_pos(beg_pos)
        row = row_col_coord[0]
        col = row_col_coord[1]

        #Use validate_move() to check if move is valid, if its valid then move piece
        if self.validate_move(beg_pos, end_pos) is False:
            return False

        else:
            #Saves current piece under current_piece and replaces position with ' '
            current_piece = self._board[row][col]
            self._board[row][col] = ' '

            #Retrieves row and column of end position
            end_row_col_coord = self.convert_pos(end_pos)
            end_row = end_row_col_coord[0]
            end_col = end_row_col_coord[1]
            end_piece = self._board[end_row][end_col]

            #If current piece captures opponent's king, increment turn counter and return game_won()
            if end_piece.lower() == "k":
                self._board[end_row][end_col] = current_piece
                return self.game_won() and True

            #Places current piece at end position
            self._board[end_row][end_col] = current_piece

            #If current piece is a king and moves to central squares (d4,d5,e4,e5) game is won
            if current_piece.lower() == "k" and end_pos.lower() in {"d4", "d5", "e4", "e5"}:
                return self.game_won() and True

            else:
                #Increment turn counter
                self._turn_counter += 1

                if self._turn_counter % 2 == 0:
                    self._turn = "WHITE"
                else:
                    self._turn = "BLACK"
                return True


# Example usage and demonstration
if __name__ == "__main__":
    # Create a new chess game
    game = ChessVar()
    
    print("Welcome to ChessVar - King of the Hill!")
    print("Initial board state:")
    game.print_board()
    print(f"Current turn: {game.get_turn()}")
    print(f"Game state: {game.get_game_state()}")
    print()
    
    # Example moves
    print("Making some example moves:")
    
    # White pawn moves
    print("1. White pawn from e2 to e4")
    result = game.make_move("e2", "e4")
    print(f"Move result: {result}")
    game.print_board()
    print(f"Current turn: {game.get_turn()}")
    print()
    
    # Black pawn moves
    print("2. Black pawn from e7 to e5")
    result = game.make_move("e7", "e5")
    print(f"Move result: {result}")
    game.print_board()
    print(f"Current turn: {game.get_turn()}")
    print()
    
    # White knight moves
    print("3. White knight from g1 to f3")
    result = game.make_move("g1", "f3")
    print(f"Move result: {result}")
    game.print_board()
    print(f"Current turn: {game.get_turn()}")
    print()
    
    print("Game demonstration complete!")
    print(f"Final game state: {game.get_game_state()}")
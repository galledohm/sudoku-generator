import random

class SudokuBoard:
    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.__reset_board()
    
    def __reset_board(self):
        self.board = [[0]*9 for _ in range(9)]

    def get_num_subsquare(self, row: int, col: int):
        """Returns the subsquare location number:
        0: Upper left
        1: Upper center 
        ..."""
        square_numbers = [[0,1,2],[3,4,5],[6,7,8]]
        return square_numbers[row // 3][col // 3]
    
    def get_subsquare(self, num: int):
        row_start = (num // 3) * 3 # Integer division to find the row start
        col_start = (num % 3) * 3 # Module operator to find the column start
        return [self.board[row_start + i][col_start:col_start + 3] for i in range(3)] # type: ignore
    
    def set_subsquare(self, num:int, subsquare):
        row_start = (num // 3) * 3
        col_start = (num % 3) * 3
        for i in range(3):  
            self.board[row_start + i][col_start:col_start + 3] = subsquare[i] # type: ignore
    
    def generate_subsquare(self):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        return [numbers[i*3:(i+1)*3] for i in range(3)] # type: ignore
    
    def generate_diagonal(self):
        for i in range(3):
            self.set_subsquare(i*4, self.generate_subsquare())
    
    def check_subsquare(self, num: int):
        """ Check if a subsquare contains no duplicates """
        subsquare = self.get_subsquare(num)
        flat_list = [num for row in subsquare for num in row]
        filled_numbers = [num for num in flat_list if num != 0]
        return (len(filled_numbers) == len(set(filled_numbers)))
    
    def check_row(self, row: int):
        """ Check if a row contains no duplicates """
        # Filter out empty cells (0s) and check for duplicates among filled cells
        filled_numbers = [num for num in self.board[row] if num != 0]
        # Check that there are no duplicates by comparing length with set length
        return len(filled_numbers) == len(set(filled_numbers))
    
    def check_column(self, col: int):
        """ Check if a column contains no duplicates """
        column = [self.board[i][col] for i in range(9)]
        filled_numbers = [num for num in column if num != 0]
        return (len(filled_numbers) == len(set(filled_numbers)))
    
    def fill_remaining(self, row: int, col: int):
        """ Placeholder for a backtracking algorithm to fill the remaining cells. """
        # End condition
        if row == 9:
            return True
        
        # Next row (final column reached)
        if col == 9:
            return self.fill_remaining(row + 1, 0)
        
        if self.board[row][col] != 0:
            return self.fill_remaining(row, col + 1)
        
        for i in range(1,10):
            self.board[row][col] = i
            if self.check_subsquare(self.get_num_subsquare(row,col)) & self.check_row(row) & self.check_column(col):
                if self.fill_remaining(row, col + 1):
                    return True
            # Always reset the cell when backtracking, regardless of validation result
            self.board[row][col] = 0

        return False
    
    def generate_full_board(self):
        """ Placeholder for a full board generation algorithm. """
        self.generate_diagonal()
        # Further implementation needed to fill the rest of the board correctly.
        return self.fill_remaining(0,0)

    def Board2Code(self):
        code = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                code.append(self.board[i][j])

        return ''.join(map(str,code))

if __name__ == "__main__":
    # Example usage
    sudoku = SudokuBoard()
    print (sudoku.Board2Code())
    if sudoku.generate_full_board():
        print("SUCCESS! Full board generated:")
        for row in sudoku.board:
            print(row)
        print(sudoku.Board2Code())
    else:
        print("Failed to generate board")
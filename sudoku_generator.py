"""Sudoku Board Generator using backtracking algorithms.

This module implements a complete Sudoku puzzle generator that uses
recursive backtracking to fill a 9x9 grid following standard Sudoku rules.
"""

import random


class SudokuBoard:
    """A Sudoku board generator and validator using backtracking algorithms.
    
    This class provides methods to generate complete Sudoku puzzles,
    validate board states, and manipulate 3x3 subsquares.
    """

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
        """Get the 3x3 subsquare by its number (0-8)."""
        row_start = (num // 3) * 3  # Integer division to find the row start
        col_start = (num % 3) * 3  # Module operator to find the column start
        return [self.board[row_start + i][col_start:col_start + 3] for i in range(3)]

    def set_subsquare(self, num: int, subsquare):
        """Set a 3x3 subsquare by its number (0-8)."""
        row_start = (num // 3) * 3
        col_start = (num % 3) * 3
        for i in range(3):
            self.board[row_start + i][col_start:col_start + 3] = subsquare[i]

    def generate_subsquare(self):
        """Generate a random valid 3x3 subsquare with numbers 1-9."""
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        return [numbers[i*3:(i+1)*3] for i in range(3)]

    def generate_diagonal(self):
        """Generate the three diagonal subsquares (0, 4, 8)."""
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
            if (self.check_subsquare(self.get_num_subsquare(row, col)) and
                    self.check_row(row) and self.check_column(col)):
                if self.fill_remaining(row, col + 1):
                    return True
            # Always reset the cell when backtracking, regardless of validation result
            self.board[row][col] = 0

        return False

    def generate_full_board(self):
        """Generate a complete valid Sudoku board."""
        self.generate_diagonal()
        return self.fill_remaining(0, 0)

    def board_to_code(self):
        """Convert the board to an 81-character string representation."""
        code = []
        for row in self.board:
            for cell in row:
                code.append(cell)
        return ''.join(map(str, code))

if __name__ == "__main__":
    # Example usage
    sudoku = SudokuBoard()
    print(sudoku.board_to_code())
    if sudoku.generate_full_board():
        print("SUCCESS! Full board generated:")
        for board_row in sudoku.board:
            print(board_row)
        print(sudoku.board_to_code())
    else:
        print("Failed to generate board")

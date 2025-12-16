"""
Simple recursion example for Sudoku-like backtracking
Using a 4x4 board for easy understanding
Each 2x2 subsquare must contain numbers 1-4 without repetition
"""

class SimpleBoard:
    def __init__(self):
        # 4x4 board with some pre-filled numbers
        self.board = [
            [1, 0, 0, 0],
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 3, 0, 0]
        ]
        self.call_count = 0
        
    def print_board(self):
        print("Current board:")
        for row in self.board:
            print(row)
        print()
    
    def is_valid(self, row, col, num):
        """Check if placing num at [row][col] is valid"""
        
        # Check row - no duplicates
        for c in range(4):
            if c != col and self.board[row][c] == num:
                return False
        
        # Check column - no duplicates  
        for r in range(4):
            if r != row and self.board[r][col] == num:
                return False
        
        # Check 2x2 subsquare - no duplicates
        start_row = (row // 2) * 2
        start_col = (col // 2) * 2
        
        for r in range(start_row, start_row + 2):
            for c in range(start_col, start_col + 2):
                if (r != row or c != col) and self.board[r][c] == num:
                    return False
        
        return True
    
    def solve(self, row=0, col=0):
        """Backtracking solver with detailed tracing"""
        self.call_count += 1
        indent = "  " * (self.call_count - 1)
        
        print(f"{indent}📞 CALL #{self.call_count}: solve({row}, {col})")
        
        # Base case: reached the end
        if row == 4:
            print(f"{indent}✅ SUCCESS! Reached end of board")
            return True
        
        # Move to next row when we reach end of current row
        if col == 4:
            print(f"{indent}➡️  End of row {row}, moving to row {row+1}")
            result = self.solve(row + 1, 0)
            if result:
                print(f"{indent}✅ Row {row+1} solved successfully")
            else:
                print(f"{indent}❌ Row {row+1} failed")
            return result
        
        # If cell is already filled, skip to next cell
        if self.board[row][col] != 0:
            print(f"{indent}⏭️  Cell [{row}][{col}] = {self.board[row][col]} (already filled)")
            result = self.solve(row, col + 1)
            if result:
                print(f"{indent}✅ Next cell solved successfully")
            else:
                print(f"{indent}❌ Next cell failed")
            return result
        
        # Try numbers 1-4 in empty cell
        print(f"{indent}🔍 Cell [{row}][{col}] is empty, trying numbers 1-4...")
        
        for num in range(1, 5):
            print(f"{indent}  🧪 Trying {num} at [{row}][{col}]...")
            
            if self.is_valid(row, col, num):
                print(f"{indent}  ✅ {num} is valid! Placing it...")
                self.board[row][col] = num
                self.print_board()
                
                print(f"{indent}  🔄 Recursing to next cell...")
                if self.solve(row, col + 1):
                    print(f"{indent}  🎉 SUCCESS! {num} at [{row}][{col}] led to solution")
                    return True
                
                print(f"{indent}  ⏪ BACKTRACK! {num} at [{row}][{col}] didn't work, removing...")
                self.board[row][col] = 0
                self.print_board()
            else:
                print(f"{indent}  ❌ {num} is invalid (constraint violation)")
        
        print(f"{indent}💥 DEAD END! No number works at [{row}][{col}]")
        return False

# Run the example
if __name__ == "__main__":
    print("🎯 RECURSION DEMONSTRATION - 4x4 Sudoku-like puzzle")
    print("=" * 50)
    
    board = SimpleBoard()
    print("Initial board:")
    board.print_board()
    
    print("Starting recursive solve...")
    print("=" * 50)
    
    if board.solve():
        print("\n🎉 FINAL SOLUTION:")
        board.print_board()
    else:
        print("\n💔 No solution found")
    
    print(f"Total recursive calls: {board.call_count}")
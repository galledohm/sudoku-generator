# Sudoku Generator

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python implementation of a Sudoku puzzle generator using a simple backtracking algorithm. This project demonstrates recursive problem-solving techniques and constraint satisfaction algorithms.

## Table of Contents

- [Sudoku Generator](#sudoku-generator)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Basic Usage](#basic-usage)
    - [Running the Examples](#running-the-examples)
  - [Project Structure](#project-structure)
  - [Algorithm Details](#algorithm-details)
    - [Core Components](#core-components)
    - [Key Methods](#key-methods)
  - [Examples](#examples)
    - [Generated Board Output](#generated-board-output)
    - [Educational Example](#educational-example)
  - [Contributing](#contributing)
    - [Development Setup](#development-setup)
  - [License](#license)
  - [Future Improvements](#future-improvements)

## Features

- **Full Sudoku Board Generation**: Creates complete 9×9 Sudoku puzzles
- **Backtracking Algorithm**: Uses recursive backtracking puzzle solving
- **Constraint Validation**: Ensures Sudoku rules are maintained (rows, columns, and 3×3 subsquares)
- **Diagonal Generation**: Pre-fills diagonal subsquares for optimization
- **Board Serialization**: Converts boards to string format for easy storage/transmission
- **Educational Examples**: Includes simplified 4×4 example with detailed tracing

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/sudoku-generator.git
   cd sudoku-generator
   ```

2. **Requirements:**
   - Python 3.7 or higher
   - No external dependencies required (uses only standard library)

## Usage

### Basic Usage

```python
from sudoku_generator import SudokuBoard

# Create a new Sudoku board
sudoku = SudokuBoard()

# Generate a complete board
if sudoku.generate_full_board():
    print("SUCCESS! Full board generated:")
    for row in sudoku.board:
        print(row)
else:
    print("Failed to generate board")

# Get board as string
board_code = sudoku.Board2Code()
print(f"Board code: {board_code}")
```

### Running the Examples

```bash
# Run the main Sudoku generator
python sudoku_generator.py

# Run the educational 4x4 example with detailed tracing
python example/recursion_example.py
```

## Project Structure

```bash
sudoku-generator/
├── README.md                    # Project documentation
├── sudoku_generator.py          # Main Sudoku generator implementation
└── example/
    └── recursion_example.py     # Educational 4x4 backtracking example
```

## Algorithm Details

### Core Components

1. **SudokuBoard Class**: Main class handling board operations
   - Board initialization and reset
   - Subsquare management (get, set, generate)
   - Validation methods (rows, columns, subsquares)
   - Backtracking solver

2. **Backtracking Algorithm** (`fill_remaining`):
   - Recursively fills empty cells
   - Validates constraints at each step
   - Backtracks when constraints are violated
   - Returns `True` for successful completion

3. **Constraint Validation**:
   - **Rows**: No duplicate numbers 1-9
   - **Columns**: No duplicate numbers 1-9
   - **3×3 Subsquares**: No duplicate numbers 1-9

### Key Methods

| Method | Description |
|--------|-------------|
| `generate_diagonal()` | Pre-fills the three diagonal 3×3 subsquares |
| `fill_remaining()` | Recursive backtracking to fill remaining cells |
| `check_subsquare()` | Validates 3×3 subsquare constraints |
| `check_row()` | Validates row constraints |
| `check_column()` | Validates column constraints |
| `Board2Code()` | Serializes board to 81-character string |

## Examples

### Generated Board Output

```bash
[6, 2, 8, 4, 3, 9, 5, 1, 7]
[1, 9, 4, 7, 5, 2, 3, 8, 6]
[3, 7, 5, 6, 8, 1, 9, 4, 2]
[8, 5, 9, 1, 2, 4, 7, 6, 3]
[4, 3, 1, 9, 7, 6, 2, 5, 8]
[2, 6, 7, 3, 1, 5, 8, 9, 4]
[5, 8, 6, 2, 9, 7, 4, 3, 1]
[7, 1, 2, 5, 4, 3, 6, 2, 9]
[9, 4, 3, 8, 6, 1, 1, 7, 5]
```

### Educational Example

The [recursion_example.py](example/recursion_example.py) provides a detailed trace of the backtracking algorithm on a simplified 4×4 board, showing:

- Recursive call stack
- Decision points
- Backtracking steps
- Constraint validation

## Contributing

Contributions are welcome! Here are some ways you can help:

1. **Bug Reports**: Open an issue describing the bug
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Fork the repo and submit a pull request
4. **Documentation**: Improve documentation and examples

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements

- [ ] Puzzle difficulty levels
- [ ] Puzzle solver (given partial board)
- [ ] GUI interface
- [ ] Performance optimizations
- [ ] Unit tests
- [ ] Multiple solution detection
- [ ] Puzzle uniqueness validation

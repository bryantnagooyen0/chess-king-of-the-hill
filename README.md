# ChessVar - King of the Hill Chess Game

A Python implementation of a chess variant called "King of the Hill" where the goal is to either capture the opponent's king or move your own king to the center squares (d4, d5, e4, e5).

## Features

- Complete chess game implementation with all standard pieces
- "King of the Hill" variant rules
- Move validation for all chess pieces
- Turn-based gameplay
- Board state tracking
- Game state management (UNFINISHED, WHITE_WON, BLACK_WON)

## How to Play

1. **Standard Chess Rules**: All pieces move according to standard chess rules
2. **King of the Hill Victory**: Move your king to any of the center squares (d4, d5, e4, e5) to win
3. **Traditional Victory**: Capture the opponent's king to win

## Game Setup

The game starts with the standard chess board layout:
- White pieces are uppercase letters (R, N, B, Q, K, P)
- Black pieces are lowercase letters (r, n, b, q, k, p)
- White moves first

## Usage

### Running the Demo

```bash
python ChessVar.py
```

This will run a demonstration showing:
- Initial board state
- Example moves (e2-e4, e7-e5, g1-f3)
- Board updates after each move
- Turn tracking

### Using the ChessVar Class

```python
from ChessVar import ChessVar

# Create a new game
game = ChessVar()

# Print the current board
game.print_board()

# Make a move (format: "e2" to "e4")
result = game.make_move("e2", "e4")
print(f"Move successful: {result}")

# Check game state
print(f"Game state: {game.get_game_state()}")
print(f"Current turn: {game.get_turn()}")
```

## Piece Notation

- **R/r**: Rook
- **N/n**: Knight  
- **B/b**: Bishop
- **Q/q**: Queen
- **K/k**: King
- **P/p**: Pawn

## Coordinate System

The game uses standard chess notation:
- Files (columns): a-h (left to right)
- Ranks (rows): 1-8 (bottom to top)
- Example: "e4" means column e, row 4

## Methods

### Core Game Methods
- `make_move(beg_pos, end_pos)`: Attempts to move a piece from beginning to end position
- `get_game_state()`: Returns current game state
- `get_turn()`: Returns whose turn it is
- `print_board()`: Displays the current board state

### Utility Methods
- `get_board()`: Returns the board array
- `get_piece(position)`: Gets the piece at a given position
- `validate_move(beg_pos, end_pos)`: Validates if a move is legal

## Author

**Bryant Nguyen**  
GitHub: [bryantnagooyen0](https://github.com/bryantnagooyen0)  
Date: 3/12/25

## License

This project is open source and available under the MIT License.


def find_next_empty(puzzle):
    #finds next void space
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
                
    return None, None # if no blank spaces


def is_valid(puzzle, guess, row, col):
    # returns True if is valid
    # chack the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # check the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
        
    # check the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
                
    return True


def solve_sudoku(puzzle):
    # 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    
    if row is None:
        return True
        
    # 2: if there is space put a number
    for guess in range(1, 10):
        # 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
                
        # 5: if not valid or the guess do not solve the puzzle
        puzzle[row][col] = -1
        
    # 6: if the guesses do not work, the puzzle is unsolvable
    return False
    
    
if __name__ == '__main__':
    example_board = [
        [-1, -1, -1,   8, -1, -1,   -1, -1, 5],
        [4, -1, -1,   -1, 3, 5,   -1, 2, -1],
        [-1, 3, -1,   7, 1, -1,   -1, -1, -1],
        
        [-1, -1, 6,   -1, -1, -1,   -1, 4, -1],
        [-1, 8, -1,   -1, 9, 1,   -1, -1, 2],
        [-1, -1, -1,   5, -1, -1,   -1, -1, -1],

        [-1, -1, -1,   -1, 7, -1,   -1, -1, -1],
        [-1, 9, -1,   -1, 2, 3,   -1, -1, 1],
        [8, -1, -1,   -1, -1, -1,   9, -1, -1]]
        
    print(solve_sudoku(example_board))
    print(example_board)

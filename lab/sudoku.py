# write a program that checks if a sudoku solution is valid. ✅
# check if the numbers 1-9 are present in each row, column, and 3x3 subgrid. ✅
# return Yes if the solution is valid, No otherwise.✅
# input is a 9x9 grid of numbers.✅
# use a nested list to represent the grid.✅
# ensure the rows and colums have no duplicates. ✅


def is_valid_sudoku(grid):
    # check if the numbers 1-9 are present in each row
    for row in grid:
        # Check if row contains exactly 1-9 (no duplicates, all present)
        if sorted(row) != list(range(1, 10)):
            return "No"
    # check if the numbers 1-9 are present in each column
    for col in range(9):
        # Extract the column
        column = [grid[row][col] for row in range(9)]
        # Check if column contains exactly 1-9 (no duplicates, all present)
        if sorted(column) != list(range(1, 10)):
            return "No"
    # check if the numbers 1-9 are present in each 3x3 subgrid
    for row in range(0, 9, 3): # this creates the 3x3 sub-squares rows
        for col in range(0, 9, 3): # this creates the 3x3 sub-squares columns
            sub_squares = [grid[i][j] for i in range(row, row + 3) for j in range(col, col + 3)] # this creates the 3x3 sub-squares
            for num in range(1, 10): # this checks if the numbers 1-9 are present in the 3x3 sub-squares
                if num not in sub_squares:
                    return "No"
    return "Yes" # if all the numbers 1-9 are present in each row, column, and 3x3 subgrid, return Yes

# test the function
print(is_valid_sudoku([[2,9,5,7,4,3,8,6,1], [4,3,1,8,6,5,9,2,7], [8,7,6,1,9,2,5,4,3], [3,8,7,4,5,9,2,1,6], [6,1,2,3,8,7,4,9,5], [5,4,9,2,1,6,7,3,8], [7,6,3,5,2,4,1,8,9], [9,2,8,6,7,1,3,5,4], [1,5,4,9,3,8,6,7,2]])) # this is the test case
print(is_valid_sudoku([[1,9,5,7,4,3,8,6,2], [4,3,1,8,6,5,9,2,7], [8,7,6,1,9,2,5,4,3], [3,8,7,4,5,9,2,1,6], [6,1,2,3,8,7,4,9,5], [5,4,9,2,1,6,7,3,8], [7,6,3,5,2,4,1,8,9], [9,2,8,6,7,1,3,5,4], [2,5,4,9,3,8,6,7,1]]))

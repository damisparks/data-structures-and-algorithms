# Solution for Practice Exercise 2
correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku()


def check_sudoku(sudoku_square):
    """
    Define a procedure check_sudoku that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True
    If the input is a valid sudoku square and returns the boolean False otherwise.
    A valid sudoku square satisfies these two properties:
    - Each column of the square contains each of the whole numbers from 1 to n exactly once.
    - Each row of the square contains each of the whole numbers from 1 to n exactly once.
    """
    for row in sudoku_square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(sudoku_square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(sudoku_square[0])):
        # We do the same here for each column in the sudoku_square.
        check_list = list(range(1, len(sudoku_square[0]) + 1))
        for row in sudoku_square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True

print(check_sudoku(correct))


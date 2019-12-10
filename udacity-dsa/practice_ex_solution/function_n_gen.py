## Solution for Practice Exercise 1. 
def prod(a,b):
    return a * b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output

# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

## Solution for Practice Exercise 2 
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

## Define a function check_sudoku() 

def check_sudokuy():
    """
    Define a procedure check_sudoku that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True
    If the input is a valid sudoku square and returns the boolean False otherwise.
    A valid sudoku square satisfies these two properties:
    - Each column of the square contains each of the whole numbers from 1 to n exactly once.
    - Each row of the square contains each of the whole numbers from 1 to n exactly once.
    """
    return 'Work in Progress.'






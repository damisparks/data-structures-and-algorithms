# Function and Generator 
## Function 
A function is a block of code which only runs when it is called. Information can be passed to functions as parameter.
In Python every function returns a value. In case you do not specify a return value explicitly, Python will return `None` from that function.

> Function are used to handle repetitive task. **Best practice is to have one function per task**
In Python a function is defined using the `def` keyword:
```python

def doSomething():
    print('Hello function')

## expected return value is "Hello function"
doSomething() ## Calling the function --> doSomething


## Function think 🤔
def think(yourThought):
    print('You are thinking about ' + str(yourThought))

mythought = 'Coding'
think(mythought) ## Calling the function --> think
## expected return value is "You are thinking about Coding"

# Example function 1: return the sum of two numbers.
def sum(a, b):
    return a+b

# Example function 2: return the size of list, and modify the list to now be sorted.
def list_sort(my_list):
    my_list.sort()
    return len(my_list),  my_list

```

## Generator
A **generator** in Python is said to be similar to a function except instead of returning a value and exiting a process, a **generator**  pauses the process, saving its state for next time. Generator functions allow you to declare a function that behaves like an iterator. Generators introduce the `yield` statement to Python. It works a bit like `return` because it returns a value.

A generator becomes very useful when dealing with very large collections of data that you don’t want to store in memory all at once. So basically it saves memory space. 

> The next time the function is called, execution continues from where it left off, with the same variable values it had before yielding.

## Example. 

*To create the next successive even number simply call `next()` on the generator object, and it will yield the next iteration. After `yield` is called, everything in the state of the generator function freezes, and the value is returned. When the generator is called again with `next()`, it picks back up right where it stopped at `yield` from before.*
```python 
# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))
```
## Practice Exercise 1. 

```python 
def prod(a,b):
    # TODO change output to the product of a and b
    output = 0
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product


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

```

## Practice Exercise 2 
```python 
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
               
# Define a function check_sudoku() here:


#print(check_sudoku(incorrect))
#>>> False

#print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False

#print(check_sudoku(incorrect5))
#>>> False

```


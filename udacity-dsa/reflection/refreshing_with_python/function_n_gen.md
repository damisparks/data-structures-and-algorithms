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

```

## Generator
A **generator** in Python is said to be similar to a function except instead of returning a value and exiting a process, a **generator**  pauses the process, saving its state for next time. Generator functions allow you to declare a function that behaves like an iterator. Generators introduce the `yield` statement to Python. It works a bit like `return` because it returns a value.

A generator becomes very useful when dealing with very large collections of data that you don’t want to store in memory all at once. So basically it saves memory space

> The next time the function is called, execution continues from where it left off, with the same variable values it had before yielding.

## Practice Exercise. 


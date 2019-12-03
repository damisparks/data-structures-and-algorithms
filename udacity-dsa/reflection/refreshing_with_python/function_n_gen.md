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
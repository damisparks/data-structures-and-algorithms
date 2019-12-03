# Control Structure

## Iteration with loops. 
There are several ways to iterate in python. The traditional method can be used when an `i` is initiate then **increased** / **decreased** until it reaches the end value depending on the functionality to be achieved. 


Python's `for` loops are `for-each` in nature like that of [JavaScript for each](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach). This means that when you are iterating using a `for loop` over a list, you actually iterate over the items of that list. If you need the index value from the list, you can use `enumerate`

```python

## Examples of iteration with for loops.

sample_list = [0, 1, 2, 3, 4, 5]

for item in sample_list: 
    print('Item value : ' + str(item))

## Print each index and its value pair.
for i, value in enumerate(my_list):
    print('The index is: ' + str(i) + '. The value at i is: ' + str(value))


## Using a while loop to print 0-9 
count = 0
while(count < 10):
    print(count)
    count += 1

## Print each key and dictionary value. 
## Note that you can use the "in" keyword to iterate over dictionary keys.
## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])

```

* [Read more about `in` Python official docs](https://docs.python.org/3.4/reference/expressions.html#in)

* [Google Education](https://developers.google.com/edu/python/dict-files)

## Conditional Statements
A **control statement** is a statement that determines whether other statements will be executed aiding our decision process. The statement is  either `true` or `false`. These statements are structured using comparison operator like :
* greater than `(>)`
* less than `(<)`,
* equal to `(==)`.
To achieve control flow using conditional statements, we make use of **Python's** : 
* `if`
* `elif` (generally use as the last comparison)
* `else` means *else if*

> Example 😀
```python 

num = 10
if num < 10:
    print('This number is less than 10.')
elif num == 10:
    print('This number equals 10.')
else:
    print('This number is greater than 10.')
## Expected solution : The number equals 10.
```

## Your turn to Practice
### Practice Exercise 1 
> In the following exercise you will finish writing `smallest_positive` which is a function that finds the smallest positive number in a list.

```python
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    
    return 0

## Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
## Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
## Correct output: 0.2

``` 

## Practice Exercise 2
> ### Write a Python program to count the number of even and odd numbers from a series of numbers. 

**Example**  if `numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)`. 
Expected Output :
* Number of even numbers : 5
* Number of odd numbers : 4*

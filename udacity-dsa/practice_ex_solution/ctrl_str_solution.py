## Question 1 
## What would be the output of the following code?
my_dict = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output) # [0,1,2,3]


## Practice Exercise 1 Solution
def smallest_positive(in_list):
    # Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    if len(in_list) == 1:
        return None
    smallest = max(in_list)
    for num in in_list:
        if all([num < smallest, num > 0]):
            smallest = num
    return smallest

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

## Practice Exercise 2 Solution
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers : ",count_even)
print("Number of odd numbers : ",count_odd)

## Number of even numbers : 4                                                   
## Number of odd numbers : 5 

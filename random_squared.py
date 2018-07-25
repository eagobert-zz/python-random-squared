#Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
import random

#Create an empty list
random_numbers = []

#Create a for loop that stops at 20 numbers
for number in range(20):
    #Generate random #s from 0 to 49 and append to list
    random_numbers.append(random.randint(0,49))

# Print the list of random numbers. Note: Placed print outside of the for loop to print a single list
print(random_numbers)

#With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].
numbers_squared = [n * n for n in random_numbers]
print(numbers_squared)
# Using the list Constructor

# Creating an empty array
my_array = []

# Creating an array with elements
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana']

print(type(numbers))
print(type(fruits))

# Using List Comprehension

# Creating an array of squares
squares = [x**2 for x in range(1, 6)]

print(squares)

# Creating an array of even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)

# Using the numpy.array Function

# import numpy as np

# Creating a NumPy array
# numbers_np = np.array([1, 2, 3, 4, 5])

numbers = list(range(10))

print(numbers)

fruits = ["apple", "banana", "orange"]
print(fruits)

fruits_with_index = list(enumerate(fruits))
print(fruits_with_index)

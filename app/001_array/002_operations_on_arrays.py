# Accessing elements

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[0])

print(numbers[-1])

print(numbers[1:3])

print(numbers[0:2])

# Extracting every other 2nd element
every_other_element = numbers[::2]

print(every_other_element)

# Reversing the array
reversed_array = numbers[::-1]

print(reversed_array)

for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")

my_array = [10, 20, 30, 40, 50]
my_array[1] = 100

for element in my_array:
    print(element)

import random

var = []

print(type(var))  # Prints the type of var (should be 'list')

print(type("What is this"))  # Prints the type of the string ("str")

print(type(2))  # Prints the type of the integer (should be 'int')

print(type(3.14))  # Prints the type of the float (should be 'float')

var2 = [151, 251, 386, 493, 649]

print(var2)  # Prints the list var2

var2.append("009")  # Appends the string "009" to the list var2

print(var2)  # Prints the updated list var2

var2 = var2 + ["445"]  # Concatenates the list var2 with the list ["445"]

print(var2)  # Prints the updated list var2

print(dir(var2))  # Prints the list of attributes and methods of var2

print(dir("string"))  # Prints the list of attributes and methods of the string "string"

numbers = [0, 1, 2, 3, 4]

print(numbers)  # Prints the list numbers

for number in numbers:  # Iterates over the elements of the list numbers
    print(number * 2)  # Prints each number multiplied by 2

more_numbers = list(range(0, 25, 2))  # Creates a list of even numbers from 0 to 24

print(type(more_numbers))  # Prints the type of more_numbers (should be 'list')
print(more_numbers)  # Prints the list more_numbers

print(more_numbers[5])  # Prints the element at index 5 of more_numbers

more_numbers.reverse()  # Reverses the order of elements in more_numbers

print(more_numbers)  # Prints the reversed list more_numbers

print(more_numbers[5])  # Prints the element at index 5 of more_numbers

print(more_numbers[-1])  # Prints the last element of more_numbers

n = len(more_numbers)  # Assigns the length of more_numbers to the variable n

print(n)  # Prints the value of n

print(more_numbers[n - 1])  # Prints the last element of more_numbers using n

print(more_numbers.index(10))  # Prints the index of the first occurrence of 10 in more_numbers

try:
    print(more_numbers.index(100))  # Tries to print the index of 100 in more_numbers, but raises an exception
except:
    print("100 not in list")  # Prints an error message since 100 is not in more_numbers

var3 = [[random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
        [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
        [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
        [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
        [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]]

print(var3)  # Prints the list var3

for obj in var3:  # Iterates over the sublists in var3
    print(obj)
    for ele in obj:  # Iterates over the elements in each sublist
        print(ele)  # Prints each element
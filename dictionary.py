import json
import random

var = {}

print(type(var))  # Prints the type of var (should be 'dict')

var2 = {"juice": "cranberry", "movie": "The Lion King", "fruit": "mango"}

print(var2)  # Prints the dictionary var2

print(json.dumps(var2, indent=4))  # Pretty prints the dictionary var2

print(var2["juice"])  # Prints the value associated with the key "juice" in var2

var2["drank"] = "Jose"  # Adds a new key-value pair to var2

print(var2)  # Prints the updated dictionary var2

del var2["juice"]  # Removes the key "juice" and its associated value from var2

print(var2)  # Prints the updated dictionary var2

var2["drank"] = "Don"  # Updates the value associated with the key "drank" in var2

print(var2)  # Prints the updated dictionary var2

var2["drank"] = "Patron"  # Updates the value associated with the key "drank" in var2

print(dir(var2))  # Prints the list of attributes and methods of var2

print(list(var2.keys()))  # Prints the list of keys in var2

print(list(var2.values()))  # Prints the list of values in var2

for k, v in var2.items():  # Iterates over the key-value pairs in var2
    print(k, v)  # Prints each key and its corresponding value

print(len(var2))  # Prints the number of key-value pairs in var2

var3 = {
    1: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    2: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    3: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
}

print(json.dumps(var3, indent=4))  # Pretty prints the dictionary var3

for key, value in var3.items():  # Iterates over the key-value pairs in var3
    print(key, value)
    for obj in value:  # Iterates over the elements in each sublist
        print(obj)  # Prints each element
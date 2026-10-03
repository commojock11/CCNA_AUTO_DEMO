#modules
import sys 

##Vars
my_variable = 42
print(sys.getsizeof(my_variable))
##Integers
whole_num = 10
print(sys.getsizeof(whole_num))
float_num = 3.14
print(sys.getsizeof(float_num)) 
####sys.getsizeof() returns the size of an object in bytes

##strings
a_string = "Hello, world!"
#f strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.
print(f"String: {a_string}, Size: {sys.getsizeof(a_string)} bytes")
##Booleans data type 
very_true = True
very_false = False
## == comparison operator checks if two values are equal and returns a boolean value (True or False) based on the comparison.
print(very_true == very_false)
## None data type
my_none = None
# Sequences
## Lists are ordered collections of items that can be of different data types. Lists are defined using square brackets [] and can be modified (mutable).
my_list = [1, 2, 3, 4, 5]
## tuples are ordered collections of items, similar to lists, but they are immutable (cannot be changed after creation). Tuples are defined using parentheses ().
my_tuple = (1, 2, 3)
## sets are unordered collections of unique items. Sets are defined using curly braces {} or the set() constructor. They do not allow duplicate elements.
my_set = {1, 2, 3}
# indexing and slicing
## Indexing allows you to access individual elements of a sequence (like a list, tuple,
print(my_list[0])  # Accessing the first element of the list
print(my_tuple[1])  # Accessing the second element of the tuple
# changing elements in a list
my_list[1] = 7
print(my_list) 
print(a_string[7:12])  # Slicing the string to get "world"

## dictionaries are unordered collections of key-value pairs. Each key is unique, and it maps to a specific value. Dictionaries are defined using curly braces {} and colons : to separate keys from values.
my_dict1 = { "key1": "value1", 
    "key2": "value2",
    "key3": [None]
}
my_dict2 = {"key22": "value22", "key33": "value26", "key44": [my_dict1]}



my_indexed_dict = [my_dict1, my_dict2]

print(my_indexed_dict[1]["key44"][0]["key1"])

top_speed = [150, 200, 300]


first_car = [{
    "model": "Porsche 911",
    "year": 2023,
    "within_price_range": False,
    "offroad": None,
    "speed": [top_speed[2]]
}]

second_car = [{
    "model": "Ford F-150",
    "year": 2026,
    "within_price_range": True,
    "offroad": True,
    "speed": [top_speed[0]],
    "comparison": [first_car]
}]

indexed_cars = [first_car, second_car]
print(indexed_cars[1][0]["comparison"][0][0]["speed"])  # Accessing the speed of the first car through the comparison key of the second car
print(indexed_cars[1][0]["comparison"][0][0]["year"])  # Accessing the year of the first car through the comparison key of the second car
print(indexed_cars[1][0]["comparison"][0][0]["model"])  # Accessing the model of the first car through the comparison key of the second car

#modules
# import sys 

# ##Vars
# my_variable = 42
# print(sys.getsizeof(my_variable))
# ##Integers
# whole_num = 10
# print(sys.getsizeof(whole_num))
# float_num = 3.14
# print(sys.getsizeof(float_num)) 
# ####sys.getsizeof() returns the size of an object in bytes

# ##strings
# a_string = "Hello, world!"
# #f strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.
# print(f"String: {a_string}, Size: {sys.getsizeof(a_string)} bytes")
# ##Booleans data type 
# very_true = True
# very_false = False
# ## == comparison operator checks if two values are equal and returns a boolean value (True or False) based on the comparison.
# print(very_true == very_false)
# ## None data type
# my_none = None
# # Sequences
# ## Lists are ordered collections of items that can be of different data types. Lists are defined using square brackets [] and can be modified (mutable).
# my_list = [1, 2, 3, 4, 5]
# ## tuples are ordered collections of items, similar to lists, but they are immutable (cannot be changed after creation). Tuples are defined using parentheses ().
# my_tuple = (1, 2, 3)
# ## sets are unordered collections of unique items. Sets are defined using curly braces {} or the set() constructor. They do not allow duplicate elements.
# my_set = {1, 2, 3}
# # indexing and slicing
# ## Indexing allows you to access individual elements of a sequence (like a list, tuple,
# print(my_list[0])  # Accessing the first element of the list
# print(my_tuple[1])  # Accessing the second element of the tuple
# # changing elements in a list
# my_list[1] = 7
# print(my_list) 
# print(a_string[7:12])  # Slicing the string to get "world"

# ## dictionaries are unordered collections of key-value pairs. Each key is unique, and it maps to a specific value. Dictionaries are defined using curly braces {} and colons : to separate keys from values.
# my_dict1 = { "key1": "value1", 
#     "key2": "value2",
#     "key3": [None]
# }
# my_dict2 = {"key22": "value22", "key33": "value26", "key44": [my_dict1]}



# my_indexed_dict = [my_dict1, my_dict2]

# print(my_indexed_dict[1]["key44"][0]["key1"])

# top_speed = [120, 150, 200, 300]


# favorite_cars = [{
#     "model": "Porsche 911",
#     "year": 2023,
#     "within_price_range": False,
#     "offroad": None,
#     "speed": [top_speed[2]]
# },

# {
#     "model": "Ford F-150",
#     "year": 2026,
#     "within_price_range": True,
#     "offroad": True,
#     "speed": [top_speed[0]],
#     "comparison": []
# },
# {
#     "model": "Tesla Model S",
#     "year": 2024,
#     "within_price_range": True,
#     "offroad": False,
#     "speed": [top_speed[1]],
#     "comparison": []
# },
# {
#     "model": "Chevrolet Corvette",
#     "year": 2025,
#     "within_price_range": True,
#     "offroad": False,
#     "speed": [top_speed[3]],
#     "comparison": []
# }
# ]

#REDUNDANT CODE
# print(favorite_cars[0])
# print("next item")
# print(favorite_cars[1])

# favorite_cars[0] = None
# for car in favorite_cars:
#     try:
# #BEST WAY with For loop
    
#         if car["model"] == "Tesla Model S":
#             print("This is a Tesla Model S")
#             print(f"{car['year']} {car['model']}\n")
#             break
#         else:
#             print("Not a Tesla Model S")
#             continue
#     except TypeError as e:
#         print("An error occurred while iterating over favorite_cars")
#         print(f"Error is: {e}") 

#         car = {
#             "model": "Tesla Model S",
#             "year": 2024,
#             "within_price_range": True,
#             "offroad": False,
#             "speed": [top_speed[1]],
#             "comparison": []
#         }

#         if car["model"] == "Tesla Model S":
#             print("This is a Tesla Model S")
#             print(f"{car['year']} {car['model']}\n")
#         else:
#             print("Not a Tesla Model S")
#             continue
#     else:
#         print("No encounter detected")
#     finally:
#         print("Finished processing the current car")
        
# if any(car["model"] == "Porsche 911" for car in favorite_cars):
#     print("There is a Porsche 911 in the list")
# else:
#     print("There is no Porsche 911 in the list")

## if else

# n = 200
# if n > 100:
#     print("n is greater than 100")
# elif n == 100:
#     print("n is equal to 100")
# else:
#     print("n is not equal to 100")
#     print("n is not greater than 100")


# code = 200 
# match code:
#     case 404:
#         print("Not Found")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 301:
#         print("Moved Permanently")
#     case 200:
#         print("Success")
#     case _:
#         print("Unknown code")



# favorite_cars = [
#     {
#         "make": "Tesla",
#         "model": "Model S",
#         "year": 2022,
#         "price": 79999.99,
#         "features": ["Autopilot", "Electric", "All-Wheel Drive"],
#         "is_electric": True,
#         "owner": None
#     },
#     {
#         "make": "Porsche",
#         "model": "911 Carrera",
#         "year": 2023,
#         "price": 106500.00,
#         "features": ["Sport Mode", "Rear-Wheel Drive", "Turbocharged"],
#         "is_electric": False,
#         "owner": None
#     },
#     {
#         "make": "Ford",
#         "model": "Mustang",
#         "year": 2022,
#         "price": 27995.00,
#         "features": ["Rear-Wheel Drive", "V8 Engine", "Fastback"],
#         "is_electric": False,
#         "owner": None
#     },
#     {
#         "make": "Chevrolet",
#         "model": "Corvette",
#         "year": 2023,
#         "price": 62995.00,
#         "features": ["Supercharged", "V8 Engine", "Fastback"],
#         "is_electric": False,
#         "owner": None
#     },
#     {
#         "make": "Audi",
#         "model": "R8",
#         "year": 2023,
#         "price": 144195.00,
#         "features": ["All-Wheel Drive", "V10 Engine", "Convertible"],
#         "is_electric": False,
#         "owner": None
#     }
# ]

# #for loop to check car prices
# for car in favorite_cars:
#     try:
#         if car["price"] > 100000:
#             print(f"{car['make']} {car['model']} is over $100,000")
#     except KeyError as e:
#         print(f"Missing key in car dictionary: {e}")
#     except TypeError as e:
#         print(f"Type error in car dictionary: {e}")

from Funcs.my_module import cubed_number, greet_person

print(cubed_number(3))
print(greet_person("Alice"))

"""
Question 4
Use the next() function to find the first element in a list of dictionaries whose attribute
‘x’ = 5. Default to an empty dictionary if not found.
"""

list_of_dicts = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 5, "y": 6, "z": 7},
    {"x": 4, "y": 5, "z": 6},
    {"x": 7, "y": 8, "z": 9},
    {"x": 10, "y": 11, "z": 12},
]

first_element = next((d for d in list_of_dicts if d["x"] == 5), {})
print(first_element)

empty_dict = next((d for d in list_of_dicts if d["x"] == 999), {})
print(empty_dict)

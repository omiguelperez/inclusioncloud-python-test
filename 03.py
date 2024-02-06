"""
Question 3
Use list comprehension and a lambda function to extract all of the even integers out of
a list of integers
"""

list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_integers = list(filter(lambda x: x % 2 == 0, list_of_integers))
print(even_integers)

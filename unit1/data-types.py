"""
Project:     Data Types Notes
Author:      Mr. Buckley
Last update: 8/25/2018
Description: Goes over comments, int, float, str, and type casting  
"""

# *** COMMENTS ***
# This is a comment (with a "#")
# Comments are only for the user's eyes, the program doesn't read them.
# Describe what sections of code do with a comment.
"""
This is a
multiline comment
"""

# *** DATA TYPE: INTEGER ***
# TODO: An integer number (no decimal)
integer = 5
print(integer)
print(type(integer))

# *** DATA TYPE: FLOAT ***
# TODO: A decimal number
decimal = 6.794
print(decimal)
print(type(decimal))

# *** DATA TYPE: STRING ***
# TODO: A string of characters enclosed in quotes
text = "running"
print(text)
print(type(text))


# *** TYPE CASTING ***
# This converts one type to another

# TODO: Cast float to int
float_num = 5.259
int_num = int(float_num)
print(int_num)
print(type(int_num))

# TODO: Cast int to string
number = "78"
print("5 " + str(number))

# TODO: Cast number string to int
number = "5" 
print(int(number) + 2) 

# TODO: Input demo (str to float)
print("give me a decimal and ill add 1 to it")
number = float(input())
print(number + 1)

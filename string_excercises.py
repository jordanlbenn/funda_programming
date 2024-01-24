# Question 1: Take an input string from the user and create a new string with the first, middle, and last characters of the input string

# 1. Ask the  user to input a string
# 2. Get the first character using index 0
# 3. Get the last character using index -1
# 4. Get the middle character
# a. Get the number of characters the string has using len()
# b. Get the index of the middle character len/2
# c. Get the character at middle index using str(mid_index)

test_str = 'score'
# print(int(len(test_str)/2)) # this gives the middle character index
mid_index = int(len(test_str)/2)
print(test_str[mid_index])

user_string = input('Please enter a string: ')
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

# To get the middle character, find length and index of middle character
str_length = len(user_string)
mid_index = int(str_length/2) # Since indices can only be integers

mid_char = user_string[mid_index] # To access the char at mid index
result_str = first_char + mid_char + last_char
print(result_str)
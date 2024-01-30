# Jordan Bennett
# Fundementals of Programming
# Week 3 Strings Homework

# Excerise 1 - Take user input for first name, last name, age, ssn, height #
# and weight and store them in corressponding varibles. #

input_str_start1 = input('Welcome to Exercise #1, click the "Enter" key to get started!')
input_str_firstname = input('Please enter your first name:')
input_str_lastname = input('Please enter your last name:')
input_int_age = input('Please enter your age:')
input_int_ssn = input('Please enter your SSN (with dashes):')
input_float_height = input('Please enter your height in centimeters:')
input_float_weight = input('Please enter your weight in pounds:')


name = input_str_firstname + input_str_lastname
age = input_int_age
ssn = input_int_ssn
height = float(input_float_height)
heighttoinch = (height * 0.3937)
weight = float(input_float_weight)
weighttokg = (weight / 2.2046)

print(f'Hello,{name}! Thank you for applying. Please find your details below:')
print(f'Age: {age}')
print(f'SSN: {ssn}')
print(f'Height: {heighttoinch} inches')
print(f'Weight: {weighttokg} kgs')


# Excercise 2 Considering the quote below;
input_str_start2 = input('Welcome to Exercise #2, click the "Enter" key to get started!')

org_str = 'You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose - Dr. Seuss'
input_str_stp1 = input(f'In this exercise we can consider this string: \n {org_str}')

str1 = 'You have brains in your head. You have feet in your shoes.You can steer yourself any direction you choose -Dr. Seuss'
new_string1 = str1.replace('You can steer yourself any direction you choose','')
input(f'This result will show the original string without the phrase indicated in the exercise: \n {new_string1}')

input(f'Checking if the phrase contains the word "feet":')
import re
if re.search('feet', str1):
    print('The phrase contains the word feet.')

else:
    print('The phrase does not contain the word feet.')

input(f'Replacing the ending of the phrase will prompt this result:')
str2 = 'You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose -Dr. Seuss'
new_string2 = str2.replace('-Dr. Seuss', "-Dr. Seuss, Oh, the Places You'll Go!")
print(new_string2)


input("Homework is completed! Thank you for trying :) ")





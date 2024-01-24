'''
print("Hello World!")
# for variable names do not user reserved keywords
print(help('keywords'))

# Assign multiple variables with the same value simultaneously
a = b = c = 10  # works but not recommended
print(a, b, c)

# Expression vs Statement
x = 47  # statement - we are just declaring something
y = 247 + 10  # expression - referring to something with an action

# Type Conversion

# Convert to int
print(int(10.24))
print(int(float('10.24')))

# Convert to str
print(str(20))
print(type(str(20)))

## Strings ##
# Can be created either by using single, double, or triple quotes #
first_name = 'Jane'
print(first_name)

last_name = "Doe"
print(last_name)

address = ''10 Main St''
print(address)

job1 = "Physician's Assistant"
print(job1)
'''
'''
## String Functions ##
emp_name = "Jane Doe"
# len() --> returns the numbers of characters in a given string
print(len(emp_name))

# upper and lower --> these convert the string into corresponding cases
print(emp_name.upper())
# these prints everything in upper or lower case letters

# String Concatention
first_name = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name)

age = 24
print(first_name + ' ' + last_name + ':' + str(age))

# String Multiplication
print('Hello' * 3)
# Can only add two strings and only multiply a string with an int 
'''

# Accessing string characters
emp_name: str = "Jane Doe"
print(emp_name[3])
# print(emp_name[8]) # throws index out of bounds error because the last char is at idx 7

print(emp_name.index('n'))




# format method example

name = "Navneet"
age = 24

print('{0} is {1} year old'.format(name, age))

# return same output as previous

print('{} is {} year old'.format(name, age))

# decimal (.) precision of 3 for float '0.333'
print('{0:.4f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^10}'.format('hello'))

# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# comma(,) is used to print the output in same line
print("a"),
print("b"),

# use '\' before ' so that python can understand
print('What\'s your name?')
print('This is the first line\nThis is the second line')
print('This is the first line\tThis is the second line')

# \n characte in the end of line
print('This is the first line\tThis is the second line\n')
print('This is the first line\tThis is the second line')
print(r'This is the first line\tThis is the second line')

x = 50
def func():
 global x
 print('x is', x)
 x = 2
 print('Changed global x to', x)
func()
print('Value of x is', x)


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)


def total(initial=5, *numbers, **keywords):
    count = initial
    print("count "+str(count))
    for number in numbers:
        count += number
        print('number' + str(number))
    for key in keywords:
        count += keywords[key]
        print("Keyword :" + str(key))
    return count
print(total(10, 1, 2, 15, 3, a=43, vegetables=50, fruits=100))


def some_function():
    pass

print("some function" + str(some_function()))

def print_max(e, f):
 '''Prints the maximum of two numbers.
 The two values must be integers.'''
 # convert to integers, if possible
 e = int(e)
 f = int(f)
 if e > f:
     print(e, 'is maximum')
 else:
     print(f, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)
print(total.__doc__)

value1 = int(input("Enter the first value"))
value2 = int(input("Enter the second value"))


def function_max(a, b):
    if a > b:
        print('{0} is greater'.format(a))
    elif a == b:
        print('{0} is equal to {1}'.format(a, b))
    else:
        print('{0} is greate'.format(b))

function_max(value1, value2)
function_max(9, 20)

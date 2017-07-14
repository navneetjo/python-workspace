import sys
import os

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

print(os.getcwdb())

print(dir(sys))
print(vars())
print(dir())

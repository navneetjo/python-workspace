# slicing and sequence example
shopList = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shopList[0])
print('Item 1 is', shopList[1])
print('Item 2 is', shopList[2])
print('Item 3 is', shopList[3])
print('Item -1 is', shopList[-1])
print('Item -2 is', shopList[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shopList[1:3])
print('Item 2 to end is', shopList[2:])
print('Item 1 to -1 is', shopList[1:-1])
print('Item start to end is', shopList[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# This is my shopping list
shopList = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shopList), 'items to purchase.')
print('These items are:',)

# fetching each Item from the list
for item in shopList:
    print(item)
print('\nI also have to buy rice.')

# appending rice to the list
shopList.append('rice')
print('My shopping list is now', shopList)
print('I will sort my list now')

# sorting the list
shopList.sort()
print('Sorted shopping list is', shopList)
print('The first item I will buy is', shopList[0])

# first Item in the list
oldItem = shopList[0]

# delete first Item from the list
del shopList[0]
print('I already bought the', oldItem)
print('My shopping list is now', shopList)

# insert any Item in specific location 
shopList.insert(0, 'new item')
print('My shopping list is now', shopList)
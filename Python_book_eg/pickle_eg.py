import pickle

# name of the file where we want to store data
#shopListFile = 'shopList.data'

# shopping lists
shopList = ['apple','banana','orange','mango']

# write to file
f = open('shopListFile','wb')

# dump the object to file
pickle.dump(shopList, f)
f.close()

# delete shopList
del shopList

# read the content of shopListFile
f = open('shopListFile','rb')

# load the object from file
storeData = pickle.load(f)
print(storeData)


# file example for write operation
text = "Adding a new line \n new content \n to check first program for file"

# open a file for "w" mode for write operation
f = open('a.txt', 'w')
print(f)
# write into the file
f.write(text)

# close the file
f.close()

# if no mode is defined by default read 'r' mode is there
f = open('a.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)

f.close()

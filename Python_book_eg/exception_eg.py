try:
    text = input("Enter a Name :")
except EOFError:
    print("EOF file error")
except KeyboardInterrupt:
    print("cancel the operation")
else:
    print('Name is ' + text)
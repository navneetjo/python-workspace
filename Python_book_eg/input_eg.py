def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)

name = input("Enter a name")
if is_palindrome(name):
    print("Palindrome")
else:
    print("Not Palindrome")



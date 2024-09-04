str =  "racelcar"
str = str.casefold()
revstr = reversed(str)
if list(str) == list(revstr):
    print("string is a palindrome")
else:
    print("string is not a palindrome")

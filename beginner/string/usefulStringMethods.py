'''
The upper() and lower() string methods return a new string where all the
letters in the original string have been converted to uppercase or lower-
case, respectively.

Enter the following into the interactive shell:
'''

# Note that these methods do not change the string itself but return new string values.
# If you want to change the original string, you have to call upper() or lower() on the string and 
# then assign the new string to the variable where the original was stored.
# useful for case-insenstive

spam = 'Hello world!'
spam = spam.upper()
spam

spam = spam.lower()
spam

spam = spam.title()
spam

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
  print('I feel great too.')
else:
  print('I hope the rest of your day is good.')


'''
The isupper() and islower() methods will return a Boolean True value
if the string has at least one letter and all the letters are uppercase or lowercase, respectively.
'''
spam = 'Hello world!'
spam.islower()
spam.isupper()
'HELLO'.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.isupper()


'Hello'.upper()
'Hello'.upper().lower()
'Hello'.upper().lower().upper()
'HELLO'.lower()
'HELLO'.lower().islower()

# The isX String Methods
'''
These methods return a Boolean
value that describes the nature of the string.

isalpha() returns True if the string consists only of letters and is not blank.
isalnum() returns True if the string consists only of letters and numbers and is not blank.
isdecimal() returns True if the string consists only of numeric characters and is not blank.
isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
'''

'hello'.isalpha()
'hello123'.isalpha()
'hello123'.isalnum()
'hello'.isalnum()
'123'.isdecimal()
'    '.isspace()
'This Is Title Case'.istitle()
'This Is Title Case 123'.istitle()
'This Is not Title Case'.istitle()
'This Is NOT Title Case Either'.istitle()

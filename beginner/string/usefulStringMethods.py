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

'''
The startswith() and endswith() String Methods
The startswith() and endswith() methods return True if the string value they
are called on begins or ends (respectively) with the string passed to the
method; otherwise, they return False .
'''
'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')
'abc123'.startswith('abcdef')
'abc123'.endswith('12')
'Hello world!'.startswith('Hello world!')
'Hello world!'.endswith('Hello world!')

'''
The join() and split() String Methods
The join() method is useful when you have a list of strings that need to be joined together into a single string value. 
The join() method is called on a string, gets passed a list of strings, and returns a  >>> string <<<. The returned string
is the concatenation of each string in the passed-in list.

The split() method does the opposite: It’s called on a string value and returns a list of strings.
'''

', '.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])
'ABC'.join(['My', 'name', 'is', 'Simon'])

'My name is Simon'.split()
'MyABCnameABCisABCSimon'.split('ABC')
'My name is Simon'.split('m')

# A common use of split() is to split a multiline string along the newline characters.
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

spam.split('\n')

'''
Justifying Text with rjust(), ljust(), and center()

The rjust() and ljust() string methods return a padded version of the
string they are called on, with spaces inserted to justify the text.
The first argument to both methods is an integer length for the justified string.
An optional second argument to rjust() and ljust() will specify a fill character other than a space character.
The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right.
'''
'Hello'.rjust(10)
'Hello'.rjust(20)
'Hello World'.rjust(20)
'Hello'.ljust(10)
'Hello'.ljust(1)

'Hello'.rjust(20, '*')
'Hello'.ljust(20, '-')

'Hello'.center(20)
'Hello'.center(20, '=')

'''
Removing Whitespace with strip(), rstrip(), and lstrip()
Sometimes you may want to strip off whitespace characters (space, tab, and newline) from the left side, right side, or both sides of a string.

The strip() string method will return a new string without any whitespace characters at the beginning or end.
The lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively.
'''

spam = '    Hello World     '
spam.strip()
spam.lstrip()
spam.rstrip()

spam = 'SpamSpamBaconSpamEggsSpamSpam'
# The order of the characters in the string passed to strip() does not matter: strip('ampS') will
# do the same thing as strip('mapS') or strip('Spam') .
spam.strip('ampS') 

'''
Copying and Pasting Strings with the pyperclip Module
The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard. 
Sending the output of your program to the clipboard will make it easy to paste it to an email, word processor, or some other software.
This command has something wrong on my computer.
'''

import pyperclip
pyperclip.copy('Hello world!')

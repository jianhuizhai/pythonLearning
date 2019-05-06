"""
\'    Single quote
\"    Double quote
\t    Tab
\n    Newline (line break)
\\    Backslash
"""

spam = "That is Alice's cat."

spam = 'Say hi to Bob\'s mother.'

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings
# A raw string completely ignores all escape characters and prints any backslash that appears in the string.
print(r'That is Carol\'s cat.')

# Multiline Strings with Triple Quotes
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

# or
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# Multiline Comments

"""This is a test Python program.
This program was designed for Python 3, not Python 2.
"""

def spam():
"""This is a multiline comment to help
explain what the spam() function does."""

print('Hello!')

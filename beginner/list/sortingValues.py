spam = [2, 5, 3.14, 1, -7]
spam.sort()
print( spam )

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print( spam )

spam.sort(reverse=True)
print( spam )

# Third, sort() uses “ASCIIbetical order” rather than actual alphabetical
# order for sorting strings.
# This means uppercase letters come before lower-case letters.

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print( spam )

# If you need to sort the values in regular alphabetical order, pass str.
# lower for the key keyword argument in the sort() method call.
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print( spam )

# Second, you cannot sort lists that have both number values and string
# values in them, since Python doesn’t know how to compare these values.

spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
print( spam )
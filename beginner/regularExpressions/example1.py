'''
Review of Regular Expression Matching While there are several steps to using regular expressions in Python, 
each step is fairly simple.
1.  Import the regex module with import re .
2.  Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3.  Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4.  Call the Match object’s group() method to return a string of the actual matched text.
'''
linecommon = '============================================================'
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print( mo.group(1) )
print( mo.group(2) )
print( mo.group(0) )
print( mo.group() )
print( mo.groups() )
'''
Since mo.groups() returns a tuple of multiple values, you can use the
multiple-assignment trick to assign each value to a separate variable, as in
the previous areaCode, mainNumber = mo.groups() line.
'''
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print( mo.group(1) )
print( mo.group(2) )

"""
Matching Multiple Groups with the Pipe
"""
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print( mo1.group() )
mo2 = heroRegex.search('Tina Fey and Batman.')
print( mo2.group() )

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print( mo.group() )
print( mo.group(1) )

'''
Optional Matching with the Question Mark
'''
# The ? character flags the group that precedes it as an optional part of the pattern.
# If you need to match an actual question mark character, escape it with \? .
print(linecommon)
print('greedy and ungreedy')
print( linecommon )
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print( mo1.group() )

mo2 = batRegex.search('The Adventures of Batwoman')
print( mo2.group() )

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print( mo1.group() )

mo2 = phoneRegex.search('My number is 555-4242')
print( mo2.group() )

'''
Matching Zero or More with the Star
'''
# The * (called the star or asterisk) means “match zero or more”—the group
# that precedes the star can occur any number of times in the text.
print( linecommon )
print( 'Matching Zero or More with the Star' )
print( linecommon )
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print( mo1.group() )

mo2 = batRegex.search('The Adventures of Batwoman')
print( mo2.group() )

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print( mo3.group() )

# While * means “match zero or more,” the + (or plus) means “match one or more.”
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print( mo1.group() )

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print( mo2 )
print( mo2.group() )

mo3 = batRegex.search('The Adventures of Batman')
print( mo3 == None )

'''
Matching Specific Repetitions with Curly Brackets
'''
# If you have a group that you want to repeat a specific number of times,
# follow the group in your regex with a number in curly brackets.
# the regex (Ha){3} will match the string 'HaHaHa' , but it will not match 'HaHa' ,
# since the latter has only two repeats of the (Ha) group.
# Instead of one number, you can specify a range by writing a minimum,
# a comma, and a maximum in between the curly brackets. For example, the
# regex (Ha){3,5} will match 'HaHaHa' , 'HaHaHaHa' , and 'HaHaHaHaHa' .
# (Ha){3,} will match three or more instances of the (Ha) group, 
# while (Ha){,5} will match zero to five instances.
print( linecommon )
print( 'Matching Specific Repetitions with Curly Brackets' )
print( linecommon )
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print( mo1.group() )

mo2 = haRegex.search('Ha')
print( mo2 == None )
# Python’s regular expressions are greedy by default, which means that in
# ambiguous situations they will match the longest string possible.
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print( mo1.group() )

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print( mo2.group() )
'''
The findall() Method
'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print( mo.group() )

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # list assignment
print( mo, type(mo) )

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print( mo, type(mo) )
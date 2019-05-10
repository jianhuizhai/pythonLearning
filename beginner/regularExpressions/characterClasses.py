"""
Table 7-1: Shorthand Codes for Common Character Classes Shorthand character class Represents
------------------------------------------------------------------------------------------
    \d      Any numeric digit from 0 to 9.
    \D      Any character that is not a numeric digit from 0 to 9.
    \w      Any letter, numeric digit, or the underscore character.
            (Think of this as matching “word” characters.)
    \W      Any character that is not a letter, numeric digit, or the
            underscore character.
    \s      Any space, tab, or newline character. (Think of this as
            matching “space” characters.)
    \S      Any character that is not a space, tab, or newline.
------------------------------------------------------------------------------------------

Character classes are nice for shortening regular expressions.
"""
linecomment = '============================================================'
import re

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, \
                        8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge\
                        0 _')
print( mo )

'''
Making Your Own Character Classes
'''
# You can define your own character class using square brackets.
# the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase.
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print( mo )

# You can also include ranges of letters or numbers by using a hyphen.
# For example, the character class [a-zA-Z0-9] will match all lowercase letters,
# uppercase letters, and numbers.
# Note that inside the square brackets, the normal regular expression
# symbols are not interpreted as such. This means you do not need to escape
# the . , * , ? , or () characters with a preceding backslash.

# By placing a caret character ( ^ ) just after the character class’s opening
# bracket, you can make a negative character class. A negative character class
# will match all the characters that are not in the character class.
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print( mo )

'''
The Caret and Dollar Sign Characters
'''
# You can also use the caret symbol ( ^ ) at the start of a regex to indicate that
# a match must occur at the beginning of the searched text. Likewise, you can
# put a dollar sign ( $ ) at the end of the regex to indicate the string must end
# with this regex pattern. And you can use the ^ and $ together to indicate
# that the entire string must match the regex
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(     mo       )
print( mo.group() )
print( beginsWithHello.search('He said hello.') == None )

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print( mo )

print( wholeStringIsNum.search('12345xyz67890') == None )
print( wholeStringIsNum.search('12 34567890') == None )

'''
The Wildcard Character
'''
# The . (or dot) character in a regular expression is called a wildcard and will
# match any character except for a newline.
# Remember that the dot character will match just one character, which
# is why the match for the text flat in the previous example matched only lat .
# To match an actual dot, escape the dot with a backslash: \. .
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print( mo )

'''
Matching Everything with Dot-Star
'''
print( linecomment )
print( 'Matching Everything with Dot-Star' )
print( linecomment )
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print( mo.group(1) )
print( mo.group(2) )
print( mo.group() )
print( mo.groups() )

print( '''The dot-star uses greedy mode: It will always try to match as much text as
possible. To match any and all text in a nongreedy fashion, use the dot, star,
and question mark ( .*? ). Like with curly brackets, the question mark tells
Python to match in a nongreedy way.''')
print( linecomment )
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print( mo.group() )

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print( mo.group() )
print(linecomment)

print( '''Matching Newlines with the Dot Character''')
print( linecomment )
# The dot-star will match everything except a newline. By passing re.DOTALL as
# the second argument to re.compile() , you can make the dot character match
# all characters, including the newline character.
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group()
print( mo )

newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group()
print( mo )

print(linecomment)
print( '''Case-Insensitive Matching''')
# To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile() .
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print( mo )

mo = robocop.search('ROBOCOP protects the innocent.').group()
print( mo )
mo = robocop.search('Al, why does your programming book talk about robocop so much?').group()
print( mo )

print( linecomment )
print( '''Substituting Strings with the sub() Method''' )
print( linecomment )
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print( mo )

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.')
print( mo )

print(linecomment)
print( '''Managing Complex Regexes''')
print(linecomment)
# hard to read regular expression
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4} \
(\s*(ext|x|ext.)\s*\d{2,5})?)')
# you can spread the regular expression over multiple lines with comments
# like this:
phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?
                            (\s|-|\.)?
                            \d{3}
                            (\s|-|\.)
                            \d{4}
                            (\s*(ext|x|ext.)\s*\d{2,5})?
                            )''', re.VERBOSE)   
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
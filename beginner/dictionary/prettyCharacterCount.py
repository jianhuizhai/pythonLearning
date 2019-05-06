import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

'''
If you want to obtain the prettified text as a string value instead of dis-
playing it on the screen, call pprint.pformat() instead. These two lines are
equivalent to each other:

pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
'''

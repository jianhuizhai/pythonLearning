cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print( cat )
# or
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print( cat )

# The number of variables and the length of the list must be exactly
# equal, or Python will give you a ValueError :
cat = ['fat', 'black', 'loud']
size, color, disposition, name = cat
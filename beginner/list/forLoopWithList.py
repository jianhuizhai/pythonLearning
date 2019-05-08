for i in range(4):
    print(i)

spam = [0, 1,2,3,]
for i in spam:
    print(i )

# A common Python technique is to use range(len(someList)) with a for
# loop to iterate over the indexes of a list.

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
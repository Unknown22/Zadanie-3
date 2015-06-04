list1 = ['orange', 'apple', 'banana']
list2 = ('carrot', 'potato', 'lettuce')
list3 = {'milk', 'sugar', 'butter', 'flour'}
list4 = []
list4.extend(list1)
list4.extend(list2)
list4.extend(list3)

for x in list4:
    letter = x[0]
    for y in x[1:]:
        if letter == y:
            print x
        letter = y
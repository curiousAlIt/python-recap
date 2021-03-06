print('hi we are coding in python')

a = [1, 3, 14, 344]
# we have a variable: a, that is a list
# if we write "print ('a'), we get the character 'a'
print('a')
# but, if we write "print(a), we get the content of the variable a, in our case -  a list
print(a)

# now we will have a new variable,(in our case - a list): l
# this list contains strings - series of characters
l = ['eggs','milk', 'cucumbers']
print(l)
# so now, we know how to create different lists

# now, we will learn how to get the length of list
# we use the function len()
print('the length of the list a:')
print(len(a))

# now, we will learn how to add elements to lists
# we use the function append()
# in order to append the new element to a specific list, we use this:
#      (name of list).append(new element)
print('the list a before we add:')
print(a)
a.append(11235813)
a.append(-7)
a.append(22)
print('the list a after we add:')
print(a)

# in order to access to specific terms in a list:
# we use its index
# the first element always has the index 0
# example: if we want to access the second element, we use this:
#      (name of list)[1]
print('The first item in a:')
print(a[0])
print('The second item in a:')
print(a[1])
print('The last item in a:')
last_index = len(a)-1
print(a[last_index])

# now we will concatenate the lists a and l:
# we will use a new variable, like c, that equals to the list a followed by the list l
# we write this as:
#      c = a + l
# if we swap the order: d = l + a, we will get a new list with the items in a, after
# the items in l
c = a + l
d = l + a
print('l added to a: ')
print(c)
print('a added to l: ')
print(d)

"""
Array tpye
"""
# define array
names=["tim","jack","cindy"]

print(names)

# find array element
print(names[0].title())
print(names[-1].title())


# update element to array
names[0]="julian"
print(names)


# add element to array
names.append("append test")
print(names)

names.insert(0,"insert test")
print(names)


# delete element from array
del names[0]
print(names)

t = names.pop()
print(names)
print(t)

t2=names.pop(0)
print(names)
print(t2)


t3="cindy"
names.remove(t3)
print(names)


# sort element in array
names2=["tim","jack","cindy"]
print(names2)

# chi jiu pai xu
# names2.sort()
print(names2)

# temp sorted
print(sorted(names2))
print(sorted(names2,reverse=True))

# reverse array
names2.reverse()
print(names2)


# get lenth of array
print(len(names2))


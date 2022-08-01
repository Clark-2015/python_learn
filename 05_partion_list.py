ls=list(range(1,21,2))

print(ls)

print(ls[1:3])

print(ls[1:])
print(ls[:3])


print(ls[-3:])

for item in ls[4:6]:
    print(item)

# copy list
cpls=ls[:]

cpls.append(999)

print(ls)
print(cpls)




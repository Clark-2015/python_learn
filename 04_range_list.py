# range
r=range(1,11)
print(r)

r2=range(1,20,2)
print(r2)


# list 
ls= list(range(1,15,2))
print(ls)

ls2=[]
for item in ls:
    ls2.append(item**item)
print(ls2)

ls3=[item**2 for item in range(1,15,2)]
print(ls3)


# min max sum
print(min(ls3))
print(max(ls3))
print(sum(ls3))




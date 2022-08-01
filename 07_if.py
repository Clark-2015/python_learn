a=1

if a==1 :
    print("equal")
else :
    print("not equal")


mycar="vw"
cars=["benz","bmw","toyota","honda","vw"]

if mycar in cars:
    print("your car is in list")
else:
    print("your car is not in list")


for car in cars:
    if car =="bmw" or car=="vw":
        print(car.upper())
    else:
        print(car.title())



request_tops=["mashrum","banane","apple"]
# request_tops=[]
avalibe_tops=("mashrum","ounin","banane","pinia")

if request_tops:
    for t in request_tops:
        if t in avalibe_tops:
            print("add "+t+" to pizza")
        else:
            print("sorry, can not add "+t)
else:
    print("you want a plain pizza")

print("pizza is finished.")


# 1st 2nd 3rd 4th 5th ...
numls=list(range(1,10))

for num in numls:
    if num == 1:
        print(str(num)+"st")
    elif num==2:
        print(str(num)+"nd")
    elif num==3:
        print(str(num)+"rd")
    else:
        print(str(num)+"th")





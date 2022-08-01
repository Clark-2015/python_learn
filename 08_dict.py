alien_0 = {
        "color":"green",
        "points":10,
        "speed":"fast",
        }
print(alien_0)

alien_0["pos_x"]=10
alien_0["pos_y"]=15
print(alien_0)


alien_0["test"]="test"
print(alien_0)
del alien_0["test"]
print(alien_0)

increat_x=1
if alien_0["speed"]=="slow" :
    increat_x=1
elif alien_0["speed"]=="midum":
    increat_x=2
else:
    increat_x=3

alien_0["pos_x"] = alien_0["pos_x"] + increat_x

print(alien_0)


for k,v in alien_0.items():
    print("key:"+str(k)+", value:"+str(v)+".\n")

for k in alien_0.keys():
    print("key:"+str(k))

for v in alien_0.values():
    print("value:"+str(v))


favorite_lang={
        "jan":"c#",
        "clark":"javascript",
        "ben":"rust",
        "cindy":"javascript",
        }
print(set(favorite_lang.values()))


# json module is the tool to read and write struct data to  json file
import json

# import User class to save User entity
from user import User

json_file='test.json'

u1=User("si","li",age=13,sex="man")
u2=User("hong","xiao",age=12,sex="woman")

users=[u1.format_username(),u2.format_username()]

# write json to file
try:
    with open(json_file,"w") as json_obj:
        # write serierlized json data to json file
        json.dump(users,json_obj)
except OSError:
    print(OSError)
else:
    print("write file success.")



# read data from json file
try:
    with open(json_file) as json_obj:
        json_data = json.load(json_obj)
except OSError:
    print(OSError)
else:
    print("read JSON data:\n")
    print("\t"+str(json_data))


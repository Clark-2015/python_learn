# define a function

def say_hello(name,sex="man"):
    print("hello, "+name.title()+" "+sex)

# params receive as list
def get_userinfo(name,*profile,age=18):
    print("name: "+name)
    print("age: "+str(age))
    print("profile: "+str(profile))

# params receive as dict
def get_userinfo2(id,name,**profile):
    print("ID: "+str(id))
    print("name: "+name)
    print("profile2:"+str(profile))


# return results
def ret_result(**result):
    return result




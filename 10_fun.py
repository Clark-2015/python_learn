# define a function

def say_hello(name,sex="man"):
    print("hello, "+name.title()+" "+sex)

# call function say_hello
say_hello("xiaoli")
say_hello("xiaozhang","woman")
say_hello(sex="unkown",name="xiaozhao")

# params receive as list
def get_userinfo(name,*profile,age=18):
    print("name: "+name)
    print("age: "+str(age))
    print("profile: "+str(profile))

get_userinfo("userinfo","man",True)


# params receive as dict
def get_userinfo2(id,name,**profile):
    print("ID: "+str(id))
    print("name: "+name)
    print("profile2:"+str(profile))
get_userinfo2(10001,"zhangsan",age=18,sex="man",desc="I am very happy.")


# return results
def ret_result(**result):
    return result
print("result: "+str(ret_result(id=10001,name="zhangsan",age=18,sex="man",desc="I am very happy.")))




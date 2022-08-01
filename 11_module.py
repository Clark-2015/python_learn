# import all function from other module with modulename
'''
import m_sayhello
# call function say_hello
m_sayhello.say_hello("xiaoli")
'''

# import few functions from other module without modulename
#  use `as` to rename function name or module name
'''
from m_sayhello import get_userinfo as get_ui
get_ui("userinfo","man",True)
'''

# import all function from module without modulename
from m_sayhello import *
get_userinfo2(10001,"zhangsan",age=18,sex="man",desc="I am very happy.")

# say_hello("xiaozhang","woman")
# say_hello(sex="unkown",name="xiaozhao")

# get_userinfo("userinfo","man",True)

# get_userinfo2(10001,"zhangsan",age=18,sex="man",desc="I am very happy.")

# print("result: "+str(ret_result(id=10001,name="zhangsan",age=18,sex="man",desc="I am very happy.")))




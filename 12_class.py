# import user class
from user import User
# import Admin class extends User
from admin import Admin

# create a user entity with User Class
u1 = User("san","zhang",age=13,sex="man",id=10001)
u2 = User("si","li",age=14,sex="woman",id=10002)
u3 = User("wu","wang",age=12,sex="man",id=10003)

u1.say_greet()
u1.user_desc()

u2.say_greet()
u2.user_desc()

u3.say_greet()
u3.user_desc()

u1.increate_login_attempts()
u1.increate_login_attempts()
u1.increate_login_attempts()
u1.increate_login_attempts()
u1.increate_login_attempts()

u1.reset_login_attempts()


u1.increate_login_attempts()
u1.increate_login_attempts()
u1.increate_login_attempts()
u1.increate_login_attempts()

a1 = Admin("liu","zhao",id=1001,sex="man",age=28)

a1.say_greet()
a1.user_desc()

a1.show_privileges()

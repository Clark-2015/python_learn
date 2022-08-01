# define class user
class User():
    '''
    user class for system user
    '''
    def __init__(self,first_name,last_name,**user_profile):
        self.first_name=first_name
        self.last_name=last_name
        self.user_profile=user_profile
        self.login_attempts=0;

    def format_username(self):
        return (self.first_name+" "+self.last_name).title()

    def say_greet(self):
        print(self.format_username()+" say: Hello~.")

    def user_desc(self):
        print(self.format_username()+"'s infomation:")
        print("\tFirst Name: "+self.first_name.title())
        print("\tLast Name: "+self.last_name.title())
        for k,v in self.user_profile.items():
            print("\t"+str(k).title()+": "+str(v))

    def increate_login_attempts(self):
        if self.login_attempts>=3:
            print("login warning over 3 times("+str(self.login_attempts)+"), your account is locked.")
            return
        self.login_attempts+=1
        print("login warning: login attempts("+str(self.login_attempts)+")")

    def reset_login_attempts(self):
        self.login_attempts=0
        print("reset login attempts("+str(self.login_attempts)+")")


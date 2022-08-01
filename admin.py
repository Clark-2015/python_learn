# define admin class extends from User class
from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self,first_name,last_name,**user_profile):
        # unstruct user_profile param
        super().__init__(first_name,last_name,**user_profile)
        self.privileges=Privileges("read","write","execute")
    def show_privileges(self):
        print(self.format_username()+" have privileges: ")
        self.privileges.show_privileges()
    def user_desc(self):
        '''
        admin can not show desc
        '''
        print("\t(Admin can not show desc.)")

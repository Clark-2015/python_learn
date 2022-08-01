# define class privileges
class Privileges():
    def __init__(self,*privileges):
        self.privileges=privileges
    def show_privileges(self):
        for p in self.privileges:
            print("\tcan "+str(p))

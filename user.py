print(".....................9-3.....................")
class User():
    def __init__(self,first,last,age,place):
        self.first_name=first
        self.last_name=last
        self.age=age
        self.place=place
    def describe_user(self):
        print(self.first_name+ " " + self.last_name + " is " + str(self.age) + " years old.  : " + self.place.title() )
    def greet_user(self):
        print("Hello!   " + self.first_name + " " + self.last_name + ".")
if (__name__=="__main__"):
    jake=User("jak","li",18,"los angeles")
    jake.describe_user()
    jake.greet_user()
    tom=User("tim","robbin",20,"new york")
    tom.describe_user()
    tom.greet_user()

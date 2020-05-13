from restaurant import Restaurant
from user import User
# print(.....................9-6.....................)
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["sweet","salt","Spicy"]
    def view_ice(self):
        print(self.restaurant_name + ":" +self.cuisine_type+":  " ,end="")
        print(self.flavors)

my_ice=IceCreamStand("big","japan")
my_ice.view_ice()
# print("....................9-8.part...................")
class Privileges():
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print("Privileges:  ",end="")
        for priv in self.privileges:
            print(priv+",   ",end="")
# print(.....................9-7.....................)
class Admin(User):
    def __init__(self, first, last, age, place):
        super().__init__(first, last, age, place)
        self.priv=Privileges()
our_admin=Admin("tom","cruise",18,"USA")
our_admin.priv.show_privileges()
















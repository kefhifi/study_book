print("..........................9-1................................")
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("A " + self.cuisine_type + " 's " + self.restaurant_name)
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is opening")
restaurant = Restaurant("forever","China")
print(restaurant.restaurant_name + " " + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("..........................9-2................................")
restaurant_sec=Restaurant("happy","west")
restaurant_sec.describe_restaurant()
restaurant_third=Restaurant("big","italy")
restaurant_third.describe_restaurant()

print("..........................9-3................................")
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
    def change_name(self,name_1,name_2):
        self.first_name=name_1
        self.last_name=name_2
jake=User("jak","li",18,"los angeles")
jake.describe_user()
jake.greet_user()
tom=User("tim","robbin",20,"new york")
tom.describe_user()
tom.greet_user()
jake.first_name="wrek"
jake.greet_user()

jake.change_name("smith","hancks")
jake.greet_user()
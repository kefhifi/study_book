print("..........................9-1................................")
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("A " + self.cuisine_type + " 's " + self.restaurant_name)
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is opening")
if (__name__ == "__main__"):
    restaurant = Restaurant("forever","China")
    print(restaurant.restaurant_name + " " + restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

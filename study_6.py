# 9.1.1 创建Dog类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

# 根据约定，在Python中，首字母大写的名称指的是类。
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 1． 访问属性
# 要访问实例的属性，可使用句点表示法。
my_dog.name
# 句点表示法在Python中很常用，这种语法演示了Python如何获悉属性的值。在这里，Python先找到实例my_dog，再查找与这个实例相关联的属性name。
# 在Dog类中引用这个属性时，使用的是self.name。在❸处，我们使用同样的方法来获取属性age的值。

# 2． 调用方法
# 根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
# 要调用方法，可指定实例的名称（这里是my_dog）和要调用的方法，并用句点分隔它们。

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
jake=User("jak","li",18,"los angeles")
jake.describe_user()
jake.greet_user()
tom=User("tim","robbin",20,"new york")
tom.describe_user()
tom.greet_user()

# 9.2 使用类和实例

# 9.2.2 给属性指定默认值

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 9.2.3 修改属性的值
# 1． 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 2． 通过方法修改属性的值
class Car():
    ......
        def update_odometer(self, mileage):
            self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 3． 通过方法对属性的值进行递增
class Car():
    .......

    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("..........................9-4................................")




print("..........................9-5................................")

# 9.3 继承
# 9.3.1 子类的方法__init__()
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法__init__()需要父类施以援手。
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# 首先是Car类的代码。创建子类时，父类必须包含在当前文件中，且位于子类前面。
# 我们定义了子类ElectricCar。定义子类时，必须在括号内指定父类的名称。方法__init__()接受创建Car实例所需的信息。

# super()是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar的父类的方法__init__()，
# 让ElectricCar实例包含父类的所有属性。父类也称为超类（superclass），名称super因此而得名。

# 9.3.3 给子类定义属性和方法
# 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。

# 9.3.4 重写父类的方法
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
# 这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

# 9.3.5 将实例用作属性


# 9.3.6 模拟实物

print("..........................9-6................................")





print("..........................9-7................................")





print("..........................9-8................................")



print("..........................9-9................................")



# 9.4 导入类



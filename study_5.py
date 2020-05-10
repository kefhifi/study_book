# 8.2.2 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
# 关键字实参的顺序无关紧要，因为Python知道各个值该存储到哪个形参中。下面两个函数调用是等效的：
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
# 注意　使用关键字实参时，务必准确地指定函数定义中的形参名。

# 8.2.3 默认值
# 编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
# 这里修改了函数describe_pet()的定义，在其中给形参animal_type指定了默认值'dog'。这样，调用这个函数时，
# 如果没有给animal_type指定值，Python将把这个形参设置为'dog'：
# 请注意，在这个函数的定义中，修改了形参的排列顺序。由于给animal_type指定了默认值，无需通过实参来指定动物类型，
# 因此在函数调用中只包含一个实参——宠物的名字。然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，
# 这个实参将关联到函数定义中的第一个形参。这就是需要将pet_name放在形参列表开头的原因所在。
# 现在，使用这个函数的最简单的方式是，在函数调用中只提供小狗的名字：
describe_pet('willie')
# 注意　使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。
print("...........................8-3..............................")
def make_shirt(size,string):
    print("The Size: " + str(size) + " " + string)
make_shirt(42, "too big")
make_shirt(size=42,string="too big")
make_shirt(string="too big",size=42)

print("...........................8-5..............................")
def describe_city(city,country="china"):
    print(city + " is in " + country)
describe_city("beijing")
describe_city("shanghai")
describe_city("New York","USA")

# Python将非空字符串解读为True

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        #  字典追加 key-value
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)


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

# 8.4.1 在函数中修改列表


# 8.4.2 禁止函数修改列表
# 要将列表的副本传递给函数，可以像下面这样做：
function_name(list_name[:])
# 切片表示法[:]创建列表的副本。在print_models.py中，如果不想清空未打印的设计列表，可像下面这样调用print_models()：
print_models(unprinted_designs[:], completed_models)

print("...........................8-9.............................")
def show_magicians(names):
    for  name in names:
        print(name + " ",end="")
magicians = ["jake","brad","tom" ]
show_magicians(magicians)

print("...........................8-10.............................")
def show_magicians(names):
    for  name in names:
        print(name + "     ",end="")
magicians = ["jake","brad","tom" ]
show_magicians(magicians)
print("")
def make_great(names):
    i=0
    while i < len(names):
        names[i] = "the Great "+ names[i]
        i+=1
make_great(magicians)
show_magicians(magicians)
print("")
print(magicians)

print("...........................8-11.............................")
def show_magicians(names):
    for  name in names:
        print(name + "     ",end="")
magicians = ["jake","brad","tom" ]
show_magicians(magicians)
print("")
def make_great(names):
    i=0
    while i < len(names):
        names[i] = "the Great "+ names[i]
        i+=1
    return names
print("start print:")
show_magicians(make_great(magicians[:]))
print("")
show_magicians(magicians)

# 8.5 传递任意数量的实参
def make_pizza(*toppings):
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#  形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元祖中。函数体内的print语句通过生成输出来
# 证明Python能够处理使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用，
# 注意，Python将实参封装到一个元组中，即便函数只收到一个值也如此：


# 8.5.1 结合使用位置实参和任意数量实参
# 例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings的前面：
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 基于上述函数定义，Python将收到的第一个值存储在形参size中，并将其他的所有值都存储在元组toppings中。
# 在函数调用中，首先指定表示比萨尺寸的实参，然后根据需要指定任意数量的配料。

# 8.5.2 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# 函数build_profile()的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—值对。
# 形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中。
# 在这个函数中，可以像访问其他字典那样访问user_info中的名称—值对。
#######      函数内创建的字典，为什么函数外面可以引用？？？？？？？？？  这是局部变量啊！！！！！！

i=1
def test_var_range(i):
    i+=1
    print("in function: i=" + str(i))
test_var_range(1)
print("out function: i=" + str(i))


print("...........................8-12.............................")



print("...........................8-13.............................")


print("...........................8-14.............................")

# 8.6 将函数存储在模块中
# 要调用被导入的模块中的函数，可指定导入的模块的名称pizza和函数名make_pizza()，并用句点分隔它们。
# 这就是一种导入方法：只需编写一条import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。
# 如果你使用这种import语句导入了名为module_name.py的整个模块，就可使用下面的语法来使用其中任何一个函数：
 module_name.function_name()

# 8.6.2 导入特定的函数
# 你还可以导入模块中的特定函数，这种导入方法的语法如下：
from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
from module_name import function_0, function_1, function_2
# 对于前面的making_pizzas.py示例，如果只想导入要使用的函数，代码将类似于下面这样：
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数make_pizza()，因此调用它时只需指定其名称。

# 8.6.3 使用as给函数指定别名

# 下面给函数make_pizza()指定了别名mp()。这是在import语句中使用make_pizza as mp实现的，关键字as将函数重命名为你提供的别名：
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# 上面的import语句将函数make_pizza()重命名为mp()；在这个程序中，每当需要调用make_pizza()时，都可简写成mp()，
# 而Python将运行make_pizza()中的代码，这可避免与这个程序可能包含的函数make_pizza()混淆。
# 指定别名的通用语法如下：
from module_name import function_name as fn

# 8.6.4 使用as给模块指定别名

# 你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p），让你能够更轻松地调用模块中的函数。
# 相比于pizza.make_pizza()，p.make_pizza()更为简洁：
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 给模块指定别名的通用语法如下：
import module_name as mn

# 8.6.5 导入模块中的所有函数
# 使用星号（*）运算符可让Python导入模块中的所有函数：
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# import语句中的星号让Python将模块pizza中的每个函数都复制到这个程序文件中。由于导入了每个函数，
# 可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，
# 最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
# Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。

# 8.7 函数编写指南
# 编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。
# 给模块命名时也应遵循上述约定。

# 给形参指定默认值时，等号两边不要有空格：
def function_name(parameter_0, parameter_1='default value')
# 对于函数调用中的关键字实参，也应遵循这种约定：
 function_name(value_0, parameter_1='value')
# 如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，
# 从而将形参列表和只缩进一层的函数体区分开来。

print("...........................8-15.............................")



print("...........................8-16.............................")


print("...........................8-17.............................")




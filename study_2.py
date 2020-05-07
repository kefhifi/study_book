for value in range(1,5):
    print(value)
# 上面的循环只打印了 1 2 3 4
# 函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。
print("......................4.3.2.......................")
list_value=[]
for value in range(1,5):
    list_value.append(str(value))
print(list_value)
# 方法二
# 要创建数字列表，可使用函数list()将range()的结果直接转换为列表。如果将range()作为list()的参数，输出将为一个数字列表。
numbers = list(range(1,6))
print(numbers)
# 指定步长
numbers = list(range(1,6,3))
print(numbers)
# 处理列表的部分元素——Python称之为切片。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
# 输出：['charles', 'martina', 'michael']
# 输出也是一个列表，其中包含前三名队员：
print("..........................if语句..............................")
car = "Audi"
if car == 'Audi':
    print("==")
else:
    print("!=")
# 输出：==    所以 字符串用双引号或单引号都可以，没有区别
# 要判断特定的值是否已包含在列表中，可使用关键字in。来看你可能为比萨店编写的一些代码；这些代码首先创建一个列表，其中包含用户点的比萨配料，
# 然后检查特定的配料是否包含在该列表中。
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("in it")
else:
    print("not in")
if 'pepperoni' in requested_toppings:
    print("in it")
else:
    print("not in")
# 这种技术很有用，它让你能够在创建一个列表后，轻松地检查其中是否包含特定的值。
# 确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 在if语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True，并在列表为空时返回False。
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 输出：Are you sure you want a plain pizza?
print(".............................................")
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")








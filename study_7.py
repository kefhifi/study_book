# 10. 文件和异常
# 10.1 文件操作
with open('pi_digits.txt',encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents)
# 在这个程序中，第1行代码做了大量的工作。我们先来看看函数open()。要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开文件，这样才能访问它。
# 函数open()接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。在这个示例中，当前运行的是file_reader.py，
# 因此Python在file_reader.py所在的目录中查找pi_digits.txt。函数open()返回一个表示文件的对象。
# 在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象；Python将这个对象存储在我们将在后面使用的变量中。
# 关键字with在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了open()，但没有调用close()；
# 你也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。
# 这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调用close()，你会发现需要使用文件时它已关闭（无法访问），
# 这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让Python去确定：你只管打开文件，
# 并在不需要使用它时，Python自会在合适的时候自动将其关闭。

# 10.1.3 逐行读取
filename = 'pi_digits.txt'
with open(filename,encoding='utf-8') as file_object:
    for line in file_object:
        print(line,end="")

# 10.1.4 创建一个包含文件各行内容的列表
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外访问文件的内容，
# 可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# 方法readlines()从文件中读取每一行，并将其存储在一个列表中；接下来，该列表被存储到变量lines中；在with代码块外，
# 我们依然可以使用这个变量。在❷处，我们使用一个简单的for循环来打印lines中的各行。
# 由于列表lines的每个元素都对应于文件中的一行，因此输出与文件内容完全一致。

# 10.1.5 使用文件的内容


# 10.1.6 包含一百万位的大型文件
# 索引访问字符串
a="abcd1234"
print(a[0:2]+"...")
print(a[1])

# 判断字符串是否在另外一个字符串里面
string="abcdefghijklmnopq"
test_str="efg"
if test_str in string:
    print("in")
else:
    print("no in")

print(".....................10-1.........................")
file_name="learning_python.txt"
with open(file_name,mode='r',encoding='utf-8-sig') as file_obj:
    # 全部读取
    contents=file_obj.read()
    print("1st:")
    print(contents)
with open(file_name, mode='r', encoding='utf-8-sig') as file_obj:
    print("2nd:")
    # 遍历     要以每次一行的方式检查文件，可对文件对象使用for循环
    for li in file_obj:
        print(li.rstrip())
with open(file_name, mode='r', encoding='utf-8-sig') as file_obj:
    print("3rd:")
    lines=file_obj.readlines()
for lin in lines:
    print(lin,end="")

print(".....................10-2.........................")
file_name="learning_python.txt"
with open(file_name,mode='r',encoding='utf-8-sig') as file_obj:
    # 全部读取
    contents=file_obj.read()
new_contents=contents.replace("Python","C")
print(new_contents)

# 10.2.1 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。
# 如果你省略了模式实参，Python将以默认的只读模式打开文件。
# 如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入（'w'）模式打开文件时千万要小心，
# 因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
# 注意　Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

print(".....................10-3.........................")


print(".....................10-4.........................")


print(".....................10-5.........................")

# 10.3 异常
# 异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
# 使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback。

# 10.3.4 else 代码块
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)
# try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。
# 有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。except代码块告诉Python，
# 如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。

# 10.3.5 处理FileNotFoundError异常

# 10.3.6 分析文本

# 10.3.7 使用多个文件

# 10.3.8 失败时一声不吭
# 要让程序在失败时一声不吭，可像通常那样编写try代码块，但在except代码块中明确地告诉Python什么都不要做。
# Python有一个pass语句，可在代码块中使用它来让Python什么都不要做。
# pass语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。例如，在这个程序中，
# 我们可能决定将找不到的文件的名称写入到文件missing_files.txt中。用户看不到这个文件，但我们可以读取这个文件，进而处理所有文件找不到的问题。

# 10.3.9 决定报告哪些错误


print(".....................10-6.........................")


print(".....................10-7.........................")


print(".....................10-8.........................")


print(".....................10-9.........................")


print(".....................10-10.........................")


# 10.4 存储数据

# 10.4.1 使用json.dump()和json.load()

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# 我们先导入模块json，再创建一个数字列表。在❶处，我们指定了要将该数字列表存储到其中的文件的名称。
# 通常使用文件扩展名.json来指出文件存储的数据为JSON格式。接下来，我们以写入模式打开这个文件，让json能够将数据写入其中。
# 在处，我们使用函数json.dump()将数字列表存储到文件numbers.json中。

import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
# ，我们使用函数json.load()加载存储在numbers.json中的信息，并将其存储到变量numbers中

# 10.4.2 保存和读取用户生成的数据
import json
namefile="username.json"
try:
    with open(namefile,"r",encoding="utf-8-sig") as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    with open(namefile,"w",encoding="utf-8-sig") as file_obj:
        username=input("what is your name? ")
        json.dump(username,file_obj)
    with open(namefile,"r",encoding="utf-8-sig") as file_obj:
        username = json.load(file_obj)
        print("hello!", end="")
        print(username)
else:
    print("hello!",end="")
    print(username)

# 10.4.3 重构


print(".....................10-11.........................")


print(".....................10-12.........................")


print(".....................10-13.........................")


print(".....................10-14.........................")


# 11.1 测试函数

# 11.1.1 单元测试和测试用例

# 我们使用了unittest类最有用的功能之一：一个断言方法。断言方法用来核实得到的结果是否与期望的结果一致。



#我们将这个方法命名为test_first_last_middle_name()。方法名必须以test_打头，这样它才会在我们运行test_name_function.py时自动运行。
# 这个方法名清楚地指出了它测试的是get_formatted_name()的哪个行为，这样，如果该测试未通过，我们就会马上知道受影响的是哪种类型的姓名。
# 在TestCase类中使用很长的方法名是可以的；这些方法的名称必须是描述性的，这才能让你明白测试未通过时的输出；
# 这些方法由Python自动调用，你根本不用编写调用它们的代码。



print(".....................11-1.........................")
city_function.py
def city_country(city,country):
    return (city + " " + country).title()

test_cities.py
import unittest
from city_function import city_country
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago","chile"),"Santiago Chile")



print(".....................11-2.........................")
city_function.py
def city_country(city,country,population=""):
    if population:
        return (city + " " + country).title()+ " - " + "population " + population
    else:
        return (city + " " + country).title()

def city_country_1(city,country,population=0):
    if population:
        return (city + " " + country).title()+ " - " + "population " + str(population)
    else:
        return (city + " " + country).title()

test_cities.py
import unittest
from city_function import city_country,city_country_1
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago","chile"),"Santiago Chile")
    def test_city_country_1(self):
        self.assertEqual(city_country_1("santiago","chile"),"Santiago Chile")
    def test_city_country_population(self):
        self.assertEqual(city_country("santiago", "chile", "5000000"), "Santiago Chile - population 5000000")
    def test_city_country_population_1(self):
        self.assertEqual(city_country_1("santiago", "chile", 5000000), "Santiago Chile - population 5000000")

# 11.2 测试类
# 11.2.1 各种断言方法
# 表11-1描述了6个常用的断言方法。使用这些方法可核实返回的值等于或不等于预期的值、返回的值为True或False、返回的值在列表中或不在列表中。
# 你只能在继承unittest.TestCase的类中使用这些方法。

# 11.2.2 一个要测试的类
# 方法	                  用途
# assertEqual(a,b)	    核实a == b
# assertNotEqual(a,b)	    核实a != b
# assertTrue(x)	        核实x为True
# assertFalse(x)	        核实x为False
# assertIn(item,list)	    核实item在list中
# assertNotIn(item,list)	核实item不在list中


# 11.2.4 方法setUp()
# 在前面的test_survey.py中，我们在每个测试方法中都创建了一个AnonymousSurvey实例，并在每个方法中都创建了答案。
# unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们。
# 如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
# 这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。

# 测试自己编写的类时，方法setUp()让测试方法编写起来更容易：可在setUp()方法中创建一系列实例并设置它们的属性，
# 再在测试方法中直接使用这些实例。相比于在每个测试方法中都创建实例并设置其属性，这要容易得多。

# 注意　运行测试用例时，每完成一个单元测试，Python都打印一个字符：测试通过时打印一个句点；
# 测试引发错误时打印一个E；测试导致断言失败时打印一个F。这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。
# 如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果来获悉有多少个测试通过了。

print(".....................11-3.........................")
class Employee():
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
    def give_raise(self,incre=5000):
        self.salary=self.salary+incre

import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_emp=Employee("jak","lee",100000)
        self.fi="jak"
        self.la="lee"
        self.sa=105000
        self.sal=110000

    def test_give_default_raise(self):
        self.my_emp.give_raise()
        self.assertEqual(self.my_emp.salary,self.sa)

    def test_give_custom_raise(self):
        self.my_emp.give_raise(10000)
        self.assertEqual(self.my_emp.salary,self.sal)















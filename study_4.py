# input函数 和 while 循环
age = input("How old are you? ")
print(age)

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nNo........")

# 7.1.3 求模运算符
# 将两个数相除并返回余数
print(4%3)
print(12%3)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# Python首次执行while语句时，需要将message的值与'quit'进行比较，但此时用户还没有输入。如果没有可供比较的东西，Python将无法继续运行程序。
# 为解决这个问题，我们必须给变量message指定一个初始值。虽然这个初始值只是一个空字符串，但符合要求，让Python能够执行while循环所需的比较。
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

active = True
while active:
    print("8")


# 7.2.4 使用break退出循环
# 注意　在任何Python循环中都可使用break语句。例如，可使用break语句来退出遍历列表或字典的for循环。

# 7.2.5 在循环中使用continue

# 7.3.1 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())



# 7.3.2 删除包含特定值的所有列表元素
# 法一：
numbers=[1,2,3,5,8,2,5,8,2,3,2,99]
print(numbers)
while True:
    if 2 in numbers:
# remove 每次只删除第一个匹配值
        numbers.remove(2)
    else:
        break
print(numbers)
# 法二：
numbers=[1,2,3,5,8,2,5,8,2,3,2,99]
print(numbers)
while 2 in numbers:
    numbers.remove(2)
print(numbers)

# 7.3.3 使用用户输入来填充字典

























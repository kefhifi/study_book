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






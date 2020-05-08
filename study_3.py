print("............................字典...........................")
# 打印列表
cars=["audi","bmw","ford"]
print(cars)
# ['audi', 'bmw', 'ford']

# 打印字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
alien_0['color']='red'
print(alien_0)
# {'color': 'red', 'points': 5, 'x_position': 0, 'y_position': 25}
alien_0={}
print(alien_0)
# {}
alien_0['color']='red'
alien_0['num']=3
print(alien_0)
# {'color': 'red', 'num': 3}

favorite_languages = {
    'jen':'python',
    'jake':'c',
    'luke':'c++',
    }
print(favorite_languages)

# print语句分成多行
print("this "+
      "is "+
      "a pear")
# this is a pear
print("............................6-1...........................")
person={"first_name":"brad","last_name":"pitt","age":33,"city":"Los Angeles"}
print(person)
print("............................遍历字典...........................")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
# 或者 for k, v in user_0．items()
    print("\nKey: " + key)
    print("Value: " + value)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())
# 如果将上述代码中的for name in favorite_languages.keys():替换为for name in favorite_languages:，输出将不变
for name in favorite_languages:
    print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
# 通过对包含重复元素的列表调用set()，可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合
for language in set(favorite_languages.values()):
    print(language.title())


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
for name,info in users.items():
    print(name.title()+ "'s INFO:")
    for key,value in info.items():
        print(key+" is "+value)

# 这章的习题一定要做，多练习，否者过几天又忘记了。
print("...............................6-7................................")










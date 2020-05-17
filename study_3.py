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

print("..........................6-3.......................")
dic_table={"for":"loop_1","while":"loop_2","in":"loop_in ","with":"open file use","as":"to be"}
for key,value in dic_table.items():
    print(key + ": " + value)

for key,value in dic_table.items():
    print(key+"\n")
    print("\t" + value)

print("..........................6-4.......................")
dic_table={"for":"loop_1","while":"loop_2","in":"loop_in ","with":"open file use","as":"to be"}
dic_table["if"]="assume"
dic_table["else"]="another aspect"
dic_table["class"]="define class"
dic_table["def"]="define"
dic_table["and"]="2 condition"
for key,value in dic_table.items():
    print(key + ": " + value)




# 这章的习题一定要做，多练习，否者过几天又忘记了。
print("...............................6-8................................")

cats = {'location': 'beijing', 'master': 'kate'}
dogs = {'location': 'shanghai', 'master': 'tom'}
fish = {'location': 'shenzhen', 'master': 'lily'}
pets = [cats, dogs, fish]
for pet in pets:
    for key, value in  pet.items():
        print(key + ":  " + value + "         ", end='')
    print("")

print("...............................6-9................................")
favorite_places = {
    "jake": ["New York", "Chicago", "Boston"],
    "brad": ["Miami", "Philadelphia", "San Francisco"],
    "will": ["Los Angeles", "Las Vegas", "Seattle", "Washington"],
}
for name, places in favorite_places.items():
    print(name.title() + " likes :    ",end="")
    for place in places:
        print(place.title(), end='')
        if place == places[-1]:
            print("")
# 这个print语句默认换行
#            print("\n")
# 这个print语句还要再换一次行，相当于空了一行
        else:
            print(",     ", end='')
# print 里面 end="" 为不换行

print("...............................6-11................................")
cities = {
    'Paris' : {'Country': 'France', 'population': 67000000, 'fact': 'romantic'},
    'London' : {'Country': 'England', 'population': 66490000, 'fact': 'luxury'},
    'Amsterdam': {'Country': 'Holland', 'population': 17260000, 'fact': 'Football'},
}
# 字典最后一个键值对后面可以加逗号，也可以不加
for city, summay in cities.items():
    print(city,end='')
    for key, value in summay.items():
        print(key + " :  " + str(value) + "     ", end='')
    print("")













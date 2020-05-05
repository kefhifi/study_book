name = "jack chen"
print(name)
print(name.title())

print(".....................分割线-1....................")
name="brad pitt"
print(name)
print(name.lower())
print(name.upper())
print(name.title())
print(".....................分割线-2.5....................")
name="Albert Einstein"
words="A person who never made a mistake never tried anything new."
print(name+" once said, \""+words+"\"")
print(f'{name} once said, "{words}"')
print(".....................分割线-2.6....................")

name="  brad pitt  "
print(name)
print(name.lstrip())
print("\n"+name.rstrip())
print("\t\n"+name.strip())

print("....................2.4.3...........................")
age=23
messages="Happy " + str(age) +"rd Birthday!"
print(messages)
print("Happy " + str(age) +"rd Birthday!")

print("....................3.1............................")
all=["bike","car","you"]
print(all)
print(all[0])
print(all[2].title())
for item in all:
    print(item.title())
print(all[-1])
print(all[-2])
all[0]="Honda"
print(all)
all.append("ford")
print(all)
all.insert(0,"nissan")
print(all)
# 上一行输出：['nissan', 'Honda', 'car', 'you', 'ford']
#删除元素
del all[3]
print(all)
# 上一行输出；['nissan', 'Honda', 'car', 'ford']
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
# 上一行输出：['honda', 'yamaha']
print(popped_motorcycle)
# 上一行输出：suzuki
# 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha','ducati', 'suzuki', 'ducati']
print(motorcycles)
# 输出：['honda', 'yamaha', 'ducati', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
# 输出：['honda', 'yamaha', 'suzuki', 'ducati']
# 证明只删除了第一个匹配的元素

motorcycles = ['honda', 'yamaha','ducati', 'suzuki', 'ducati']
print(motorcycles)
for item in motorcycles:
    if item=="ducati":
        motorcycles.remove("ducati")
print(motorcycles)
print("....................3-4............................")
vistors=["tom","brad","jack"]
for item in vistors:
    print(item+" welcome to dinner")
print("....................3-5............................")
old_vistor="tom"
new_vistor="kate"
vistors.remove(old_vistor)
vistors.append(new_vistor)
print(vistors)
print(old_vistor+" could not come")
print("....................3-5-替换..错误解法...........................")
vistors=["tom","brad","jack"]
print(vistors)
# 输出：['tom', 'brad', 'jack']
old_vistor="tom"
new_vistor="kate"
for item in vistors:
    if item==old_vistor:
        item=new_vistor
print(vistors)
# 输出：['tom', 'brad', 'jack']
print("....................3-5-替换..正确解法...........................")
vistors=["tom","brad","jack"]
print(vistors)
# 输出：['tom', 'brad', 'jack']
old_vistor="tom"
new_vistor="kate"
i=0
for item in vistors:
    if item==old_vistor:
        vistors[i]=new_vistor
    i+=1
print(vistors)
# 输出：['kate', 'brad', 'jack']
print("....................3-6...........................")
vistors=["tom","brad","jack"]
print(vistors)
# ['tom', 'brad', 'jack']
vistors.insert(0,"kate")
print(vistors)
# ['kate', 'tom', 'brad', 'jack']
vistors.insert(2,"mira")
print(vistors)
# ['kate', 'tom', 'mira', 'brad', 'jack']
vistors.append("julia")
print(vistors)
# ['kate', 'tom', 'mira', 'brad', 'jack', 'julia']
print("....................3-7...........................")
while len(vistors) > 2:
    out_vistor = vistors.pop()
    print(out_vistor+" not come")
print(vistors)
del vistors[1]
del vistors[0]
print(vistors)
# 3.3.1 使用方法sort()对列表进行永久性排序
print(".............使用方法sort()对列表进行永久性排序........................")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)
# ['toyota', 'subaru', 'bmw', 'audi']

# 3.3.2 使用函数sorted()对列表进行临时排序
print(".............使用函数sorted()对列表进行临时排序........................")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
# ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the sorted list:")
print(sorted(cars))
# ['audi', 'bmw', 'subaru', 'toyota']
print("Here is the original list again:")
print(cars)
# ['bmw', 'audi', 'toyota', 'subaru']


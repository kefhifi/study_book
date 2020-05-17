#列表去重
L = [1,2,3,4,5,6,6,5,4,3,2,1]

#第一种方法，利用字典的fromkeys()和keys()方法
#创建一个空字典
d = {}

#用字典的fromkeys()方法去重，得到一个字典，去重之后的元素为键，值为None的字典
#{1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
#fromkeys(iterable,value=None)
L = d.fromkeys(L)
print(L) #{1: None, 2: None, 3: None, 4: None, 5: None, 6: None}

#用字典的keys()方法得到一个类似列表的东西，但不是列表。keys()函数返回的是一个dict_keys对象：
#以字典的键作为元素的一个类列表
L = L.keys()
#print(L) #dict_keys([1, 2, 3, 4, 5, 6])

L = list(L)
print(L)  #[1, 2, 3, 4, 5, 6]

#可以用列表的sort()方法排序，默认是升序
# print(L.sort())
L.sort(reverse=True) #升序
print(L)#[6, 5, 4, 3, 2, 1]


print('-----------------------------')
#第二种方法，集合,集合是可迭代的
L2 = [1,2,3,4,5,6,6,5,4,3,2,1]
L2=set(L2)
print(L2) #{1, 2, 3, 4, 5, 6}

L2 = list(L2)
print(L2) #[1, 2, 3, 4, 5, 6]

print('-------------------------------')
#第三种方法，用for循环
L3 = [1,2,3,4,5,6,6,5,4,3,2,1]
L4 = []
for x in L3:
    if x not in L4:
        L4.append(x)
print(L4) #[1, 2, 3, 4, 5, 6]

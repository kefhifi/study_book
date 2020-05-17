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


print("..........................6-4.......................")
dic_table={"for":"loop_1","while":"loop_2","in":"loop_in ","with":"open file use","as":"to be"}
dic_table["if"]="assume"
dic_table["else"]="another aspect"
dic_table["class"]="define class"
dic_table["def"]="define"
dic_table["and"]="2 condition"
for key,value in dic_table.items():
    print(key + ": " + value)

print(".........................9-13.............................")
from collections import OrderedDict
dic_table=OrderedDict()
dic_table["for"]="loop_1"
dic_table["while"]="loop_2"
dic_table["in"]="loop_in"
dic_table["with"]="open file use"
dic_table["as"]="to be"
dic_table["if"]="assume"
dic_table["else"]="another aspect"
dic_table["class"]="define class"
dic_table["def"]="define"
dic_table["and"]="loop_1"
for key,value in dic_table.items():
    print(key + ": " + value)

print(".........................9-14.............................")
from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,sides))
the_die=Die()
the_die.roll_die()



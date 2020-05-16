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













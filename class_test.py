#导入多个类
#from animal_class import Animal, Dog, Cat
#导入所有类，不推荐，可能包含重复类，无法看到类名
#from animal_class import *
"""
animal1 = Animal("xcmt",10)
#print("这只小动物叫"+dog1.name+"，他今年"+str(dog1.age)+"岁了！")
animal1.ret()      #这只小狗叫xcmt，他今年10岁了！

dog1 = Dog("sdlkjas")
dog1.ret()
dog1.sound()
"""
#测试类   unittest
#先运行setUp()  然后运行test_开头的方法
import unittest
from animal_class import Dog
class dog_test(unittest.TestCase):
    def setUp(self):
        self.dog2 = Dog("tysad")
        #dog2.sound()   "汪汪~"
        self.sound = self.dog2.sound()
    def test_dog_sound(self):
        self.assertEqual(self.sound,"汪汪~")      #a==b?
        self.assertNotEqual(self.sound,"汪~")     #a!=b?
        self.assertTrue(self.sound)                #a为True?
        self.assertFalse(0)                #a为TFalse?
        self.assertIn(self.sound,"汪汪~")         #a in b?
        self.assertNotIn(self.sound,"汪汪")      #a not in b?
        

unittest.main()
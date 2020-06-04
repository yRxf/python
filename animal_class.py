#类
class Animal():
    def __init__(self,name,age=""):
        self.name = name
        self.age = age
        self.animal_type = ""
    
    def ret(self):
        message = "这只"+self.animal_type+"叫"+self.name if self.animal_type else "这只小动物叫"+self.name
        if self.age:
            message+="，他今年"+str(self.age)+"岁了！"
        print(message)

 #继承，创建子类
class Dog(Animal):
    def __init__(self,name,age=""):
        super().__init__(name,age)      #super()关联父类和子类，让子类拥有父类所有属性
        self.animal_type = "小狗"
    def sound(self):
        print("汪汪~")
        return "汪汪~"

 #继承，创建子类
class Cat(Animal):
    def __init__(self,name,age=""):
        super().__init__(name,age)
        self.animal_type = "小猫"
    def sound(self):
        print("喵喵~")
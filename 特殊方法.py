"""类的特殊方法"""
#https://docs.python.org/zh-cn/3/reference/datamodel.html
"""字符串/字节序列表示形式"""
#__repr__、__str__  相当于定义print方法？
#__format__   格式化输出
#print("the point is x:{}, y:{}".format(1,2))    #the point is x:1, y:2
#print("the point is x:{x}, y:{y}".format(y=2,x=1))    #the point is x:1, y:2
"""
formats = {
    'normal': 'x: {p.x}, y: {p.y}',
    'point' : '({p.x}, {p.y})',
    'prot': '<{p.x}, {p.y}>'
}
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, code):
        return formats[code].format(p=self)

print('the point is {:point}'.format(point(1,2)))   #the point is (1, 2)
"""

"""数值转换"""
#__abs__、__bool__、__complex__、__int__、__float__、__hash__、__index__
"""集合模拟"""
#__xxxitem__:使用 [''] 的方式操作属性时被调用
#__setitem__:每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
#__getitem__:当访问不存在的属性时会调用该方法
#__delitem__:当删除属性时调用该方法
#__contains__():当使用in对象的时候
"""迭代枚举"""
#__iter__:此方法在需要为容器创建迭代器时被调用。此方法应该返回一个新的迭代器对象，它能够逐个迭代容器中的所有对象。
#__next__
#__reversed__

#实例创建和销毁
#__new__、__init__、__del__





















"""运算符有关的特殊方法"""
#一元运算符：__neg__(self) -、__add__(self) +、__abs__(self) abs()、__invert__(self) ~
#比较运算符：__lt__(self, other) <、__le__(self, other) <=、__eq__(self, other) ==、__ne__(self, other) !=、__gt__(self, other) >、__ge__(self, other) >=
#算数运算符：__add__(self, other) +、__sub__(self, other) -、__mul__(self, other) *、__truediv__(self, other) /、__floordiv__(self, other) //、__mod__(self, other) %
#__divmod__(self, other) divmad()  它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。
#对于整数，结果和 (a // b, a % b) 一致。对于浮点数，结果是 (q, a % b)
#print(divmod(5,2))      #(2, 1)
#print(divmod(5.0,2.6))      #(1.0, 2.4)
#__pow__(self, other[, modulo]) ** 或 pow()
#print(2**3)     #8
#print(pow(2,3,3))   #2**3%3
#print(4**0.5)   #2.0
#__lshift__(self, other) << 、__rshift__(self, other) >>
#__and__(self, other) & 、__xor__(self, other) ^ 、__or__(self, other) |
#__matmul__(self, other) @
#__rxxx__(self, other)  交换操作数进行运算
#__ixxx__(self, other)  算数赋值运算  +=、-=、...
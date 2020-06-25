#msg = "Hello World"
#msg = "hello world"
#msg = " hello world "
#print(msg.strip().title())

#字符串拆分  split()
#list_msg = msg.split()
#print(list_msg)             #['hello', 'world']
#msg1 = "1-2-3-4-5-6"
#print(msg1.split('-'))      #['1', '2', '3', '4', '5', '6']
#print(msg1.split('-',2))    #['1', '2', '3-4-5-6']

#列表
#插入元素  append()、insert()
#删除元素  del()、pop()、remove()
#list_ = ["one", "two", "three"]
#list_.append("four")    #['one', 'two', 'three', 'four']
#list_.insert(1,"four")  #['one', 'four', 'two', 'three']
#del list_[1]            #['one', 'three']
#print(list_.pop())      #three  弹出末尾元素  list_=['one', 'two']
#list_.remove("two")     #['one', 'three'] remove根据值删除1个元素 

#排序
#sort()  #永久性排序 默认升序 reverse=Treu  降序
#list_.sort()            #['one', 'three', 'two']
#list_.sort(reverse=True)            #['two', 'three', 'one']

#sorted()  #临时排序，不影响原列表
#print(sorted(list_))        #['one', 'three', 'two']
#print(list_)                #['one', 'two', 'three']

#reverse  #永久性反转排序
#list_.reverse()             #['three', 'two', 'one']
#print(list_)

#range(min, max, step)  生成数字 [min, max) 步长为step 的数字  
#for i in range(0,5):
#    print(i)  #0\n1\n2\n3\n4
#list_ = list(range(0, 5))   #[0, 1, 2, 3, 4]
#list_ = list(range(0, 10, 2))   #[0, 2, 4, 6, 8]  
#print(list_)

#squares = [value ** 2 for value in range(1, 11)]
#print(squares)      #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#print("hello")      #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#复制列表
#list2_ = list_[:]  #['one', 'two', 'three']
#引用列表
#list2_ = list_      #['one', 'two', 'three']
#print(list2_)
#list_.append("four")    #['one', 'two', 'three', 'four']
#print(list2_)
#判断列表是否为空
#list3_ = []
#print("空") if not list3_ else print("非空")

#元组，与列表类似，不可改变，可整个重新赋值
#dimensions_ = ('one', 'two', 'three')   #('one', 'two', 'three')
#dimensions_[1] = "2"        #报错：'dimensions_' does not support item 
#dimensions_ = ('four','five')   #('four', 'five')
# print(dimensions_[0])

#字典
#dic = {"name":"L"}  #{'name': 'L'}
#添加字典
#dic["age"] = 17     #{'name': 'L', 'age': 17}
#del dic["name"]     #{'age': 17}
#遍历字典
#for key,value in dic.items():       #遍历自带换行
#    print(key+":"+str(value))      #name:L \n age:17
#遍历所有的键
#for key in dic.keys():
#    print(key)                     #name  \n   age
#遍历所有的值
#for value in dic.values(): 
#    print(value)                    #L \n 17

#用户输入  3.0 input  2.7  因使用 raw_input() 获取输入信息
#name = input("请输入您的名字：")
#print(name)

#while循环
"""message = ""
while message != "q":
    message = input()
    print(message)
"""

#删除列表中的特定元素
"""
list4_ = ["a","b","a","c","b","a","c","d"]
while "a" in list4_:
    list4_.remove("a")
print(list4_)       #['b', 'c', 'b', 'c', 'd']
"""
"""
def test(list_):
    list_.pop()

list5_ = ["a","b","c"]
test(list5_[:])     #['a', 'b', 'c']
test(list5_)        #['a', 'b']
"""


# *传递任意长参数，**传递关键字，即创建一个空字典
"""
def test1(*args:list,**dics:dict) -> str:
    '''测试，__doc__'''
    if args:
        for arg in args:
            print(arg)
    else:
        print("没有传递参数！")
    if dics:
        for key,value in dics.items():
            print(key+":"+value)
    else:
        print("没有传递字典！")

#test1()     #没有传递参数！ 没有传递字典！
#test1("dasklj","dashjk")        #dasklj  dashjk  没有传递字典！
#test1(lala = "k",nana = "c")        #没有传递参数！  lala:k  nana:c
#test1("dsaljk","dsaljkhxkj",la = "lala")    #dsaljk  dsaljkhxkj  la:lala
#print(test1.__doc__)        #测试，__doc__
#print(test1.__annotations__)        #{'args': <class 'list'>, 'dics': <class 'dict'>, 'return': <class 'str'>}
"""
"""
#__call__     实现()运算符
class Sum_sum:
    '''动态累加'''
    def __init__(self):
        self.points = []
    def __call__(self,*new_points):
        if new_points:
            for new_point in new_points:
                self.points.append(new_point)
        return sum(self.points)
he = Sum_sum()
#print(he(1))            #1
#print(he(5,5))          #11
#print(he(100))          #111
"""
#导入模块
"""
import test1
from test1 import test1 as t1       #as 函数别名
test1.test1()     #没有传递参数！ 没有传递字典！
test1.test1("dasklj","dashjk")        #dasklj  dashjk  没有传递字典！
test1.test1(lala = "k",nana = "c")        #没有传递参数！  lala:k  nana:c
test1.test1("dsaljk","dsaljkhxkj",la = "lala")
t1("daskdlj")
"""


#内置函数
#eval() :函数用来执行一个字符串表达式，并返回表达式的值。
#enumerate()：enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#enumerate(sequence, [start=0])     #start -- 下标起始位置。
#isinstance()：判断一个对象是否是一个已知的类型，类似 type()。
#isinstance(object, classinfo)      #classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
#execfile()：函数可以用来执行一个文件。     #python3 删去了 execfile()
# exec()：函数可以用来执行一段表达式
#execfile('animal_class.py')        #3.0后NameError: name 'execfile' is not defined
#with open('class_test.py','r',encoding='UTF-8') as f:
#    exec(f.read())
#super()：函数是用于调用父类(超类)的一个方法
#bin()：返回一个整数 int 或者长整数 long int 的二进制表示
#oct():返回一个整数转换成8进制字符串。
#file()  别名：open()？
#raw_input()：将所有输入作为字符串看待，返回字符串类型。  3.0以下使用，3.0后input() 默认接收到的是 str 类型。
#unichr() 函数:unichr() 函数 和 chr()函数功能基本一样， 只不过是返回 unicode 的字符。 3.0后取消了，请使用chr()
#callable():用于检查一个对象是否是可调用的。可用于检验是否有__call__方法？
#对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
#str.format()：格式化函数
#基本语法是通过 {} 和 : 来代替以前的 %
#print("{} {}".format("hello","world!"))
#locals():以字典类型返回当前位置的全部局部变量。
#globals():以字典类型返回当前位置的全部全局变量。
#reload() 用于重新载入之前载入的模块
#getattr():返回一个对象属性值。
#reverse():就地对列表的元素进行反向排序。
#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
#zipped = zip('1 2 3'.split(),range(1,4))
#解压：
#a,b = zip(*zipped)
#print(a,b)      #('1', '2', '3') (1, 2, 3)
#print("%s %s"%zip(*zipped))     #[('1', 1), ('2', 2), ('3', 3)]
#__import__() 函数用于动态加载类和函数 。
#如果一个模块经常变化就可以使用 __import__() 来动态载入。
#hasattr()：用于判断对象是否包含对应的属性。
#delattr()：用于删除属性。  delattr(x, 'foobar') 相等于 del x.foobar。
#assert： 如果条件不成立，则打印出 '这是异常信息' 并抛出AssertionError异常
#assert 1==2, '这是异常信息'         #AssertionError: 这是异常信息

#优先级：NOT、AND、OR。
'''
#for......else......
#while......else......
#当循环正常结束时会执行else，如果非正常结束(break等)，不会执行else
#for......else......的执行顺序为：
for x in range(5):
    if x == 2:
        print(x)
        # break
else:
    print("执行else....")
"""
2
执行else....
"""
'''

#列表去重
l = [2,1,2,3,4,5,6,6,5,4,3,2,1]
#不考虑顺序去重  set()
#print(list(set(l)))     #[1, 2, 3, 4, 5, 6]
#考虑顺序  fromkeys()
print(list({}.fromkeys(l).keys()))      #[2, 1, 3, 4, 5, 6]
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

"""
# *传递任意长参数，**传递关键字，即创建一个空字典
def test1(*args,**dics):
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


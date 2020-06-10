#元组拆包
"""
x,y = (1,2)
print("%d、%d" % (x,y))     #1、2
x,y = y,x       #交换两个元素
print("%d、%d" % (x,y))     #2、1
"""
"""
points = [("x",1),("y",2)]
for point in points:
    print("%s:%d" % point)          #x:1  y:2   列表会报错
"""
"""
#*可把元组拆开作为函数参数
print(divmod(20,8))
t = (20,8)
print(divmod(*t))
#*处理剩下元素
a,b,*rest,c = range(5)    #a=0,b=1,rest=[2,3],c=4
a,b,*rest,c,d,e = range(5)    #rest=[]
"""
"""
from collections import namedtuple
point = namedtuple("point",'x y z')
point1 = point(1,2,3)       #point(x=1, y=2, z=3)
print(point1.y)             #2
print(point1._fields)       #('x', 'y', 'z')
point2 = point1._make(range(4,7))   #point(x=4, y=5, z=6)
#_make() 跟 *类似相当于以下代码
a = range(4,7)
point2 = point(*a)   #point(x=4, y=5, z=6)
#point2 = point(*range(4,7))   #point(x=4, y=5, z=6)
print(point2._asdict())     #{'x': 4, 'y': 5, 'z': 6}
"""
"""
#元组没有__reversed__方法，但可以使用reversed(tuple)
points = range(5)
for point in reversed(points):
    print(point)               #4  3  2  1  0
"""
#元组方法：
#s.__contains__(e)      即 in
#s.count(e)             e出现的次数
#s.__getitem__(p)       即s[p]
#s.__getnewargs__()     列表没有，元组有
#s.index(e)             e第一次出现的位置
#s.__iter__()           迭代器
#s.__len__()            len(s)
#s.__mul__(n)           s * n  n个s重复拼接
#s.__rmul__(n)          n * s  反向拼接

#切片操作   slice(a,b,c)
#s = 'bicycle'
#s[a:b:c]               在a和b直接以c为间隔取值，c可以为负数
#print(s[slice(3,None)])  #ycle
#print(s[3:])            #从下标为3的地方分割，ycle
#print(s[::3])           #对s每隔3个取一次值，bye
#print(s[::-1])          #elcycib
#print(s[:3:-1])         #elc
#print(s[3::-2])         #yi
#赋值
#s[:3] = ['a']           #TypeError: 'str' object does not support item assignment
#l = list(range(10))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#l[:3]                  #[0, 1, 2]
#l[:3] = [-1]            #[-1, 3, 4, 5, 6, 7, 8, 9]
#l[:3] = list(range(10,15))  #[10, 11, 12, 13, 14, 3, 4, 5, 6, 7, 8, 9]
#del l[:3]               #[3, 4, 5, 6, 7, 8, 9]
#print(l*2)              #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(l+list(range(10,15)))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
"""
#l1 = [['_']*3] * 3           #[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]                   
#l得到的其实是3个['_', '_', '_']的引用 而不是3个['_', '_', '_']里面的值
#l1[1][1] = 'X'           #[['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
#等同于以下操作：
l = ['_']*3
l1 = []
for i in range(3):
    l1.append(l)        #每一次都将l加入
    #l1.append(l[:])        #每一次都将l所有值加入
l1[1][1] = 'X'
print(l1)
"""
"""
l2 = [['_']*3 for i in range(3)]
l2[1][1] = 'X'          #[['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
print(l2)
#等同于以下操作：
l2 = []
for i in range(3):
    l = ['_']*3         #每一次都新建一个列表加入
    l2.append(l)    
l2[1][1] = 'X'
print(l2)
"""
'''
#对元组进行+=运算
#元组元素是不能修改的，但下面t确实修改了
t = (1,2,[3,4])
"""
try:
    t[2]+=[5,6]     #TypeError: 'tuple' object does not support item assignment
except TypeError:
    print(t)        #(1, 2, [3, 4, 5, 6])
实际上：
1、将t[2]的值存入了TOS(TOP Of Stack，栈的顶端)
2、计算 TOS += [5,6]，即[3,4] += [5,6] 这一步是可以完成的，TOS一个可变对象
3、对t[2] = TOS 赋值。失败，因为t是不可变的元组
"""
TOS = t[2]     #[3, 4]  TOS即是t[2]的引用
#TOS = t[2][:]     #[3, 4]  TOS即是t[2]的值
TOS += [5,6]   #[3, 4, 5, 6]   即t[2]已经是[3, 4, 5, 6]
print(t)        #(1, 2, [3, 4, 5, 6])
try:
    t[2] = TOS
except TypeError:
    print(t)
#t[2].extend([5,6])  #(1, 2, [3, 4, 5, 6])   没有异常可以实现
#print(t)
'''

#排序
#list.sort  就地排序，即不会；把原列表拷贝一份进行排序
#内置函数 sorted 会新建一个列表作为返回值，故可以接受任何形式的参数(可变、不可变、...)，最终都会返回一个列表
#sorted  可选关键字参数：
#reverse：如果设定为True，则降序排列（由大到小），默认是False
#key：排序算法依赖对比的关键字，如key=str.lower忽略大小写排序，key=len以长度进行排序
#l = list(range(5,0,-1))     #[5, 4, 3, 2, 1]
#print(l.sort())             #返回#None会被忽略
#print(l)                    #[1, 2, 3, 4, 5]
#None：如果一个函数或者方法对对象进行的是就地改动，返回None，让调用者只读传入的参数发生了变化并未产生新的对象

#fruits = ['grape', 'raspberry', 'apple', 'banana']
#print(sorted(fruits))       #['apple', 'banana', 'grape', 'raspberry']
#原fruits排序没有变化
#print(fruits)               #['grape', 'raspberry', 'apple', 'banana']
#print(sorted(fruits,reverse=True))       #['raspberry', 'grape', 'banana', 'apple']
#print(sorted(fruits,key=len))           #['grape', 'apple', 'banana', 'raspberry']
#fruits.sort()               #原排序发生了变化
#print(fruits)               #['apple', 'banana', 'grape', 'raspberry']
"""
l = [28,14,'28',1,'12',5,0,6,19,23,'27']
print(sorted(l,key=int))        #[0, 1, 5, 6, '12', 14, 19, 23, '27', 28, '28']
print(sorted(l,key=str))        #[0, 1, '12', 14, 19, 23, '27', 28, '28', 5, 6]
"""
#有序序列插入元素
#bisect(haystack, needle) 
#在haystack中查找needle的位置
#导入bisect
'''
import bisect
#l = list(range(1,10,2))     #[1, 3, 5, 7, 9]
#index = bisect.bisect(l,6)  #3
#l.insert(index,6)           #[1, 3, 5, 6, 7, 9]
#使用bisect.insort()插入新元素
#bisect.insort(l,6)          #[1, 3, 5, 6, 7, 9]
#print(l)
"""分数跟成绩对应函数"""
def grade(score,points=[60,70,80,90,100],grade='FDCBAS'):
    i = bisect.bisect(points,score)
    return grade[i]
print([grade(score) for score in [33,99,77,70,89,90,100]])      #['F', 'A', 'C', 'C', 'B', 'A', 'S']


'''
#数组 array
#数组对数字类型文件的读写操作
#array.tofile  写方法
#array.fromfile 读方法
#from array import array
#from random import random
#创建一个double(d)型的数组
#floats = array('d',(random() for i in range(10**7)))
"""
with open('floats.bin','wb') as fp:
    floats.tofile(fp)
floats2 = array('d')
with open('floats.bin','rb') as fp:
    floats2.fromfile(fp,10**7)
"""
#对数组进行复制操作copy.copy、copy.deepcopy
#导入copy包里的copy
#from copy import copy
#from copy import deepcopy
#floats2 = copy(floats)
#print(floats2[-1] == floats[-1])        #True
'''
"""copy.copy和copy.deepcopy的区别"""
"""经过copy操作得到的两个拥有不同的地址，但列表里面如果还有列表，则里面的列表拥有相同的地址，即如果修改里面的列表，原列表也会被修改
经过deepcopy操作得到的两个拥有不同的地址，且列表里面如果还有列表，则里面的列表也拥有不同的地址，即对新列表操作不影响原列表"""
list1 = list(range(3))+[[11,22]]    #[0, 1, 2, [11, 22]]
n_list2 = copy(list1)
d_list2 = deepcopy(list1)
#对使用deepcopy的列表进行操作
d_list2[-1]+=[12]
#原列表的值没有被修改
print(list1)                    #[0, 1, 2, [11, 22]]
print(d_list2)                  #[0, 1, 2, [11, 22, 12]]
#对使用copy的列表进行操作
n_list2[-1]+=[12]
#原列表的值被修改
print(list1)                    #[0, 1, 2, [11, 22, 12]]
print(n_list2)                  #[0, 1, 2, [11, 22, 12]]
'''
'''
array1 = array('b',(1,2,3))     #一个存储byte类型的数组array('b', [1, 2, 3])
#使用extend()添加可迭代列表，如果有TypeError异常，之前添加的元素还存在
#使用fromlist()添加可迭代列表，如果有TypeError异常，则取消所有添加
"""
try:
    array1.extend((4,5,'6'))    #array('b', [1, 2, 3, 4, 5])
except TypeError:
    print(array1)  
"""
"""
try:
    array1.fromlist((4,5,'6'))    #array('b', [1, 2, 3])
except TypeError:
    print(array1) 
"""
'''
#s.itemsize         返回数组中元素长度的字节数'b':1、'i':4、'f':4、'l':4、'd':8
#s.typecode         返回数组的存储类型：b、i、...
#s.tolist()         转换为列表，元素是数字对象
#数组排序  python 3.4后数组类型不再支持list.sort()这种就地排序方法。要排序只能新建一个数组
#array1 = array('b',(2,1,6))
#array1 = array(array1.typecode,sorted(array1))  #array('b', [1, 2, 6])
#print(array1)
#对已是有序序列的数组可以使用bisect.insort进行插入
#import bisect
#bisect.insort(array1,5)                        #array('b', [1, 2, 5, 6])

#memoryview
#Numpy
#SciPy

#双向队列  collections.deque
#from collections import deque
#dq = deque(range(7), maxlen=7)       #deque([0, 1, 2, 3, 4, 5, 6], maxlen=7), maxlen=5)  
#maxlen  可选参数，表示队列最大容纳元素的数量，一旦设定无法改变
#.rotate(n)，当n>0,表示把最右n个元素移到队列左边，当n<0时，将最左移到右边
#dq.rotate(3)                        #deque([4, 5, 6, 0, 1, 2, 3], maxlen=7)
#dq.rotate(-3)                       #deque([3, 4, 5, 6, 0, 1, 2], maxlen=7)
#appendleft在队列头部添加元素，append在队列尾部添加元素
#extendleft按迭代器里面的元素逐个添加，故会逆序出现在队列
#当len()>maxlen时会挤掉另一端元素
#dq.appendleft(-1)                   #deque([-1, 0, 1, 2, 3, 4, 5], maxlen=7)
#dq.append(-1)                       #deque([1, 2, 3, 4, 5, 6, -1], maxlen=7)
#dq.extend([11,12,13])               #deque([3, 4, 5, 6, 11, 12, 13], maxlen=7)
#dq.extendleft([11,12,13])            #deque([13, 12, 11, 0, 1, 2, 3], maxlen=7)
#pop()、popleft()
#print(dq)


#字典(dict)
"""
#创建一个{'one': 1, 'two': 2, 'three': 3}的字典
a = dict(one=1,two=2,three=3)
b = {'one':1,'two':2,'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2),('one',1),('three',3)])
e = dict({'three':3,'one':1,'two':2})
print(a==b==c==d==e)            #True
"""
#字典推导：
#l = [(1, 'one'), (2, 'two'), (3, 'three')]
#dict1 = {s_num:num for num,s_num in l}      #{'one': 1, 'two': 2, 'three': 3}
#d.keys()               所有的键
#d.values()             所有的值
#d.get(k,[default])     返回键k对应的值，如果不存在则返回None或[default]
#d.setdefult(k,[default])     返回键k对应的值，如果不存在则添加d[k] = [default],然后返回[default]
#print(dict1.get('one'))                     #1
#print(dict1.get('o'))                     #None
#print(dict1.get('o','not found'))          #not found
#print(dict1.setdefault('one'))              #1
#print(dict1.setdefault('four',4))              #4   dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
#d.items()  返回所有的键值对
#for key,value in dict1.items():
#    print(key+":"+str(value))               #one:1    two:2    three:3
#d.pop(k,[default])                         #返回k所对应的键，并移除，如果不存在则返回None或[default]
#d.popitem()                            #返回最后一个键值对并移除它吧！！！有些资料上写着作用是随机返回（翻译有误吧）一个键值对并移除它，但测试了一下是返回最后一个
#print("key:%s,value:%d"%dict1.popitem())    #key:three,value:3
#for i in range(10):
#    dict1 = dict(zip('a b c d e f g h i j k l n m o p q r s t u v w x y z'.split(),list(range(1,27))))
#    print("key:%s,value:%d"%dict1.popitem())    #输出结果全是key:z,value:26
#d.update(m, [**kargs]) 如果key已存在，则会更新对应的value
#如果m存在keys方法，则对dict1更新m和[**kargs]
#如果不存在则会当作包含键值对(key,value)元素的迭代器
#dict1.update(dict1,four=4,five=5)           #{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
#dict2 = {'four':4,'five':5,'one':11}
#d = zip(['eight','nine'],[8,9])
#dict1.update(dict2,six=6,nana=7)           #{'one': 11, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'nana': 7}
#dict1.update(d,one=1)           #{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'nana': 7, 'eight': 8, 'nine': 9}
#print(dict1)
"""
#__missing__
#基类dict没有定义这个方法，但dict是知道有这么一个方法。
#如果一个类继承了dict且提供了一个__missing__方法，那么在__getitem__找不到键时(d[k])，会调用它

class StrKeyDict(dict):
    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()
    
str_dict = StrKeyDict({'1':'one','2':'two','3':'three'})
print(str_dict[1])      #one
#str_dict[1]先调用__getitem__方法，没有找到，调用__missing__
#__missing__方法先是判断1是不是字符串，如果是直接引发异常，如果不是将其返回用字符串再查一遍
"""
#其他字典
"""
#collections.Counter    用于计算各个字母出现的次数
#most_common([n])       返回计数中最常见的n个键和它的计数
from collections import Counter
ct = Counter('sadhjkashcjaksga')        #Counter({'a': 4, 's': 3, 'h': 2, 'j': 2, 'k': 2, 'd': 1, 'c': 1, 'g': 1})
#ct = Counter(a=5,b=1,c=7)
ct.update('asddasd')                    #Counter({'a': 6, 's': 5, 'd': 4, 'h': 2, 'j': 2, 'k': 2, 'c': 1, 'g': 1})
ct2 = Counter('vo da vi vi'.split())    #Counter({'vi': 2, 'vo': 1, 'da': 1})
ct2.update('vo da vi vi'.split())       #Counter({'vi': 4, 'vo': 2, 'da': 2})
print(ct.most_common(3))                #[('a', 6), ('s', 5), ('d', 4)]
"""
#不可变映射类型
#types.MappingProxyType
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)       #{1: 'A'}
#d_proxy[2] = 'B'                    #TypeError: 'mappingproxy' object does not support item assignment
#d[2] = 'B'                          #d_proxy = {1: 'A', 2: 'B'}
#print(d_proxy)      

#集合
#set、frozenset
#a|b，a与b的合集  a&b，a与b的交集  a-b，a与b的差集
s = {1}                            #type:<class 'set'>      {1}
print(s.pop())                     #1   s:set()
#空集
#s = {}                              #type:<class 'dict'>
#s = set()                           #type:<class 'set'>
#print(type(s))    
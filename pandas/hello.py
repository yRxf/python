#numpy
#import numpy as np
#data = [1,2,3,4,5,6]    #[1, 2, 3, 4, 5, 6]
#一维数组
#x = np.array(data,dtype=np.int16)      #[1 2 3 4 5 6] dtype设置类型
#二维数组
#x = np.array([[1,2,3],[4,5,6],[7,8,9]])   #3*3矩阵
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
#print(x.ndim)           #矩阵维度：2
#print(x.shape)          #(3, 3)  矩阵各个维度的长度
#x=np.zeros((2,3))        #生成全0矩阵
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''
#x=np.ones((2))          #生成全一矩阵，全其他矩阵可以在后面成个数
'''[1. 1.]''' 
#x = np.empty((2,1))     #生成未被初始化的矩阵
#eye():返回一个单位矩阵，对角线上的值为1
#identity():返回给定大小的单位对角矩阵
#rand():返回给定大小的填充随机值的矩阵  0~1直接
#使用arrange生成连续元素,和range相似
#x = np.arange(0,6,2)        #生成[0,6)步长为2的数组：[0 2 4]
#x = np.array([1,2.7,3.2],dtype=np.float64)      #[1.  2.7 3.2]
#使用astype复制转换类型
#y = x.astype(np.int32)                          #[1 2 3]
#将字符串元素转换为数值元素 dtype=np.string_,转换为np.bytes类
#x = np.array(['1','2','3'],dtype=np.string_)    #[b'1' b'2' b'3']
#x = np.array(['1','2','3'],dtype=np.int16)    #[1 2 3]
#ndarray数组与标量/数组的运算
#对应相加减
#print(x>2)        #[False False  True]
#ndarray数组的基本索引和切片
#与Python的列表索引功能相似
#x = np.array([[1,2],[3,4],[5,6]])
'''
[[1 2]
 [3 4]
 [5 6]]
'''
#print(x[:])
'''
[[1 2]
 [3 4]
 [5 6]]
'''
#print(x[1:])      #下标由0开始第二行到最后
'''
[[3 4]
 [5 6]]
'''
#print(x[:2])      #开始到第二行
'''
[[1 2]
 [3 4]]
'''
#print(x[:2,:1])      #开始到第二行的开始到第一个数
'''
[[1]
 [3]]
'''
#x[:2,:1] = [[8],[6]] #赋值
'''
[[8 2]
 [6 4]
 [5 6]]
'''
#numpy.reciprocal():返回参数元素的倒数
#布尔索引和花式索引：
#x = np.arange(6)        #[0 1 2 3 4 5]
#print(x[~(x>=3)])       #[0 1 2]    判断x里大于等于3的值，取反，输出
#print(x[(x==5)|(x==2)]) #[2 5]
#print(x[[1,3,5]])       #[1 3 5]    x里面的第1，3，5个
#x = np.array([[1,2],[3,4],[5,6]])
#print(x[[0,2],[0,1]])   #[1 6]      打印[0][0]和打印[2][1]
#print(x[[0,1]][:,[0,0]])   #打印[0][:][0]、[0][:][0]、[1][:][0]、[1][:][0]
'''
[[1 1]
 [3 3]]
'''
#numpy.ix_()：
#print(x[np.ix_([0,1],[0,1])])       #等同于x[[0,1]][:,[0,1]]
'''
[[1 2]
 [3 4]]
'''

#数组的转置和轴对换
#k = np.arange(6)        #[0 1 2 3 4 5]
#x = k.reshape((2,3))   #reshape复制生成2*3的矩阵
'''
[[0 1 2]
 [3 4 5]]
'''
#print(x.T)        #转置
'''
[[0 3]
 [1 4]
 [2 5]]
'''
#计算矩阵的内积 xTx
#print(np.dot(x,x.T))    #.dot 点乘
#高维数组（张量）的轴对象
#k = np.arange(8).reshape(2,2,2)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
#print(k[1][0][0])       #4
#m = k.transpose((1,0,2)) # m[y][x][z] = k[x][y][z]
#等价于：
#m = k.swapaxes(0,1)     #将第一个轴和第二个轴交换
'''
[[[0 1]
  [4 5]]

 [[2 3]
  [6 7]]]
'''

#通用函数:
#x = np.array([1.1,1.3,2.5,2.4])
#y,z = np.modf(x)
#print(y)          #[0.1 0.3 0.5 0.4]
#print(z)          #[1. 1. 2. 2.]

#x = np.array([[1,4],[6,7]])
#y = np.array([[2,3],[5,8]])
#print(np.maximum(x,y)) # [[2,4],[6,8]]
#print(np.minimum(x,y))# [[1,3],[5,7]]

#np.where(condition, x, y)，第一个参数为一个布尔数组，第二个参数和第三个参数可以是标量也可以是数组
#相当于if？如果condition为真，则x,否则y
#x = np.arange(6)
#print(np.where(x>3,1,-1))     #[-1 -1 -1 -1  1  1]
#numpy.extract():函数返回满足条件的元素
#numpy的基本统计方法
#sum求和、mean算数平均数、
#std标准差、var方差
#min、max
#argmin、argmax最小和最大元素的索引
#cumsum所有元素累计和
#cumprod所有元素累加积
#x = np.array([[1,2],[3,3],[1,2]])
#print(x.mean())         #2.0
#print(x.mean(axis=0))   #[1.66666667 2.33333333]    每一列求平均
#print(x.mean(axis=1))   #[1.5 3.  1.5]    每一行求平均
#print(x.cumsum())       #[ 1  3  6  9 10 12]
#print(x.cumprod())       #[ 1  2  6 18 18 36]
#numpy.ptp():返回指定轴中值的范围，或者说是最大值减去最小值
#布尔数组的统计
#sum : 统计数组/数组某一维度中的True的个数
#any： 统计数组/数组某一维度中是否存在一个/多个True
#all：统计数组/数组某一维度中是否都是True
#x = np.array([[True,False],[True,False]])
#print(x.sum())          #2
#使用sort对数组/数组某一维度进行就地排序
#x = np.arange(6,0,-1).reshape(2,3)
'''
[[6 5 4]
 [3 2 1]]
'''
#x.sort()
'''
[[4 5 6]
 [1 2 3]]
'''

#去重以及集合运算
#unique(x)  计算x中唯一的元素并返回有序结果
#x = np.array([[1,6,2],[6,1,3],[1,5,2]])
#print(np.unique(x))     #[1 2 3 5 6]
#intersect1d(x,y)  计算x和y中的公共元素并返回有序结结果
#y = np.array([1,6,5,-1])      #[1 5 6]
#print(np.intersect1d(x,y))
#union1d(x,y)  计算x和y的并集，并返回有序结果
#print(np.union1d(x,y))        #[-1  1  2  3  5  6]
#in1d(x,y)  得到一个表示”x的元素是否包含于y"的布尔数组
#print(np.in1d(x,y))           #[ True  True False  True  True False  True  True False]
#setdiff1d(x,y)  x和y的差集，即元素在x中且不在y中
#print(np.setdiff1d(x,y))      #[2 3]
#setxor1d(x,y)  对称差，即存在于一个数组中但不存在与另一个数组中,即setdiff1d(x,y)与setdiff1d(y,x)的集合
#print(np.setxor1d(x,y))       #[-1  2  3]
#print(np.union1d(np.setdiff1d(x,y),np.setdiff1d(y,x)))      #[-1  2  3]

#numpy中的线性代数
#import numpy.linalg 模块。线性代数（linear algebra）
#import numpy.linalg as nla
#常用的numpy.linalg模块函数：
#diag: 以一维数组的形式返回方阵的对角线（或非对角线）元素，或将一维数组转换为方阵（非对角线元素为0）
#dot:矩阵乘法
#trace:计算对角线元素的和
#det:计算矩阵行列式
#eig:计算方阵的特征值和特征向量
#inv:计算方阵的逆
#pinv:计算矩阵的Moore-penrose伪逆
#qr:计算QR分解
#svd:计算奇异值分解(SVD分解)
#solve:解线性方程组Ax=b，其中A为一个方阵
#lstsq:计算Ax=b的最小二乘解

#numpy中的随机数生成
#import numpy.random as npr
#seed:随机数生成器种子
#permutation:返回一个序列的随机排序或返回一个随机排序的范围
#x=np.arange(0,6)
#print(npr.permutation(x))     #[0 5 2 3 1 4]
#shuffle：对一个序列就地随机排序
#npr.shuffle(x)
#print(x)                      #[3 0 4 1 2 5]
#rand：产生均匀分布的样本值
#randint：从给定的上下限范围内随机选取整数
#x = npr.randint(0,2,size=100000)    #抛硬币
#print((x>0).sum())         #1的概率     
#randn:产生正态分布（平均值为0，标准差为1）的样本值
# binomial:产生二项分布样本值
# normal:产生正态分布的样本值
# beat:产生Beta分布的样本值
# chisquare:产生卡方分布的样本值
# uniform:产生在[0,1)中的均匀分布的样本值
#print(npr.uniform(size=(2,2))) 

#x = np.arange(0,6).reshape(2,3)
#y = x.flatten()         #拷贝x里面的元素  #[0 1 2 3 4 5]
#x.flatten()[1] = 100         #返回的时拷贝里面的元素修改，x没变
#x.ravel()[1] = 200      #返回的时x的引用，x被修改
#z = x.copy()         #拷贝x
'''
[[  0 200   2]
 [  3   4   5]]
'''
#x = np.arange(0,6)
#print(x.reshape((2,-1)))      #指定行，自动推导
'''
[[0 1 2]
 [3 4 5]]
'''
#合并数组
#x = np.arange(1,7).reshape(2,-1)
#y = np.arange(7,13).reshape(x.shape)
#z1 = np.concatenate([x,y],axis=0)    #垂直合并  等价于  np.vstack((x, y))   等价于  np.r_[x,y]

'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
#z2 = np.concatenate([x,y],axis=1)    #水平合并  等价于  np.hstack((x, y))  等价于  np.c_[x,y]
'''
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
'''
#dstack：按深度堆叠，即增加阶数
#print(np.dstack((x,y)))             #3*2*2的三阶张量
'''
[[[ 1  7]
  [ 2  8]
  [ 3  9]]

 [[ 4 10]
  [ 5 11]
  [ 6 12]]]
'''
#print(np.split(x,2,axis=0))         #按行分割
#print(np.split(x,3,axis=1))         #按列分割

#元素重复操作
#x = np.array([[1,2],[3,4]])
'''
[[1 2]
 [3 4]]
'''
#print(x)
#print(x.repeat(2))            #[1 1 2 2 3 3 4 4]按元素重复
#print(x.repeat(2,axis=0))            #按行重复
'''
[[1 2]
 [1 2]
 [3 4]
 [3 4]]
'''
#print(x.repeat(2,axis=1))            #按列重复
'''
[[1 1 2 2]
 [3 3 4 4]]
'''
#print(np.tile(x,2))                 #tile(x,n)重复n次瓦片
'''
[[1 2 1 2]
 [3 4 3 4]]
'''
#print(np.tile(x,(3,2)))                 #指定从低维到高维依次复制的次数，np.tile(x,(n,m))生成x的行数*n复制m次
'''
[[1 2 1 2]
 [3 4 3 4]
 [1 2 1 2]
 [3 4 3 4]
 [1 2 1 2]
 [3 4 3 4]]
'''

#pandas
#import pandas as pd
#from pandas import Series,DataFrame
#生成一位数组
#x = Series([1,2,3,4])
'''
0    1
1    2
2    3
3    4
'''
#print(x.values)         #[1 2 3 4]
#print(x.index)          #RangeIndex(start=0, stop=4, step=1)
#可以指定index
#跟字典差不多的操作
#x = Series([1,2,3,4],index='a b c d'.split())
#print(x['b'])       #2
#x['e'] = 5
#print(x)
'''
a    1
b    2
c    3
d    4
e    5
'''
#print(x[['a','b']])
'''
a    1
b    2
'''
#print('e' in x)     #True

#使用字典来生成Series
#data = {'a':1, 'b':2, 'c':3, 'd':4}
#x = Series(data)
#print(x)
'''
a    1
b    2
c    3
d    4
'''
#使用字典生成Series,并指定额外的index，不匹配的索引部分数据为NaN。
#exindex = ['a', 'b', 'c', 'e']
#y = Series(data, index = exindex)
#加法：相同行索引的相加，不同行索引数值为NaN
#print(x+y)
'''
a    2.0
b    4.0
c    6.0
d    NaN
e    NaN
'''
#指定Series/索引的名字
#y.name = 'weight of letters'
#y.index.name = 'letter'
#print(y)
'''
letter
a    1.0
b    2.0
c    3.0
e    NaN
Name: weight of letters, dtype: float64
'''
#替换index,不会添加
#y.index = ['a', 'b', 'c', 'f']
#print(y)
'''
a    1.0
b    2.0
c    3.0
f    NaN
Name: weight of letters, dtype: float64
'''

#DataFrame
#构造DataFrame最常用的方式是字典+列表
#使用字典生成DataFrame，key为列名字,index为行名
#data = {'state':['ok', 'ok', 'good', 'bad'],
#        'year':[2000, 2001, 2002, 2003],
#        'pop':[3.7, 3.6, 2.4, 0.9]}
#x = DataFrame(data,index=['one', 'two', 'three', 'four'])
'''
      state  year  pop
one      ok  2000  3.7
two      ok  2001  3.6
three  good  2002  2.4
four    bad  2003  0.9
'''
#print(x['year'])    #也可以使用x.year
#print(x.year)
'''
one      2000
two      2001
three    2002
four     2003
Name: year, dtype: int64
'''
#print(x.year['two'])        #2001
#x['debt'] = 16.5        #添加，修改一列数据
#print(x.T)              #转置
'''
        one   two three  four
state    ok    ok  good   bad
year   2000  2001  2002  2003
pop     3.7   3.6   2.4   0.9
debt   16.5  16.5  16.5  16.5
'''
#指定索引和列的名称
#x.index.name = '序号'
#x.columns.name = '信息' 
#print(x)
'''
信息    state  year  pop  debt
序号
one      ok  2000  3.7  16.5
two      ok  2001  3.6  16.5
three  good  2002  2.4  16.5
four    bad  2003  0.9  16.5
'''

#索引对象
#from pandas import Index
#x = Series(range(3), index = ['a', 'b', 'c'])
#index = x.index
#print(index)        #Index(['a', 'b', 'c'], dtype='object')
#判断列/行索引是否存在
#data = {'pop':[2.4,2.9],'year':[2001,2002]}
#x = pd.DataFrame(data,index=['one','two'])
'''
     pop  year
one  2.4  2001
two  2.9  2002
'''
#print('pop' in x.columns)     #True
#print(2001 in x.values)     #True
#print('one' in x.index)      #True

#基本功能
#reindex函数:对列/行索引重新指定索引（删除/增加：行/列）
#参数：ffill或pad       前向填充（或搬运）值
#bfill或backfill       后向填充（或搬运）值

#重新指定索引及NaN填充值
#x = Series([4, 7, 5], index = ['a', 'b', 'c'])
#y = x.reindex(['a', 'b', 'c', 'd'])       #x中没有的元素会赋值NaN
#z = x.reindex(['a', 'b', 'c', 'd'],fill_value=0)      #x中没有的元素会赋值0
#print(y)
'''
a    4.0
b    7.0
c    5.0
d    NaN
dtype: float64
'''
#print(z)
'''
a    4
b    7
c    5
d    0
dtype: int64
'''
#重新指定索引并指定填充NaN的方法
#x = Series(['blue', 'purple'], index = [0, 2])
#print(x.reindex(range(4)))
'''
0      blue
1       NaN
2    purple
3       NaN
dtype: object
'''
#print(x.reindex(range(4),method='ffill')) #前向填充   原不存在的元素与前一个相等
'''
0      blue
1      blue
2    purple
3    purple
dtype: object
'''
#对DataFrame重新指定行/列索引
#import numpy
#x = DataFrame(numpy.arange(9).reshape(3, 3),    #使用numpy创建一个3*3的方阵
#                  index = ['a', 'c', 'd'],
#                  columns = ['A', 'B', 'C'])
'''
   A  B  C
a  0  1  2
c  3  4  5
d  6  7  8
'''
#x =  x.reindex(['a', 'b', 'c', 'd'],method = 'bfill') #后向填充 原不存在的元素与后一个相等
'''
   A  B  C
a  0  1  2
b  3  4  5
c  3  4  5
d  6  7  8
'''
#重新指定column
#states = pd.Index(list(x.columns)+['D'])       emmmmmmmm
#states = ['A', 'B', 'C','D']
#x =  x.reindex(columns = states,fill_value = 0)
'''
   A  B  C  D
a  0  1  2  0
b  3  4  5  0
c  3  4  5  0
d  6  7  8  0
'''
#drop函数:删除（丢弃）整一行/列的元素

#Series根据行索引删除行
#x = Series(range(4), index = ['a', 'b', 'c','d']).drop('c')       #创建，删除c
'''
a    0
b    1
d    3
dtype: int64
'''
#print(x.drop(['a','b']))            #删除a,b
'''
d    3
dtype: int64
'''
#x = DataFrame(np.arange(9).reshape(3, 3),    #使用numpy创建一个3*3的方阵
#                  index = ['a', 'c', 'd'],
#                  columns = ['A', 'B', 'C'])
#print(x.drop(['A','B'],axis=1))     #列维度上，删除A,B两列
'''
   C
a  2
c  5
d  8
'''
#print(x.drop(['a','c']))     #行维度上，删除a,c两行，axis=0，也是定义行维度
'''
   A  B  C
d  6  7  8
'''

#索引、选取和过滤
#print(x[['A','B']])           #打印A,B列
'''
   A  B
a  0  1
c  3  4
d  6  7
'''
#print(x[:2])            #前两行
'''pandas 0.20.0后面移除了ix，可以改用loc查询'''
#print(x.ix[:2,['A','B']])     #指定行和列索引
'''
   A  B
a  0  1
b  4  5
'''
#print(x.loc['a'])       #索引行
#print(x.loc[0])       #loc索引的是name,没有一个name是叫0，所以会报错
'''
A    0
B    1
C    2
Name: a, dtype: int32
'''
#print(x.loc[['a','c']]) #索引多行
'''
   A  B  C
a  0  1  2
c  3  4  5
'''
#print(x.loc[:,['A','B']])     #索引多列
'''
   A  B
a  0  1
c  3  4
d  6  7
'''
#print(x.loc[['a','c'],['A','B']])   #索引某些行，某些列
'''
   A  B
a  0  1
c  3  4
'''

#iloc:是基于position进行索引的！即索引下标
#print(x.iloc[0])        #等价于   x.loc['a']
'''
A    0
B    1
C    2
Name: a, dtype: int32
'''
#print(x.iloc[1:])       #索引多行，从1到最后
'''
   A  B  C
c  3  4  5
d  6  7  8
'''
#print(x.iloc[1:,:2])    #索引某些行，某些列
'''
   A  B
c  3  4
d  6  7
'''

#print(x[x.A>2])         #条件索引行
'''
   A  B  C
c  3  4  5
d  6  7  8
'''
#print(x.loc[:,x.loc['a']<2])  #条件索引列
'''
   A  B
a  0  1
c  3  4
d  6  7
'''

#x = DataFrame(np.arange(9.).reshape((3, 3)),columns = ['A','B','C'],index = ['a', 'b', 'c'])
#y = DataFrame(np.arange(12).reshape((4, 3)),columns = ['A','B','C'],index = ['a', 'b', 'c', 'd'])
#DataFrame算术:不重叠部分为NaN,重叠部分元素运算 +、-、*、/
#print(x+y)
'''
      A     B     C
a   0.0   2.0   4.0
b   6.0   8.0  10.0
c  12.0  14.0  16.0
d   NaN   NaN   NaN
'''
#print(x-y)
'''
     A    B    C
a  0.0  0.0  0.0
b  0.0  0.0  0.0
c  0.0  0.0  0.0
d  NaN  NaN  NaN
'''
#print(x*y)
'''
      A     B     C
a   0.0   1.0   4.0
b   9.0  16.0  25.0
c  36.0  49.0  64.0
d   NaN   NaN   NaN
'''
#print(x/y)
'''
     A    B    C
a  NaN  1.0  1.0
b  1.0  1.0  1.0
c  1.0  1.0  1.0
d  NaN  NaN  NaN
'''
#fill_value:对x/y的不重叠部分填充，不是对结果NaN填充 add、sub、mul、truediv
#print(x.add(y,fill_value=0))  #x不变
'''
      A     B     C
a   0.0   2.0   4.0
b   6.0   8.0  10.0
c  12.0  14.0  16.0
d   9.0  10.0  11.0
'''
#print(x.sub(y,fill_value=0))
'''
     A     B     C
a  0.0   0.0   0.0
b  0.0   0.0   0.0
c  0.0   0.0   0.0
d -9.0 -10.0 -11.0
'''
#DataFrame与Series运算：每行/列进行运算
#series = x.loc['a']
#print(x-series)
'''
     A    B    C
a  0.0  0.0  0.0
b  3.0  3.0  3.0
c  6.0  6.0  6.0
'''
#series = x.A
#print(x.sub(series,axis=0))   #按列运算。
'''
     A    B    C
a  0.0  1.0  2.0
b  0.0  1.0  2.0
c  0.0  1.0  2.0
'''
#print((x.T-series).T)
#x['A']['a'] =10
'''
      A    B    C
a  10.0  1.0  2.0
b   3.0  4.0  5.0
c   6.0  7.0  8.0
'''
#print(x.max())    #计算每一列的最大值
'''
A    10.0
B     7.0
C     8.0
dtype: float64
'''
#print(x.max(axis=1)) #计算每一行的最大值
#匿名函数和apply(function)
#f = lambda x:x.max()-x.min()
#print(x.apply(f))    #每一列的最大值减最小值
'''
A    7.0
B    6.0
C    6.0
dtype: float64
'''
#print(x.apply(f,axis=1))    #每一行的最大值减最小值
#f = lambda x: Series([x.min(), x.max()], index = ['min', 'max'])
#print(x.apply(f,axis=1))    #返回一个Series，每一行的最大值减最小值
'''
   min   max
a  1.0  10.0
b  3.0   5.0
c  6.0   8.0
'''
#'applymap和map：作用到每一个元素'
#f = lambda x: '%.2f' %x
#print(x.applymap(f))    #针对DataFrame
'''
       A     B     C
a  10.00  1.00  2.00
b   3.00  4.00  5.00
c   6.00  7.00  8.00
'''
#print(x['A'].map(f))    # 针对Series
'''
a    10.00
b     3.00
c     6.00
Name: A, dtype: object
'''

#排序：sort_index和sort_values函数
#x = Series(range(4), index = ['b', 'a', 'c', 'd'])
#print(x.sort_index())  #对index排序
'''
a    1
b    0
c    2
d    3
'''
#print(x.sort_values())  #对value排序
#x = DataFrame(np.arange(8).reshape((2, 4)),index = ['b', 'a'],columns = list('ABDC'))
'''
   A  B  D  C
b  0  1  2  3
a  4  5  6  7
'''
#print(x.sort_index())      #对行索引排序
#print(x.sort_index(axis=1,ascending=False))      #对列索引排序,ascending设置降序排序
'''
   D  C  B  A
b  2  3  1  0
a  6  7  5  4
'''
#DataFrame按列的值排序
#x = DataFrame(dict(zip(list('CAB'),[np.random.randint(-10,10,5) for i in range(3)])))
#x = DataFrame({'b':[4, 7, -3, 2], 'a':[0, 1, 0, 1]})
'''
   b  a
0  4  0
1  7  1
2 -3  0
3  2  1
'''
#print(x.sort_values(by='b',ascending=False)) #根据b列进行降序排序
'''
   b  a
1  7  1
0  4  0
3  2  1
2 -3  0
'''
#print(x.sort_values(by=['a','b'],ascending=(True,False))) #先对a列进行升序再对b列进行降序
'''
   b  a
0  4  0
2 -3  0
1  7  1
3  2  1
'''
#x = Series([4, 2, 0, 4],index = ['a','b','c','d'])
# 以值从小到大来赋排名值：c:0(1) b:2(2) a:4(3) d:4(4)
#rank函数的默认处理是当出现重复值的情况下，默认取他们排名次序值的平均值。
#故以下a,d的排名分别是3、4取均值为3.5
#print(x.rank())
'''
a    3.5
b    2.0
c    1.0x
d    3.5
dtype: float64
'''
#print(x.rank(method = 'first')) # 按出现顺序排名，不求平均值。
'''
a    3.0
b    2.0
c    1.0
d    4.0
dtype: float64
'''
#print(x.rank(ascending=False, method='max'))
#ascending=False逆序排名a:4(1) d:4(2) b:2(3) c:0(4)
#method='max' 相同排名取最大的排名，故a、d取2
'''
a    2.0
b    3.0
c    4.0
d    2.0
dtype: float64
'''

#frame = DataFrame({'b':[4.3, 7, -3, 2],'a':[0, 1, 0, 1],'c':[-2, 5, 8, -2.5]})
#print(frame)
'''
     b  a    c
0  4.3  0 -2.0
1  7.0  1  5.0
2 -3.0  0  8.0
3  2.0  1 -2.5
'''
#print(frame.rank())     #按列进行排名，默认升序
'''
     b    a    c
0  3.0  1.5  2.0
1  4.0  3.5  3.0
2  1.0  1.5  4.0
3  2.0  3.5  1.0
'''
#print(frame.rank(axis=1))  #按行进行排名，默认升序
'''
     b    a    c
0  3.0  2.0  1.0
1  3.0  1.0  2.0
2  1.0  2.0  3.0
3  3.0  2.0  1.0
'''

#重复索引:进行两次索引
#x = Series([0,1,2,3,4], index = ['a', 'a', 'b', 'b', 'c'])
'''
a    0
a    1
b    2
b    3
c    4
dtype: int64
'''
#print(x.index.is_unique)      #索引值是否唯一，True唯一，False有重复索引值
#print(x['a'])
'''
a    0
a    1
'''

#idxmax、idxmin   获取最大最小值的索引
#print(frame.idxmax())
'''
b    1
a    1
c    2
dtype: int64
'''
#print(frame.describe())    #对DataFrame每列计算汇总统计
'''
              b        a         c
count  4.000000  4.00000  4.000000
mean   2.575000  0.50000  2.125000
std    4.241364  0.57735  5.202163
min   -3.000000  0.00000 -2.500000
25%    0.750000  0.00000 -2.125000
50%    3.150000  0.50000  1.500000
75%    4.975000  1.00000  5.750000
max    7.000000  1.00000  8.000000
'''

#print(frame.isin([0,1,2]))    #判断元素是否存在
'''
       b     a      c
0  False  True  False
1  False  True  False
2  False  True  False
3   True  True  False
'''
#print(frame)
'''
     b  a    c
0  4.3  0 -2.0
1  7.0  1  5.0
2 -3.0  0  8.0
3  2.0  1 -2.5
'''
#print(frame.apply(pd.value_counts).fillna(0))   #统计每列数字出现的次数
#如果只有一条它会降维，变成Series类型，此时统计的是数据的str的长度
'''
        b    a    c
-3.0  1.0  0.0  0.0
-2.5  0.0  0.0  1.0
-2.0  0.0  0.0  1.0
 0.0  0.0  2.0  0.0
 1.0  0.0  2.0  0.0
 2.0  1.0  0.0  0.0
 4.3  1.0  0.0  0.0
 5.0  0.0  0.0  1.0
 7.0  1.0  0.0  0.0
 8.0  0.0  0.0  1.0
 '''
#print(frame.apply(pd.value_counts,axis=1).fillna(0))  #统计每行各个数字出现的次数
'''
   -3.0  -2.5  -2.0   0.0   1.0   2.0   4.3   5.0   7.0   8.0
0   0.0   0.0   1.0   1.0   0.0   0.0   1.0   0.0   0.0   0.0
1   0.0   0.0   0.0   0.0   1.0   0.0   0.0   1.0   1.0   0.0
2   1.0   0.0   0.0   1.0   0.0   0.0   0.0   0.0   0.0   1.0
3   0.0   1.0   0.0   0.0   1.0   1.0   0.0   0.0   0.0   0.0
'''

#处理缺失数据
#NaN（Not a Number）表示浮点数和非浮点数组中的缺失数据，None也被当作NA处理。
#dropna 函数：DatFrame默认丢弃任何含有缺失值的行。how参数控制行为，axis参数选择轴，thresh参数控制NaN数量的要求。
#fillna函数： inplace参数决定返回新对象还是就地修改
#isnull：返回一个含有布尔值的对象，表示哪些值是缺失值
#notnull：isnull的否定式
#x=Series(['a', 'b', np.nan, 'd'])
'''
0      a
1      b
2    NaN
3      d
'''
#print(x.isnull())
'''
0    False
1    False
2     True
3    False
dtype: bool
'''
#print(x[x.notnull()])      #查看未缺失的数据等价于  x.dropna()
#print(x.dropna())
'''
0    a
1    b
3    d
'''
#x[0]=None
#print(x.isnull())    #None也被当作是缺失数据
'''
0     True
1    False
2     True
3    False
dtype: bool
'''
#frame = DataFrame([[1, 6, 3], [1, np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6, 3]])
'''
     0    1    2
0  1.0  6.0  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.0  3.0
'''
#print(frame.dropna())   #默认只要某行有NA就全部删除
'''
     0    1    2
0  1.0  6.0  3.0
'''
#print(frame.dropna(how='all'))   #某行全部为NA才删除
'''
     0    1    2
0  1.0  6.0  3.0
1  1.0  NaN  NaN
3  NaN  6.0  3.0
'''
#how='all'     全部为NA才删除
#thresh = n    至少要有n个非NA元素

#frame = DataFrame(np.arange(9).reshape(3, 3))
#frame[0][:2]=np.nan
#frame.iloc[2]=np.nan
'''
    0    1    2
0 NaN  1.0  2.0
1 NaN  4.0  5.0
2 NaN  NaN  NaN
'''
#frame.fillna(0)      #将NA改为0，返回表类型，非就地修改即不会改变原数据
#print(frame)
'''
    0    1    2
0 NaN  1.0  2.0
1 NaN  4.0  5.0
2 NaN  NaN  NaN
'''
#frame.fillna(1,inplace=True)  #就地修改，会改变原数据
#print(frame)
'''
     0    1    2
0  1.0  1.0  2.0
1  1.0  4.0  5.0
2  1.0  1.0  1.0
'''
#frame[0][0]=1
#print(frame)
'''
     0    1    2
0  1.0  1.0  2.0
1  NaN  4.0  5.0
2  NaN  NaN  NaN
'''
#print(frame.fillna(method = 'ffill'))
'''
     0    1    2
0  1.0  1.0  2.0
1  1.0  4.0  5.0
2  1.0  4.0  5.0
'''
#print(frame.fillna(method = 'ffill',limit=1))   #只可填充一步
'''
     0    1    2
0  1.0  1.0  2.0
1  1.0  4.0  5.0
2  NaN  4.0  5.0
'''
#print(frame.fillna(frame.mean()))      #填充没一列的平均值
'''
     0    1    2
0  1.0  1.0  2.0
1  1.0  4.0  5.0
2  1.0  2.5  3.5
'''

#多层次化索引
#对Series和DataFrame进行多层次的索引MultiIndex，通过stack与unstack进行Series和DataFrame的变换。
#from pandas import MultiIndex
#x = Series(np.arange(8),index = [['a', 'a', 'b', 'b',  'c', 'c', 'd','d'],[1, 2, 1, 2, 1, 2, 1,2]])
'''
a  1    0
   2    1
b  1    2
   2    3
c  1    4
   2    5
d  1    6
   2    7
'''

#print(x.index)
'''
MultiIndex([('a', 1),
            ('a', 2),
            ('b', 1),
            ('b', 2),
            ('c', 1),
            ('c', 2),
            ('d', 1),
            ('d', 2)],
           )
'''
#print(x.b)
'''
1    2
2    3
dtype: int32
'''
#print(x['b':'d'])
'''
b  1    2
   2    3
c  1    4
   2    5
d  1    6
   2    7
dtype: int32
'''
#print(x[:3])      #使用数组的索引，不区分标签
'''
a  1    0
   2    1
b  1    2
dtype: int32
'''
#print(x.unstack())   #将Series转换为DataFrame   .stack()将DataFrame转换回Series
'''
   1  2
a  0  1
b  2  3
c  4  5
d  6  7
'''

#DataFrame的多层次化索引
#frame = DataFrame(np.arange(12).reshape((4, 3)),index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],columns = [['A', 'A', 'B'], ['A1', 'A2', 'B1']])
#print(frame)
'''
     A       B
    A1  A2  B1
a 1  0   1   2
  2  3   4   5
b 1  6   7   8
  2  9  10  11
'''
#print(frame.index)
'''
MultiIndex([('a', 1),
            ('a', 2),
            ('b', 1),
            ('b', 2)],
           )
'''
#print(frame.columns)
'''
MultiIndex([('A', 'A1'),
            ('A', 'A2'),
            ('B', 'B1')],
           )
'''
#print(frame['A'])
'''
     A1  A2
a 1   0   1
  2   3   4
b 1   6   7
  2   9  10
'''
#print(frame['A','A1'])
'''
a  1    0
   2    3
b  1    6
   2    9
Name: (A, A1), dtype: int32
'''
#print(frame[[('A','A1'),('B','B1')]])
'''
     A   B
    A1  B1
a 1  0   2
  2  3   5
b 1  6   8
  2  9  11
'''
#print(frame.iloc[0])
'''
A  A1    0
   A2    1
B  B1    2
'''
#print(frame.iloc[1:,[0,2]])
'''
     A   B
    A1  B1
a 2  3   5
b 1  6   8
  2  9  11
'''
#print(frame.iloc[1,1])     #4
#frame.index.names = ['key1', 'key2']
#print(frame)
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
     2     3   4   5
b    1     6   7   8
     2     9  10  11
'''
#print(frame.swaplevel('key1','key2'))  #交互索引层
'''
           A       B
          A1  A2  B1
key2 key1
1    a     0   1   2
2    a     3   4   5
1    b     6   7   8
2    b     9  10  11
'''
#print(frame.swaplevel('key1','key2').swaplevel(0,1))  #通过下标交互
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
     2     3   4   5
b    1     6   7   8
     2     9  10  11
'''
#对索引层排序
#print(dir(frame))
#print(frame.sort_index(level=1))     #对key2排序
#print(frame.sort_index(level='key2'))     #对key2排序
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
b    1     6   7   8
a    2     3   4   5
b    2     9  10  11
'''
#print(frame.sort_values(by=('A', 'A1'),axis=0,ascending=False))     #对key2排序
'''
           A       B
          A1  A2  B1
key1 key2
b    2     9  10  11
     1     6   7   8
a    2     3   4   5
     1     0   1   2
'''
#print(frame.sum(level = 'key2'))    #对key2求和
'''
       A       B
      A1  A2  B1
key2
1      6   8  10
2     12  14  16
'''
#将列索引转化行层次索引
#frame = DataFrame({'a':range(7),'b':range(7, 0, -1),'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'],'d':[0, 1, 2, 0, 1, 2, 3]})
#print(frame)
'''
   a  b    c  d
0  0  7  one  0
1  1  6  one  1
2  2  5  one  2
3  3  4  two  0
4  4  3  two  1
5  5  2  two  2
6  6  1  two  3
'''
#frame1 = frame.set_index(['c','d'])    #把c/d列索引变成行索引,drop = False不移除，即保留c/d列
#print(frame1)      
'''
       a  b
c   d
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1
'''
#print(frame1.index)
'''
MultiIndex([('one', 0),
            ('one', 1),
            ('one', 2),
            ('two', 0),
            ('two', 1),
            ('two', 2),
            ('two', 3)],
           names=['c', 'd'])
'''
#print(frame1.reset_index())         #恢复
'''
     c  d  a  b
0  one  0  0  7
1  one  1  1  6
2  one  2  2  5
3  two  0  3  4
4  two  1  4  3
5  two  2  5  2
6  two  3  6  1
'''
#ser = Series(np.arange(3))
#print(ser[-1])         #KeyError: -1
#ser.index=['a','b','c']
#print(ser[-1])         #2


###增加行列
#import numpy as np
#from pandas import DataFrame
#import pandas as pd
#frame = DataFrame(np.array([np.random.randint(-9,9) for i in range(6)]).reshape(2,3),columns=list('ABC'),index=[-1,1])
#增加列
#frame['D'] = [np.random.randint(-9,9) for i in range(frame.shape[0])]
#增加行
#利用loc，只能在最后添加
#frame.loc[0] = [np.random.randint(-9,9) for i in range(frame.shape[1])]
'''
    A  B  C  D
-1 -4  1  7 -5
 1 -4 -4 -7 -7
 0 -9 -7  8  3
'''
#frame.loc[frame.index.tolist()[-1]+1] = [np.random.randint(-9,9) for i in range(frame.shape[1])]
#append() 非就地添加
#frame = frame.append(DataFrame(dict(zip(frame.columns.tolist(),[np.random.randint(-9,9) for i in range(frame.shape[1])])),index=[4],columns=frame.columns.tolist()+list('E')))
'''
    A  B  C  D    E
-1 -5 -5 -9 -9  NaN
 1  4 -1 -9 -6  NaN
 4  0 -9 -4 -5  NaN
'''

#指定位置添加可能只能重组？reindex
#在B后面插入一列G
#frame = frame.reindex(list('ABGCDE'),axis=1)
#frame_columns = frame.columns.tolist()
#frame = frame.reindex(frame_columns[:frame_columns.index('B')+1]+['G']+frame_columns[frame_columns.index('B')+1:],axis=1)
#frame['G'] = [np.random.randint(-9,9) for i in range(frame.shape[0])]
#同理
#frame_index = frame.index.tolist()
#frame_index.insert(frame_index.index(-1)+1,0)
#frame = frame.reindex(frame_index)
#frame.loc[0] = [np.random.randint(-9,9) for i in range(frame.shape[1])]
'''
      A    B    G    C    D
-1  6.0 -1.0 -1.0  2.0  3.0
 0 -6.0 -6.0 -5.0 -8.0 -1.0
 1 -7.0  7.0 -6.0 -5.0  8.0
'''
#print(frame)
#pandas replace
# replace的基本结构是：df.replace(to_replace, value) 前面是需要替换的值，后面是替换后的值。

###按电影名称和上映时间去重
#data.drop_duplicates(subset=['movie_title','title_year'],keep='first',inplace=True)
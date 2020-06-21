import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#Series索引
#ser = Series(np.arange(10,15),dtype=np.int8)
'''
0    10
1    11
2    12
3    13
4    14
dtype: int8
'''
#print(ser.index)    #RangeIndex(start=0, stop=5, step=1)
#ser[]索引
#print(ser[1])       #11
#print(ser[-1])       #KeyError: -1，有歧义，没有找到key是-1的
#print(ser.iloc[-1])       #14  可以通过指定下标索引去索引
#print(ser[1:3])
'''
1    11
2    12
'''
#print(ser[[1,3]])
'''
1    11
3    13
dtype: int8
'''
#print(ser[ser>12])
'''
3    13
4    14
dtype: int8
'''
#ser.index=list(range(-1,4))
#print(ser)
'''
-1    10
 0    11
 1    12
 2    13
 3    14
 dtype: int8
'''
#print(ser.index)    #Int64Index([-1, 0, 1, 2, 3], dtype='int64')
#当index的dtype为整型时，ser[n]是寻找key为n的元素
#print(ser[0])       #11
#print(ser[-1])       #10    index被定义，可以找到key为-1的元素
#ser.index=pd.Index(np.arange(-1,4),dtype=np.str)            #不过应该不会有人这样定义吧
#print(ser.index)        #Index(['-1', '0', '1', '2', '3'], dtype='object')
#print(ser)
'''
-1    10
0     11
1     12
2     13
3     14
dtype: int8
'''
#当index的dtype为object时，ser[n]是寻找下标为n的元素
#print(ser[0])       #10
#print(ser[-1])       #14    寻找倒数第二个
#print(ser['0'])       #11     通过key查找
#print(ser['-1'])       #10     通过key查找
#print(ser['0':'2'])
'''
0    11
1    12
2    13
dtype: int8
'''
#print(ser[['-1','1','3']])
'''
-1    10
1     12
3     14
dtype: int8
'''
#print(ser[[-1,1,3]])
'''
-1    10
1     12
3     14
dtype: int8
'''
#loc通过key索引、iloc通过下标索引
#print(ser.loc['0'])     #11
#print(ser.loc['-1'])     #10
#print(ser.iloc[0])      #10
#print(ser.iloc[-1])     #14
#print(ser.loc[['-1','1','3']])
'''
-1    10
1     12
3     14
dtype: int8
'''
#索引NA
#ser[[0,2,3]]=np.nan
#print(ser)
'''
-1     NaN
0     11.0
1      NaN
2      NaN
3     14.0
'''
#print(ser.isnull())
'''
-1     True
0     False
1      True
2      True
3     False
dtype: bool
'''
#print(ser[ser.isnull()].index)  #Index(['-1', '1', '2'], dtype='object')    NA的key
#print(ser.notnull())            #与isnull相反
'''
-1    False
0      True
1     False
2     False
3      True
dtype: bool
'''        
#print(ser.drop(['0','1']))            #移除'0','1'
'''
-1     NaN
2      NaN
3     14.0
dtype: float64
'''
#print(ser.dropna())                 #移除NA
'''
0    11.0
3    14.0
dtype: float64
'''
#print(ser.fillna(0))            #将NA改为n，参数：inplace=True时就地修改
'''
-1     0.0
0     11.0
1      0.0
2      0.0
3     14.0
dtype: float64
'''
#print(ser.sort_index(ascending=False))          #根据index排序，参数ascending=False，降序，默认为True，即升序
'''
3     14.0
2      NaN
1      NaN
0     11.0
-1     NaN
dtype: float64
'''
#print(ser.sort_values())                    #根据values排序
'''
0     11.0
3     14.0
-1     NaN
1      NaN
2      NaN
dtype: float64
'''

##########################################
#DataFrame
try:
    f = pd.read_csv('ceui2.csv',index_col=0)
except:
    x = DataFrame(dict(zip(list('CAB'),[np.random.randint(-10,10,5) for i in range(3)])),index=range(-1,4))
    x.to_csv('ceui2.csv')
    frame = x
else:
    frame = DataFrame(f)
#print(frame)
'''
   C  A  B
-1 -1 -8 -2
 0  8  9 -9
 1  3  2  1
 2 -4 -7  0
 3 -4  0 -1
'''
#frame[s]   对s列的索引
#print(frame[['C','B']])
'''
    C  B
-1 -1 -2
 0  8 -9
 1  3  1
 2 -4  0
 3 -4 -1
'''
#print(frame[0])     #KeyError: 0

#print(frame['C'][2])    #-4
#print(frame[['C','B']][2])    #KeyError: 2
#loc[s]      用key索引行
#print(frame.loc[0:3,['C','A']])
'''
   C  A
0  8  9
1  3  2
2 -4 -7
3 -4  0
'''
#loc[:,s]  #索引列，即索引所有行的s列
#print(frame.loc[:,['C','A']])
'''
    C  A
-1 -1 -8
 0  8  9
 1  3  2
 2 -4 -7
 3 -4  0
'''
#iloc[n]    与loc一样，不过通过下标索引
#print(frame.iloc[0])
'''
C   -1
A   -8
B   -2
Name: -1, dtype: int64
'''
#print(frame.iloc[0::2,[0,2]])
'''
    C  B
-1 -1 -2
 1  3  1
 3 -4 -1
'''
#DataFrame的多层次化索引
#增加行列
frame['D'] = [np.random.randint(-9,9) for i in range(frame.shape[0])]
frame['E'] = [np.random.randint(-9,9) for i in range(frame.shape[0])] 
#frame = frame.append(DataFrame(dict(zip(frame.columns.tolist(),[np.random.randint(-9,9) for i in range(0,frame.shape[1])])),index=[4]))
frame.loc[frame.index.tolist()[-1]+1] = [np.random.randint(-9,9) for i in range(0,frame.shape[0])] 
'''
    C  A  B  D  E
-1 -1 -8 -2 -7 -5
 0  8  9 -9 -2 -3
 1  3  2  1 -1  1
 2 -4 -7  0  8  2
 3 -4  0 -1 -3  8
 4 -9 -8  4 -1 -3
'''
frame = frame.set_index(['C','D']).reset_index()
print(frame)

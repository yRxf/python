#to_numeric()转换为数值类型
import pandas as pd
df = pd.DataFrame([[1,2,3,4,5,16],['1','2','3','4','5','F']],index=['data1','data2'])
#print(df)
'''
       0  1  2  3  4   5
data1  1  2  3  4  5  16
data2  1  2  3  4  5   F
'''
#print(df.apply(lambda x:x*10))  #所有数据扩大10倍
'''`
                0           1           2           3           4           5     
data1          10          20          30          40          50         160     
data2  1111111111  2222222222  3333333333  4444444444  5555555555  FFFFFFFFFF
'''
#print(df.dtypes)        #都是object类型
#都是 object 类型，Pandas 并没有承认这些数据是数值类型
#所以，开始数据分析之前，做数据清洗还是有必要的。
#Pandas 提供了转换数值类型的方法，to_numeric()转换为数值类型
#df.loc['data2'] = pd.to_numeric(df.loc['data2'])
#ValueError: Unable to parse string "F" at position 5,不能将字符串 “F”转换为数值类型
#一个可选的参数 errors，传入 errors='coerce' Pandas 遇到不能转换的数据就会赋值为 NaN（Not a Number）
df.loc['data2'] = pd.to_numeric(df.loc['data2'],errors='coerce')
'''
       0  1  2  3  4    5
data1  1  2  3  4  5   16
data2  1  2  3  4  5  NaN
'''
df = df.apply(lambda x: x*10)
print(df)
print(df.dtypes)
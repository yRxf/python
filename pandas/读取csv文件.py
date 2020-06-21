import pandas as pd
import numpy as np
#DataFrame
'''
try:
    f = pd.read_csv('ceui.csv',index_col=0)
except:
    x = pd.DataFrame(dict(zip(list('CAB'),[np.random.randint(-10,10,5) for i in range(3)])),index=range(-1,4))
    x.to_csv('ceui.csv')
    frame = x
else:
    frame = pd.DataFrame(f)
'''
#1.read_csv是以逗号分隔，将其读入一个DataFrame：
#file_name = 'ceui.csv'
#df1 = pd.read_csv(file_name)
#print(df1)
'''
   Unnamed: 0  C  A  B
0          -1 -1 -8 -2
1           0  8  9 -9
2           1  3  2  1
3           2 -4 -7  0
4           3 -4  0 -1
'''
#3.如果没有列名，可以自动获取或者自定义列名
#df2 = pd.read_csv(file_name,header=None)
#print(df2)
'''
     0   1   2   3
0  NaN   C   A   B
1 -1.0  -1  -8  -2
2  0.0   8   9  -9
3  1.0   3   2   1
4  2.0  -4  -7   0
5  3.0  -4   0  -1
'''
#index_col=n将第n列作为行索引，也可跟key
#df3 = pd.read_csv(file_name,index_col='B')  #将B列作为行索引
#print(df3)
'''
    Unnamed: 0  C  A
B
-2          -1 -1 -8
-9           0  8  9
 1           1  3  2
 0           2 -4 -7
-1           3 -4  0
'''
#df4 = pd.read_csv(file_name,index_col='Unnamed: 0')
#df4 = pd.read_csv(file_name,index_col=0)
#print(df4)
'''
    C  A  B
-1 -1 -8 -2
 0  8  9 -9
 1  3  2  1
 2 -4 -7  0
 3 -4  0 -1
'''
#names，设置列索引
#names = list('abcde')
#df5 = pd.read_csv(file_name,names=names)
#print(df5)
'''
     a   b   c   d   e
0  NaN   C   A   B NaN
1 -1.0  -1  -8  -2 NaN
2  0.0   8   9  -9 NaN
3  1.0   3   2   1 NaN
4  2.0  -4  -7   0 NaN
5  3.0  -4   0  -1 NaN
'''
#df6 = pd.read_csv(file_name,names=names,index_col='c')
#print(df6)
'''
      a   b   d   e
c
A   NaN   C   B NaN
-8 -1.0  -1  -2 NaN
9   0.0   8  -9 NaN
2   1.0   3   1 NaN
-7  2.0  -4   0 NaN
0   3.0  -4  -1 NaN
'''

#read_table读取，需要指定分隔符
#df7 = pd.read_table(file_name,sep=',',index_col=0)
#print(df7)
'''
    C  A  B
-1 -1 -8 -2
 0  8  9 -9
 1  3  2  1
 2 -4 -7  0
 3 -4  0 -1
'''
#将df7保存到ceui2.txt，\t分隔
#df7.to_csv('ceui2.txt',sep='\t')
#读取ceui2.txt
#df8 = pd.read_table('ceui2.txt',sep='\t',index_col=0)
#print(df8)
#index=False  不将行索引保存，  header=None去除列名
#df7.to_csv('ceui3.txt',sep='\t',index=False,header=None)
'''
-1	-8	-2
8	9	-9
3	2	1
-4	-7	0
-4	0	-1
'''
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'))
'''
   C  A  B
0 -1 -8 -2
1  8  9 -9
2  3  2  1
3 -4 -7  0
4 -4  0 -1
'''
#df8.index=range(-1,4)       #重新设置行名
'''
    C  A  B
-1 -1 -8 -2
0   8  9 -9
1   3  2  1
2  -4 -7  0
3  -4  0 -1
'''
#print(df8)

###参数：
#sep或delimiter:  用于对行中的各个字段进行拆分，字符序列或正则表达式
#header 作为列名的行号，默认第一行，如果不用应设为None
#index_col  用作行索引的列编号或列名
#names:设置列名
#skiprows:用于需要忽略的行数，数据，从0开始
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),skiprows=[0,2])
'''
   C  A  B
0  8  9 -9
1 -4 -7  0
2 -4  0 -1
'''
#skipfooter:用于需要忽略的行数，数据，从末尾开始，n之后的都会忽略
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),skipfooter=2)
'''
   C  A  B
0 -1 -8 -2
1  8  9 -9
2  3  2  1
'''
#nrows：需要读取的行数
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),nrows=2)
'''
   C  A  B
0 -1 -8 -2
1  8  9 -9
'''
#usecols : array-like, default None 读取指定的列
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),usecols=[2,1])
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),usecols=[2,1],nrows=2)
'''
   A  B
0 -8 -2
1  9 -9
'''
#na_values：将对应的值设为NAN
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),nrows=2,na_values=[-1,8,9])
'''
    C    A  B
0 NaN -8.0 -2
1 NaN  NaN -9
'''
'''
-1	-8	-2
8	9	-9
3	2	1
-4	-7	0
-4	0	-1

'''
#df8 = pd.read_table('ceui3.txt',sep='\t',names=list('CAB'),na_values={'C':['-1','-4'],2:'0'})
#na_values={'C':['-1','-4'],2:'0'}
#指定C列里面的-1和-4设为NaN,第3列里面的0设为NaN(下标由0开始)
'''
     C  A    B
0  NaN -8 -2.0
1  8.0  9 -9.0
2  3.0  2  1.0
3  NaN -7  NaN
4  NaN  0 -1.0
'''
#skipinitialspace:忽略分隔符后的空白（默认为False，即不忽略）.
#prefix :str, default None,在没有列标题时，给列添加前缀。例如：添加‘X’ 成为 X0, X1, ...
#df8 = pd.read_table('ceui3.txt',sep='\t',header=None,nrows=2,prefix='X')
'''
   X0  X1  X2
0  -1  -8  -2
1   8   9  -9
'''
#mangle_dupe_cols,boolean, default True  重复的列，将‘X’...’X’表示为‘X.0’...’X.N’。如果设定为false则会将所有重名列覆盖。
#engine : {‘c’, ‘python’}, optional  使用的分析引擎。可以选择C或者是python。C引擎快但是Python引擎功能更加完备。
#na_filter :boolean, default True  是否检查丢失值（空字符串或者是空值）。对于大文件来说数据集中没有空值，设定na_filter=False可以提升读取速度。
#df8 = pd.read_table('ceui3.txt',sep='\t',header=None,nrows=2,prefix='X',na_filter=False)
#verbose : boolean, default False  是否打印各种解析器的输出信息，例如：“非数值列中缺失值的数量”等。
#skip_blank_lines : boolean, default True  如果为True，则跳过空行；否则记为NaN。
'''
parse_dates : boolean or list of ints or names or list of lists or dict, default False
  boolean. True -> 解析索引
  list of ints or names. e.g. If [1, 2, 3] -> 解析1,2,3列的值作为独立的日期列；
  list of lists. e.g. If [[1, 3]] -> 合并1,3列作为一个日期列使用
  dict, e.g. {‘foo’ : [1, 3]} -> 将1,3列合并，并给合并后的列起名为"foo"

infer_datetime_format : boolean, default False
如果设定为True并且parse_dates 可用，那么pandas将尝试转换为日期类型，如果可以转换，转换方法并解析。在某些情况下会快5~10倍。
 
keep_date_col : boolean, default False
如果连接多列解析日期，则保持参与连接的列。默认为False。
 
date_parser : function, default None
用于解析日期的函数，默认使用dateutil.parser.parser来做转换。Pandas尝试使用三种不同的方式解析，如果遇到问题则使用下一种方式。
1.使用一个或者多个arrays（由parse_dates指定）作为参数；
2.连接指定多列字符串作为一个列作为参数；
3.每行调用一次date_parser函数来解析一个或者多个字符串（由parse_dates指定）作为参数。
 
dayfirst : boolean, default False
DD/MM格式的日期类型
'''
#iterator : boolean, default False  返回一个TextFileReader 对象，以便逐块处理文件。
#chunksize : int, default None  设置文件块的大小，用于分块处理文件
#df8 = pd.read_table('ceui3.txt',sep='\t',header=None,prefix='X',na_filter=False,chunksize=2)
#print(df8)      #<pandas.io.parsers.TextFileReader object at 0x079B3B68>
#for s in df8:
#    print(s)
'''
   X0  X1  X2
0  -1  -8  -2
1   8   9  -9
   X0  X1  X2
2   3   2   1
3  -4  -7   0
   X0  X1  X2
4  -4   0  -1
'''

#df8 = pd.read_table('ceui3.txt',sep='\t',header=None,prefix='X',na_filter=False,iterator=True)
#print(df8)          #<pandas.io.parsers.TextFileReader object at 0x07253B68>
#for s in df8:
#    print(s)
#print(df8.get_chunk(2))     #上面for循环使迭代器到达末尾
'''
   X0  X1  X2
0  -1  -8  -2
1   8   9  -9
'''
'''
compression : {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}, default ‘infer’
直接使用磁盘上的压缩文件。如果使用infer参数，则使用 gzip, bz2, zip或者解压文件名中以‘.gz’, ‘.bz2’, ‘.zip’, or ‘xz’这些为后缀的文件，否则不解压。如果使用zip，那么ZIP包中国必须只包含一个文件。设置为None则不解压。
新版本0.18.1版本支持zip和xz解压
'''
#thousands : str, default None  千分位分割符，如"，"或者"."
#decimal : str, default ‘.’  设置字符中的小数点 (例如：欧洲数据使用’，‘).
'''
float_precision : string, default None
Specifies which converter the C engine should use for floating-point values. The options are None for the ordinary converter, high for the high-precision converter, and round_trip for the round-trip converter.
指定
 
lineterminator : str (length 1), default None
行分割符，只在C解析器下使用。
 
quotechar : str (length 1), optional
引号，用作标识开始和解释的字符，引号内的分割符将被忽略。

quoting : int or csv.QUOTE_* instance, default 0
控制csv中的引号常量。可选 QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3)
当文本文件中带有英文双引号时，直接用pd.read_csv进行读取会导致行数减少，此时应该对read_csv设置参数quoting=3或者quoting=csv.QUOTE_NONE

doublequote : boolean, default True
双引号，当单引号已经被定义，并且quoting 参数不是QUOTE_NONE的时候，使用双引号表示引号内的元素作为一个元素使用。
 
escapechar : str (length 1), default None
当quoting 为QUOTE_NONE时，指定一个字符使的不受分隔符限值。
'''
'''
comment : str, default None
标识着多余的行不被解析。如果该字符出现在行首，这一行将被全部忽略。这个参数只能是一个字符，空行（就像skip_blank_lines=True）注释行被header和skiprows忽略一样。例如如果指定comment='#' 解析‘#empty\na,b,c\n1,2,3’ 以header=0 那么返回结果将是以’a,b,c'作为header。
'''
#encoding : str, default None  指定字符集类型，通常指定为'utf-8'. List of Python standard encodings
#tupleize_cols : boolean, default False  Leave a list of tuples on columns as is (default is to convert to a Multi Index on the columns)
#在列上保留元组列表（默认为在列上转换为多索引）

#error_bad_lines : boolean, default True
#如果一行包含太多的列，那么默认不会返回DataFrame ，如果设置成false，那么会将改行剔除（只能在C解析器下使用）。
#ParserError：Error tokenizing data.C error:Expected 2 fields in line 407,saw 3.

#ceui2.csv
'''
,C,A,B
-1,-2,-5,1
0,-5,-1,3
1,6,9,-5,6
2,5,-5,3
3,0,-3,-10
'''
#df9 = pd.read_table('ceui2.csv',sep=',',index_col=0)
#pandas.errors.ParserError: Error tokenizing data. C error: Expected 4 fields in line 4, saw 5
#df9 = pd.read_table('ceui2.csv',sep=',',index_col=0,error_bad_lines=False)
#b'Skipping line 4: expected 4 fields, saw 5\n'
'''
    C  A   B
-1 -2 -5   1
 0 -5 -1   3
 2  5 -5   3
 3  0 -3 -10
'''
#没有读取1的数据
'''
warn_bad_lines : boolean, default True
如果error_bad_lines =False，并且warn_bad_lines =True 那么所有的“bad lines”将会被输出（只能在C解析器下使用）。
'''
#memory_map : boolean, default False
#如果使用的文件在内存内，那么直接map文件使用。使用这种方式可以避免文件再次进行IO操作。
#df8 = pd.read_table('ceui2.txt',sep='\t',chunksize=2,index_col=0,memory_map=True)
#print(next(df8))
'''
    C  A  B
-1 -1 -8 -2
 0  8  9 -9
'''

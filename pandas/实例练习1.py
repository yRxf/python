###https://zhuanlan.zhihu.com/p/32572237
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator           #用于设置数值刻度
plt.rcParams["font.sans-serif"]=['Microsoft YaHei']     #处理中文
plt.rcParams['axes.unicode_minus']=False                #处理负号
#data = pd.read_csv('moCvie_metadata.csv')
#print(data.head())      #显示前5个数据
'''
   color      director_name  ...  aspect_ratio  movie_facebook_likes
0  Color      James Cameron  ...          1.78                 33000
1  Color     Gore Verbinski  ...          2.35                     0
2  Color         Sam Mendes  ...          2.35                 85000
3  Color  Christopher Nolan  ...          2.35                164000
4    NaN        Doug Walker  ...           NaN                     0
'''
#处理缺失数据
#添加默认值
#data.country.fillna('',inplace=True)  #就地修改。将NA值改为空
#data.duration.fillna(data.duration.mean(),inplace=True) #将电影的时长为NA或0的改为平均电压时长
#删除不完整的行
#data.dropna()  #删除包含NA的行
#data.dropna(how='all')  #删除一整行的值都为 NA
#data.dropna(thresh=5)    #在一行中有多少非空值的数据是可以保留下来的  行数据中至少要有 5 个非空值
#data.dropna(subset=['title_year'])  #删除列名为title_year里包含NA的行
#删除不完整的列  方法同行，使用参数,axis  0为行，1为列
#data.dropna(axis=1, how='any')  #删除任何包含NA的列
#规范化数据类型
#规范化我们数据类型的方式:读取数据的时候
#data = pd.read_csv('movie_metadata.csv', dtype={'duration': int,'title_year':str})
#告诉 Pandas ‘duration’,title_year列的类型是数值类型。
#print(data.country)
#data,rename(columns = {'title_year':'release_date','movie_facebook_likes':'facebook_likes'})

data = pd.read_csv('movie_metadata.csv')

#print(data.head())      #显示前5个数据
#print(data.shape)      #(5043, 28)  5043*28
#print(data.columns.to_list())     #显示列名
'''
['color', 'director_name', 'num_critic_for_reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 
'actor_2_name','actor_1_facebook_likes', 'gross', 'genres', 
'actor_1_name', 'movie_title', 'num_voted_users', 'cast_total_facebook_likes', 
'actor_3_name', 'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 
'language', 'country', 'content_rating', 'budget', 'title_year', 
'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes']
'''
#print(data.iloc[0].to_dict())    #查看第一行字段
'''
{'color': 'Color', 'director_name': 'James Cameron', 'num_critic_for_reviews': 723.0, 'duration': 178.0, 
'director_facebook_likes': 0.0, 'actor_3_facebook_likes': 855.0, 'actor_2_name': 'Joel David Moore', 
'actor_1_facebook_likes': 1000.0, 'gross': 760505847.0, 'genres': 'Action|Adventure|Fantasy|Sci-Fi', 'actor_1_name': 'CCH Pounder', 
'movie_title': 'Avatar\xa0', 'num_voted_users': 886204, 'cast_total_facebook_likes': 4834, 'actor_3_name': 'Wes Studi', 
'facenumber_in_poster': 0.0, 'plot_keywords': 'avatar|future|marine|native|paraplegic', 'movie_imdb_link': 'http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1', 
'num_user_for_reviews': 3054.0, 'language': 'English', 'country': 'USA', 'content_rating': 'PG-13', 'budget': 237000000.0, 'title_year': 2009.0, 
'actor_2_facebook_likes': 936.0, 'imdb_score': 7.9, 'aspect_ratio': 1.78, 'movie_facebook_likes': 33000}
'''
#print(data.dropna().shape) #(3756, 28)  存在有nan数据
#na_col = list(set(data.columns.to_list())-set(data.dropna(axis=1,how="any").columns.tolist()))   #存在nan的列
'''
['actor_1_facebook_likes', 'country', 'actor_1_name', 'actor_3_name', 
'color', 'director_facebook_likes', 'plot_keywords', 'actor_2_facebook_likes', 'duration', 'content_rating', 'actor_2_name', 
'facenumber_in_poster', 'num_user_for_reviews', 'title_year', 'actor_3_facebook_likes', 'num_critic_for_reviews', 
'aspect_ratio', 'director_name', 'language', 'budget', 'gross']
'''
#actor_1_facebook_likes、actor_2_facebook_likes、actor_3_facebook_likes、director_facebook_likes:男一号粉丝数  0
#country：地市  " "
#actor_1_name、actor_2_name、actor_3_name、director_name、:姓名  " "
#color  ？？
#plot_keywords：电影分类  " "
#duration：时长  平均时长
#content_rating：  分级   删除
#facenumber_in_poster：海报数量？  0
#num_user_for_reviews:观看人数  平均
#title_year： 年份  删除
# num_critic_for_reviews：评论人数 平均
#aspect_ratio：比例数量最大值
#language： " "
#budget:预算  平均
#gross：票房  平均

###粉丝数、演员有两个或以上不为na,则赋值为0
#data.loc[:,['actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes','director_facebook_likes']].replace(to_replace=r'^\s*$',value=np.nan,regex=True,inplace=True)
data.dropna(subset=['actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes','director_facebook_likes'],thresh=2,inplace=True)
data.loc[:,['actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes','director_facebook_likes']]=data.loc[:,['actor_1_facebook_likes','actor_2_facebook_likes','actor_3_facebook_likes','director_facebook_likes']].fillna("0.0")
data.dropna(subset=['actor_1_name','actor_2_name','actor_3_name','director_name'],thresh=2,inplace=True)
data.loc[:,['actor_1_name','actor_2_name','actor_3_name','director_name']]=data.loc[:,['actor_1_name','actor_2_name','actor_3_name','director_name']].fillna(" ")

data.country.fillna(" ",inplace=True)
###color:{nan, 'Color', ' Black and White'}  彩色、黑白、数量最大的
color_dict={data.color.tolist().count(x):x for x in set(data.color.tolist())}    #如果有两个相同数量的取其中一个就好了
color_v = color_dict[max(color_dict.keys())]
data.color.fillna(color_v,inplace=True)

data.plot_keywords.fillna(' ',inplace=True)
data.duration.fillna(data.duration.mean(),inplace=True)
data.dropna(subset=['content_rating'],inplace=True)
data.facenumber_in_poster.fillna('0.0',inplace=True)
data.num_user_for_reviews.fillna(data.num_user_for_reviews.mean(),inplace=True)
data.num_critic_for_reviews.fillna(data.num_critic_for_reviews.mean(),inplace=True)
data.dropna(subset=['title_year'],inplace=True)

aspect_ratio_dict={data.aspect_ratio.tolist().count(x):x for x in set(data.aspect_ratio.tolist())}    #如果有两个相同数量的取其中一个就好了
aspect_ratio_v = aspect_ratio_dict[max(aspect_ratio_dict.keys())]
data.aspect_ratio.fillna(aspect_ratio_v,inplace=True)

data.language.fillna(' ',inplace=True)
data.budget.fillna(data.budget.mean(),inplace=True)
data.gross.fillna(data.gross.mean(),inplace=True)
##按电影名称和上映时间去重
data.drop_duplicates(subset=['movie_title','title_year'],keep='first',inplace=True)
#print(data.shape)    #(4552, 28)


##统计票房前10的电影、movie_title、gross
data2 = data.loc[:,['movie_title','gross']].sort_values(by='gross',ascending=False).iloc[0:10]
movie = list(map(lambda x: "".join(x.split()),data2.movie_title.tolist()))
#由图可以看出数据存在2个电影名为：The Avengers的电影

#data3=data2.drop_duplicates(subset=['movie_title'], keep='first')
#print(data2)
gross_ = data2.gross.tolist()
#print(gross_)
v_g = gross_[len(gross_)//2]
gross_1 = [ round(g/v_g,6) for g in gross_]
'''
fig=plt.figure(num='竖直直方图',figsize=(8,8))
fig.add_axes([0.1, 0.13, 0.85, 0.8])

##定义图像初始位置
mngr = plt.get_current_fig_manager()
mngr.window.wm_geometry("+0+100")
plt.bar(range(len(movie)),gross_1, align='center',color='steelblue',alpha=0.8)
plt.title('票房前10的电影')
#电影名称过长，故倾斜名称
plt.xticks(range(len(movie)),movie,fontsize=8,rotation=15)
plt.xlabel("电影名称")
plt.ylabel("比例")


#设置y轴的范围
plt.ylim(0,max(gross_1)+0.2)

for x,y in enumerate(gross_1):
    plt.text(x,y+0.01,y,ha='center')

plt.show()
'''
'''
##或者水平显示
plt.figure(num='水平直方图',figsize=(12,5))
mngr = plt.get_current_fig_manager()
mngr.window.wm_geometry("+725+300")
plt.barh(range(len(movie)),gross_1, align='center',color='steelblue',alpha=0.8)
plt.yticks(range(len(movie)),movie)
plt.title('票房前10的电影')
plt.ylabel("电影名称")
plt.xlabel("比例")
#设置x轴的范围
plt.xlim(0,max(gross_1)+0.2)
for x,y in enumerate(gross_1):
    plt.text(y+0.01,x,y,ha='left')
plt.show()
'''

#年份电影数量
movie_year_color = data[['title_year','color']].set_index(['title_year'])
#year_dict={int(x):[movie_year_color.loc[x].apply(pd.value_counts).loc['Color'],movie_year_color.loc[x].apply(pd.value_counts).loc['Black and White']] for x in set(movie_year_color.index.tolist())}     #90  90个年份
#print(movie_year_color.loc[1950.0].color)
year_dict={}

for x in set(movie_year_color.index.tolist()):
    #年份1916和1932之间存在数个断层且数量没有太大变化，故删除1916-1932
    if int(x) < 1932:
        continue
    movie_color_x = movie_year_color.loc[x]
    if len(movie_color_x)>1:     #Dataframe
        try:
            color_x = int(movie_color_x.apply(pd.value_counts).loc['Color'])
        except:
            color_x = 0
        try:
            black_x = int(movie_color_x.apply(pd.value_counts).loc[' Black and White'])
        except:
            black_x = 0
        year_dict[int(x)] = [color_x+black_x,color_x,black_x]
    else:
        year_dict[int(x)] = [1,1,0] if movie_color_x.color == 'Color' else [1,0,1]

####垂直堆叠条形图
'''
fig=plt.figure(num='水平直方图',figsize=(15,7))
fig.add_axes([0.05, 0.1, 0.93, 0.8])            #调整坐标轴的位置  [距离左边，下边，坐标轴宽度，坐标轴高度]     百分比
x_count=len(list(year_dict.keys()))
b_a_w=[ v[2] for v in year_dict.values()]
cc=[ v[1] for v in year_dict.values()]
plt.bar(range(x_count),b_a_w,label='黑白',color='black',alpha=0.8,align='center')
plt.bar(range(x_count),cc,bottom=b_a_w,label='彩色',color='pink',alpha=0.8,align='center')

#为每个条形图添加数值标签
for x_t,y_t in enumerate(b_a_w):
    if y_t != 0:
        plt.text(x_t,y_t/2,y_t,ha='center',color='green',fontsize=8)

for x_g,y_g in enumerate(cc):
    if y_g >5:
        plt.text(x_g,y_g/2,y_g,ha='center',color='blue',fontsize=8)

for x_g,y_g in enumerate([ v[0] for v in year_dict.values()]):
    plt.text(x_g,y_g+2,y_g,ha='center',color='red',fontsize=8)

plt.text(1,210,"总数",ha='center',color='red',fontsize=12)
plt.text(1,200,"彩色",ha='center',color='blue',fontsize=12)
plt.text(1,190,"黑白",ha='center',color='green',fontsize=12)

#plt.legend(loc='upper center',ncol=4)

plt.title('各年电影情况')
plt.xlabel('年份')
plt.ylabel('电影数量')
plt.xticks(range(x_count),list(year_dict.keys()),fontsize=8,rotation=45)
#plt.xticks(np.arange(x_count),list(year_dict.keys()))
#x_major_locator=MultipleLocator(3)      #设置刻度间隔
y_major_locator=MultipleLocator(10)
ax=plt.gca()                            #获取各种设置
#ax.xaxis.set_major_locator(x_major_locator)     #设置刻度间隔

ax.yaxis.set_major_locator(y_major_locator)
plt.ylim([0,max([ v[0] for v in year_dict.values()])+10])
#plt.ylim([0,5])
plt.legend(loc='upper left')
plt.xlim(-1, x_count)
#plt.legend(loc='upper center',ncol=4,labels=student_scores.columns)
plt.show()
'''
'''
plt.style.use('ggplot')
fig=plt.figure(figsize=(10,6))
fig.add_axes([0.1, 0.1, 0.85, 0.8])
a=[ v[0] for v in year_dict.values() ]
plt.plot(list(year_dict.keys()), # x轴数据
         [ v[0] for v in year_dict.values() ], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 4, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='blue', # 点的填充色
         label='总和') 
plt.plot(list(year_dict.keys()), # x轴数据
         [ v[1] for v in year_dict.values()], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'pink', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 4, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='r', # 点的填充色
         label='彩色')
plt.plot(list(year_dict.keys()), # x轴数据
         [ v[2] for v in year_dict.values()], # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'black', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 4, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='brown', # 点的填充色
         label='黑白') 
plt.title('电影增长')
plt.xlabel('年份')
plt.ylabel('数量')
x_major_locator=MultipleLocator(5)      #设置刻度间隔
y_major_locator=MultipleLocator(10)
ax=plt.gca()                            #获取各种设置
ax.xaxis.set_major_locator(x_major_locator)     #设置刻度间隔
ax.yaxis.set_major_locator(y_major_locator)
plt.legend(loc='upper left')
plt.ylim(-5,max(a)+10)
plt.show()
'''
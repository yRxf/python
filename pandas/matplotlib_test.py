from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#中文乱码和坐标轴负号的处理
plt.rcParams["font.sans-serif"]=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
'''
fig=plt.figure(num='水平直方图',figsize=(15,7))
fig.add_axes([0.05, 0.1, 0.93, 0.8])            #调整坐标轴的位置  [距离左边，下边，坐标轴宽度，坐标轴高度]     百分比
x_major_locator=MultipleLocator(5)      #设置刻度间隔
y_major_locator=MultipleLocator(10)
ax=plt.gca()                            #获取各种设置
ax.xaxis.set_major_locator(x_major_locator)     #设置刻度间隔
ax.yaxis.set_major_locator(y_major_locator)
'''
'''
条形图
matplotlib.pyplot.bar(left, height, alpha=1, width=0.8, color=, edgecolor=, label=, lw=3)
left为x轴的位置序列，一般采用arange函数产生一个序列；
height为y轴的数值序列，也就是柱形图的高度，一般就是我们需要展示的数据；
width为柱形图的宽度，一般这是为1即可.一般默认，除非在交错图中会用到；
color为柱形图填充的颜色;
alpha:透明度，值越小越透明
edgecolor：图形边缘颜色
align设置plt.xticks()函数中的标签的位置,一般是center；
label:解释每个图像代表的含义
linewidth or linewidths or lw：边缘or线的宽
yerr让柱形图的顶端空出一部分。

*plt.title(‘图的标题’)函数：为图形添加标题。
plt.xlabel('x轴标签')   fontsize可以控制字体大小
plt.ylabel('y轴标签')
plt.legend(*args, **kwargs)函数：添加图例。参数必须为元组legend((line1, line2, line3), (‘label1’, ‘label2’,‘label3’))
'best'         : 0, (only implemented for axes legends)(自适应方式)
'upper right'  : 1,
'upper left'   : 2,
'lower left'   : 3,
'lower right'  : 4,
'right'        : 5,
'center left'  : 6,
'center right' : 7,
'lower center' : 8,
'upper center' : 9,
'center'       : 10,
plt.xlim(a,b)函数：设置x轴的范围。
plt.ylim(a,b)函数：设置y轴的范围。
Plt.xticks(*args, *kwargs)函数：获取或者设置X轴当前刻度的标签。Tuple1，tuple2长度相等，tuple1为对应的刻度，tuple2为对应刻度的标签。#rotation控制倾斜角度
plt.show()  显示图形
'''
'''
scores = np.random.randint(0,101,50)
scores2 = np.random.randint(0,101,50)
grade = [0 for i in range(6)]
grade2 = [0 for i in range(6)]
for score in scores:
    if score == 100:
        grade[5]+=1
    elif score >= 90:
        grade[4]+=1
    elif score >= 80:
        grade[3]+=1
    elif score >= 70:
        grade[2]+=1
    elif score >= 60:
        grade[1]+=1
    elif score < 60:
        grade[0]+=1
for score in scores2:
    if score == 100:
        grade2[5]+=1
    elif score >= 90:
        grade2[4]+=1
    elif score >= 80:
        grade2[3]+=1
    elif score >= 70:
        grade2[2]+=1
    elif score >= 60:
        grade2[1]+=1
    elif score < 60:
        grade2[0]+=1

plt.bar(range(len(grade)),grade, align='center',color='steelblue',alpha=0.8)
plt.title('班上成绩分布')

#竖直条形图

plt.xticks(range(len(grade)),list('EDCBAS'))
plt.xlabel("成绩等级")
plt.ylabel("人数")
#设置y轴的范围
plt.ylim([0,max(grade)+5])
for x,y in enumerate(grade):
    plt.text(x,y+0.5,y,ha='center')
plt.show()
'''
#水平条形图
#plt.barh(range(len(grade)),grade, align='center',color='steelblue',alpha=0.8)
#plt.yticks(range(len(grade)),list('EDCBAS'))
#plt.ylabel("成绩等级")
#plt.xlabel("人数")
#设置y轴的范围
#plt.xlim([0,max(grade)+5])
#for x,y in enumerate(grade):
#    plt.text(y+0.5,x,x,ha='center')
#plt.show()
'''
plt.bar(range(len(grade)),grade,width=0.4,align='center',color='steelblue',alpha=0.8,edgecolor='blue',lw=0.2,label='test1')
plt.bar([x+0.4 for x in range(len(grade))],grade2,width=0.4,align='center',color='indianred',alpha=0.8,edgecolor='red',lw=0.2,label='test2')

plt.title("班级成绩分布")
plt.xlabel('成绩等级')
plt.ylabel('人数')
plt.xticks(range(len(grade)),list('EDCBAS'))
plt.ylim([0,max(grade+grade2)+5])
for xt1,yt1 in enumerate(grade):
    plt.text(xt1,yt1+0.5,yt1,ha='center')
for xt2,yt2 in enumerate(grade2):
    plt.text(xt2+0.4,yt2+0.5,yt2,ha='center')
#添加图例。
plt.legend()
plt.show()
'''
####垂直堆叠条形图
'''
plt.bar(np.arange(8),data.loc[0,:][1:],label='铁路',color='red',alpha=0.8,align='center')
plt.bar(np.arange(8),data.loc[1,:][1:],bottom=data.loc[0,:][1:],label='公路',color='green',alpha=0.8,align='center')
plt.bar(np.arange(8),data.loc[2,:][1:],bottom=data.loc[0,:][1:]+data.loc[1,:][1:],label='水运',color='m',alpha=0.8,align='center')
plt.bar(np.arange(8),data.loc[3,:][1:],bottom=data.loc[0,:][1:]+data.loc[1,:][1:]+data.loc[2,:][1:],label='民航',color='black',alpha=0.8,align='center')
'''
'''
#为每个条形图添加数值标签
for x_t,y_t in enumerate(data.loc[0,:][1:]):
    plt.text(x_t,y_t/2,'%sW'%(round(y_t/10000,2)),ha='center',color='white')

for x_g,y_g in enumerate(data.loc[1,:][1:]+data.loc[0,:][1:]):
    plt.text(x_g,y_g/2,'%sW'%(round(y_g/10000,2)),ha='center',color='white')

for x_s,y_s in enumerate(data.loc[0,:][1:]+data.loc[1,:][1:]+data.loc[2,:][1:]):
    plt.text(x_s,y_s-20000,'%sW'%(round(y_s/10000,2)),ha='center',color='white')
#plt.legend(loc='upper center',ncol=4)
'''
'''
bottom参数：垂直堆叠条形图的设置不仅仅需要提供xy的数值，还需要提供bottom参数，目的就是在某个条形图顶端的基础上，绘制其他条形图，以此类推可以绘制多个堆叠条形图。

legend函数：图例的位置，在文中选择了正上方，且绘制列数为4，表面图例为一排的形式展现

堆叠条形图的数值标签，仍然按照y轴方向堆叠的思想，贴上数值标签值
'''
'''
student_scores = pd.read_excel('学生成绩.xlsx',index_col=0)
plt.bar(range(student_scores.shape[0]),student_scores.iloc[:,0],color='#ADFF2F',edgecolor='blue',lw=0.2,alpha=0.8)
plt.bar(range(student_scores.shape[0]),student_scores.iloc[:,1],bottom=student_scores.iloc[:,0],color='#FFEBCD',edgecolor='blue',lw=0.2,alpha=0.8,)
plt.bar(range(student_scores.shape[0]),student_scores.iloc[:,2],bottom=student_scores.iloc[:,0]+student_scores.iloc[:,1],color='#7FFFD4',edgecolor='blue',lw=0.2,alpha=0.8,)
plt.bar(range(student_scores.shape[0]),student_scores.iloc[:,3],bottom=student_scores.iloc[:,0]+student_scores.iloc[:,1]+student_scores.iloc[:,2],color='#D2691E',edgecolor='blue',lw=0.2,alpha=0.8,)

plt.title('模拟考试学生成绩')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.xticks(range(student_scores.shape[0]),student_scores.index)
plt.ylim([0,max(student_scores.iloc[:,4])+100])
plt.legend(loc='upper center',ncol=4,labels=student_scores.columns)
h = [0 for i in range(student_scores.shape[1])]
for i in range(student_scores.shape[1]):
    count = 0
    for x,y in enumerate(student_scores.iloc[:,i]):
        if i == student_scores.shape[1]-1:
            plt.text(x,y+3,y,ha='center',color='black')
        else:
            plt.text(x,(y/2)+h[count],y,ha='center',color='black') 
        h[count]+=y
        count+=1
plt.show()
'''

###饼图
'''
plt.pie(x, explode=None, labels=None, colors=None,      
    autopct=None, pctdistance=0.6, shadow=False,         
    labeldistance=1.1, startangle=None,        
    radius=None, counterclock=True, wedgeprops=None,        
    textprops=None, center=(0, 0), frame=False)
x：指定绘图的数据；
explode：指定饼图某些部分的突出显示，即呈现爆炸式；
labels：为饼图添加标签说明，类似于图例说明；
colors：指定饼图的填充色；
autopct：自动添加百分比显示，可以采用格式化的方法显示；
pctdistance：设置百分比标签与圆心的距离；
shadow：是否添加饼图的阴影效果；
labeldistance：设置各扇形标签（图例）与圆心的距离；
startangle：设置饼图的初始摆放角度；
radius：设置饼图的半径大小；
counterclock：是否让饼图按逆时针顺序呈现；
wedgeprops：设置饼图内外边界的属性，如边界线的粗细、颜色等；
textprops：设置饼图中文本的属性，如字体大小、颜色等；
center：指定饼图的中心点位置，默认为原点
frame：是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置；
'''
'''
plt.style.use('ggplot')

#构造数据
edu=[0.2515,0.3724,0.3336,0.0368,0.0057]
labels=['中专','大专','本科','硕士','其他']
explode=[0,0.1,0,0,0]#用于突出显示大专学历人群
colors=['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555']

#将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则是椭圆
plt.axes(aspect='equal')

#控制x轴和y轴的范围
plt.xlim(0,4)
plt.ylim(0,4)
#绘制饼图
plt.pie(
    x=edu,#绘制数据
    explode=explode,#突出显示大专人群
    labels=labels,#添加教育水平的标签
    colors=colors,#设置饼图的自定义填充色
    autopct='%.1f%%',#设置百分比格式，这里保留一位小数
    pctdistance=0.8,#设置百分比标签与圆心的距离
    labeldistance=1.15,#设置教育水平标签与圆心的距离
    startangle=180,#设置饼图的初始角度
    radius=1.5,#设置饼图的半径
    counterclock=False,#是否逆时针，这里设置为顺时针方向
    wedgeprops={'linewidth':1.5,'edgecolor':'green'},#设置饼图内外边界属性
    textprops={'fontsize':12,'color':'k'},#设置文本标签的属性值
    center=(1.8,1.8),#设置饼图的原点
    frame=1  # 是否显示饼图的原矿，这里设置是显示
)

#删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())

#添加标题
plt.title("芝麻信用失信用户教育水平分布")

#显示图形
plt.show()
'''

#折线图
#plt.hist(x,y,linestyle,linewidth,color,marker, markersize,markeredgecolor,markerfactcolor,label,alpha)
#x：指定折线图的x轴数据；
#y：指定折线图的y轴数据；
#linestyle：指定折线的类型，可以是实线、虚线、点虚线、点点线等，默认为实线；
#linewidth：指定折线的宽度
#marker：可以为折线图添加点，该参数是设置点的形状；
#markersize：设置点的大小；
#markeredgecolor：设置点的边框色；
#markerfactcolor：设置点的填充色；
#label：为折线图添加标签，类似于图例的作用；
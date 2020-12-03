import pandas as pd
import math
import numpy as np
# 显示所有列
from pandas import Series

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50

# 读取数据
input_data_excel = "F:/word文档/机器学习与数据挖掘/机器学习/一.数据源1.xlsx"
input_data_txt = "F:/word文档/机器学习与数据挖掘/机器学习/一.数据源2-逗号间隔.txt"
data = pd.read_excel(input_data_excel)
data1 = pd.read_csv(input_data_txt, sep=',')


# header=None表示数据没有名称

# 数据单位同化
# ID化为202***
def f(x):
    if x < 10:
        return '20200' + str(x)
    elif x >= 100:
        return '202' + str(x)
    else:
        return '2020' + str(x)


data['ID'] = data['ID'].apply(f)
#


# 性别统一为male/female
# excel中的性别
Gender = data['Gender'].tolist()
Gender_new = []
for i in Gender:
    if i == 'girl':
        Gender_new.append('female')
    if i == 'boy':
        Gender_new.append('male')
    if i == 'female':
        Gender_new.append('female')
    if i == 'male':
        Gender_new.append('male')
data['Gender'] = Gender_new
# txt中的性别
Gender1 = data1['Gender'].tolist()
Gender1_new = []
for i in Gender1:
    if i == 'girl':
        Gender1_new.append('female')
    if i == 'boy':
        Gender1_new.append('male')
    if i == 'female':
        Gender1_new.append('female')
    if i == 'male':
        Gender1_new.append('male')
data1['Gender'] = Gender1_new
#

# 身高Height的单位化为cm
# excel中的身高，数据在0-2.5中间的就*100，化为cm
Height = data['Height'].tolist()
Height_new = []
for i in Height:
    if 0 <= i <= 2.5:
        Height_new.append(i * 100)
    else:
        Height_new.append(i)
data['Height'] = Height_new
# txt中的身高，数据在0-2.5中间的就*100，化为cm
Height1 = data1['Height'].tolist()
Height1_new = []
for i in Height1:
    if 0 <= i <= 2.5:
        Height1_new.append(i * 100)
    else:
        Height1_new.append(i)
data1['Height'] = Height1_new
#
# 数据单位同化end


# 数据合并
data2 = pd.concat([data, data1])
# 数据合并end

# ID字符串转换成int
ID = data2['ID'].tolist()
ID_new = []
for i in ID:
    ID_new.append(int(i))
data2['ID'] = ID_new
# 字符串转换end


# 按照ID排序
data2 = data2.sort_values('ID', axis=0, ascending=True)
# 排序end

# 新添加一个序列，方便比较
k = 0
for i in data2['ID'].tolist():
    k = k + 1
data2['newID'] = range(k)

data2['C10'].fillna(0)
#
data2.info()

# 比较、填充、删除形成最终数据集
# data2.loc[data2['newID'] == i,'C10'] = i


for i in data2['newID'].tolist():
    if i != len(data2['newID']) - 1:
        if data2[data2['newID'] == i]['ID'].values == data2[data2['newID'] == i + 1]['ID'].values:
            # 如果ID、Name都一样，那么认为这2个数据是同一个人的，把前面的数据填充都后面的数据
            if data2[data2['newID'] == i]['Name'].values == data2[data2['newID'] == i + 1]['Name'].values:
                if pd.notnull(data2[data2['newID'] == i]['City'].values):
                    data2.loc[data2['newID'] == i + 1, 'City'] = data2[data2['newID'] == i]['City'].values
                if pd.notnull(data2[data2['newID'] == i]['Gender'].values):
                    data2.loc[data2['newID'] == i + 1, 'Gender'] = data2[data2['newID'] == i]['Gender'].values
                if pd.notnull(data2[data2['newID'] == i]['Height'].values):
                    data2.loc[data2['newID'] == i + 1, 'Height'] = data2[data2['newID'] == i]['Height'].values
                if pd.notnull(data2[data2['newID'] == i]['C1'].values):
                    data2.loc[data2['newID'] == i + 1, 'C1'] = data2[data2['newID'] == i]['C1'].values
                if pd.notnull(data2[data2['newID'] == i]['C2'].values):
                    data2.loc[data2['newID'] == i + 1, 'C2'] = data2[data2['newID'] == i]['C2'].values
                if pd.notnull(data2[data2['newID'] == i]['C3'].values):
                    data2.loc[data2['newID'] == i + 1, 'C3'] = data2[data2['newID'] == i]['C3'].values
                if pd.notnull(data2[data2['newID'] == i]['C4'].values):
                    data2.loc[data2['newID'] == i + 1, 'C4'] = data2[data2['newID'] == i]['C4'].values
                if pd.notnull(data2[data2['newID'] == i]['C5'].values):
                    data2.loc[data2['newID'] == i + 1, 'C5'] = data2[data2['newID'] == i]['C5'].values
                if pd.notnull(data2[data2['newID'] == i]['C6'].values):
                    data2.loc[data2['newID'] == i + 1, 'C6'] = data2[data2['newID'] == i]['C6'].values
                if pd.notnull(data2[data2['newID'] == i]['C7'].values):
                    data2.loc[data2['newID'] == i + 1, 'C7'] = data2[data2['newID'] == i]['C7'].values
                if pd.notnull(data2[data2['newID'] == i]['C8'].values):
                    data2.loc[data2['newID'] == i + 1, 'C8'] = data2[data2['newID'] == i]['C8'].values
                if pd.notnull(data2[data2['newID'] == i]['C9'].values):
                    data2.loc[data2['newID'] == i + 1, 'C9'] = data2[data2['newID'] == i]['C9'].values
                if pd.notnull(data2[data2['newID'] == i]['C10'].values):
                    data2.loc[data2['newID'] == i + 1, 'C10'] = data2[data2['newID'] == i]['C10'].values
                if pd.notnull(data2[data2['newID'] == i]['Constitution'].values):
                    data2.loc[data2['newID'] == i + 1, 'Constitution'] = data2[data2['newID'] == i]['Constitution'].values

data2 = data2.drop_duplicates(subset=['ID','Name'],keep='last')
#data2.to_csv('data2.csv')
print(data2)
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

#1.	学生中家乡在Beijing的所有课程的平均成绩。

test1=data2[data2['City']=='Beijing']
#print(test1)
C1_mean=test1['C1'].mean()
C2_mean=test1['C2'].mean()
C3_mean=test1['C3'].mean()
C4_mean=test1['C4'].mean()
C5_mean=test1['C5'].mean()
C6_mean=test1['C6'].mean()
C7_mean=test1['C7'].mean()
C8_mean=test1['C8'].mean()
C9_mean=test1['C9'].mean()
C10_mean=test1['C10'].mean()
print('家乡在北京的所有课程的平均成绩')
print('C1\t C2\t C3\t C4\t C5\t C6\t C7\t C8\t C9\t C10')
print('%.2f\t %.2f\t %.2f\t %.2f\t %.2f\t %.2f\t %.2f\t %.2f\t %.2f\t %.2f\t'%(C1_mean,C2_mean,C3_mean,C4_mean,C5_mean,C6_mean,C7_mean,C8_mean,C9_mean,C10_mean))

#2.	学生中家乡在广州，课程1在80分以上，且课程10在9分以上的男同学的数量
test2=data2[(data2['City']=='Guangzhou')& (data2['C1']>80 )& (data2['C10']>9) & (data2['Gender']=='male')].shape[0]
print('家乡在广州，课程1在80分以上，且课程10在9分以上的男同学的数量为%d'%test2)

#3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
#为比较体能成绩，为每人的成绩赋值，bad为60分，general为75分，good为85分，excellent为95分
test3_GZ=data2[(data2['City']=='Guangzhou')&(data2['Gender']=='female')]
test3_SH=data2[(data2['City']=='Shanghai')&(data2['Gender']=='female')]
map_score={'bad':60,'general':75,'good':85,'excellent':95}
test3_GZ_1=test3_GZ['Constitution'].map(map_score)
test3_SH_1=test3_SH['Constitution'].map(map_score)
test3_GZ_mean=test3_GZ_1.mean()
test3_SH_mean=test3_SH_1.mean()
print('广州女生平均体能成绩为%.2f'%test3_GZ_mean)
print('上海女生平均体能成绩为%.2f'%test3_SH_mean)
if test3_GZ_mean>test3_SH_mean:
    print('广州女生平均体能成绩更强')
elif test3_GZ_mean<test3_SH_mean:
    print('上海女生平均体能成绩更强')
else:
    print('两地区女生平均体能成绩相同')

#4.	学习成绩和体能测试成绩，两者的相关性是多少？
# 相关系数函数
def correlation(x,y):
    x_avg=sum(x)/len(x)
    y_avg=sum(y)/len(y)
    #计算x和y的协方差
    cov_xy=sum([(a-x_avg)*(b-y_avg) for a,b in zip(x,y)])
    #计算x的方差，y的方差的开方
    s2=math.sqrt(sum([(a-x_avg)**2for a in x])*sum([(b-y_avg)**2 for b in y]))
    return cov_xy/s2

r = []
# 体能成绩
y_constitution=[]
y_constitution=data2['Constitution'].map(map_score)
y_constitution=y_constitution.fillna(0).values
#print(y_constitution)
for k in range(1, 10):    # 9门成绩
    x_score = data2['C%d' % k].fillna(0).values
    #   计算9个相关性
    r.append(correlation(x_score,y_constitution))

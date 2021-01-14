import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# xy标题可以是中文
plt.rcParams['font.family'] = 'SimHei'
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 显示所有列
from pandas import Series

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50

# 读取数据
student = pd.read_csv("./studentdata.csv", sep=",")

# 题目1
# 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
C1andConstitution = []
C1 = student["C1"]
Constitution = student["Constitution"]

'''
plt.title("第1题")
plt.scatter(C1, Constitution)
plt.ylabel("体能成绩")
plt.xlabel("C1成绩")
plt.show()
'''

# 题目2
# 以5分为间隔，画出课程1的成绩直方图。
C1St = []
for i in range(101):
    if i > 0 and i % 5 == 0:
        C1St.append(i)

C1 = np.array(C1)
C1Count = []
for i in range(len(C1St)):
    count = 0
    for j in range(len(C1)):
        if C1St[i] - C1[j] >= 0 and C1St[i] - C1[j] <= 4:
            count = count + 1
        elif C1St[i] == 5 and C1[j] == 0:
            count = count + 1
    C1Count.append(count)
'''
plt.title("第2题")
plt.bar(C1St, C1Count)
plt.ylabel("成绩")
plt.xlabel("区间")
plt.show()
'''


# 题目3
# 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
# 将数据归一化
def autoNorm(dataSet):
    # 公式 原数据data = （每个data-最小数据datamin）/（最大数据datamax-datamin）
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals.values - minVals.values
    # dataSet.shape[0] 计算行数， shape[1] 计算列数
    m = dataSet.shape[0]
    # np.tile(minVals,(m,1)) 在行的方向上重复 minVals m次 即复制m行，在列的方向上重复munVals 1次，即复制1列
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    # normDataSet是归一化后的数据，ranges是最大数和最小数的差，minVals是最小数
    return normDataSet, ranges, minVals


# Constitution是体能成绩
Constitution = student['Constitution'].to_list()
Constitution_new = []
for i in Constitution:
    if i == 'bad':
        Constitution_new.append(25)
    if i == 'general':
        Constitution_new.append(50)
    if i == 'good':
        Constitution_new.append(75)
    if i == 'excellent':
        Constitution_new.append(100)
student['Constitution'] = Constitution_new
student.iloc[:, 5:16], ranges, minVals = autoNorm(student.iloc[:, 5:16])
# student.to_csv('z-scoreData.txt')

# 题目4
# 计算出100x100的相关矩阵，并可视化出混淆矩阵。
# （为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
data = student.iloc[:, 5:15]
C10 = []
for i in range(len(data)):
    C10.append(0)
data["C10"] = C10
data = np.array(data)
data = np.corrcoef(data)

fig = plt.figure()
ax = fig.add_subplot(111)

'''
# 热力图
cax = ax.matshow(data, vmin=-1, vmax=1)
# 将matshow生成热力图设置为颜色渐变条
fig.colorbar(cax)
ax.set_title("相关矩阵")
plt.show()
#print(data)
'''

# 题目5
# 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔
# 两点欧式距离
def distEclud(vecA, vecB):
    # np.power(x1,x2)  对x1中的每个元素求x2次方,不会改变x1。
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))


def distmin(dataSet):
    # 计算矩阵所有行数
    m = np.shape(dataSet)[0]
    # 用来记录对应的索引
    myindex = np.zeros((m, 3))
    # 遍历每一行数据
    for i in range(m):
        # 当前数据到所有行数据的差值  ,np.tile(x,(y,1)) 复制x 共y行 1列
        diffMat = np.tile(dataSet[i], (m, 1)) - dataSet
        # 对每个差值平方
        sqDiffMat = diffMat ** 2
        # axis=0指对向量每列求和，axis=1是对向量每行求和
        sqDistances = sqDiffMat.sum(axis=1)
        # 最后开方
        distance = sqDistances ** 0.5
        # x.argsort() 将x中的元素从小到大排序，提取其对应的index 索引，
        sortedDistIndicies = distance.argsort()
        myindex[i] = [sortedDistIndicies[1], sortedDistIndicies[2], sortedDistIndicies[3]]
    return myindex


# 用来记录索引对应的学生ID
StudentID = np.zeros((np.shape(data)[0], 3), dtype=int)
l = 0
for my_index in distmin(data):
    StudentID[l][0] = student.iloc[int(my_index[0])][0]
    StudentID[l][1] = student.iloc[int(my_index[1])][0]
    StudentID[l][2] = student.iloc[int(my_index[2])][0]
    l = l + 1
# 保存到txt文件
# np.savetxt('./dist.txt', StudentID, '%d', '\t')

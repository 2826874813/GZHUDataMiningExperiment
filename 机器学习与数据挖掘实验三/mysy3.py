import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import copy
import pickle
import random

def inxt(data, k,num):
    k_point={}
    record=[]
    while(len(record))!=k:
        r=random.randint(0,num-1)
        if r not in record:
            k_point[len(record)]=data[r]
            record.append(r)
    return k_point

def grade(point_tag,k_point,k,num,new_data,p_num,c_num):
    for i in range(0,k):
        k_point[i]=list(0 for i in range(c_num))

    for i in range(0, num):
        for j in range(0,c_num):
            k_point[point_tag[i]][j]+=copy.copy(new_data[i][j])

    for i in k_point:
        k_point[i]=[z/p_num[i] for z in k_point[i]]
    return k_point

def tagdue(k_point, k, data,coord_num):
    p_num={i: 0 for i in range(k)}
    point_tag = []
    flag=-1
    for line_list in data:
        dis = 1000000000000
        for i in range(0, k):
            d = 0
            for j in range(0, coord_num):
                d += (line_list[j] - k_point[i][j]) ** 2
            if d < dis:
                dis=d
                flag = i
        point_tag.append(copy.deepcopy(flag))
        p_num[flag]+=1

    return point_tag,p_num

def kmeans(data,c_num,num,k):
    p_num={i: 0 for i in range(k)}
    k_point = inxt(data, k, num)
    for i in range(0,1000):
        flag_num = copy.deepcopy(p_num)
        point_tag ,p_num= tagdue(k_point, k, data,c_num)
        flag =0
        for i in flag_num:
            if  flag_num[i]!=p_num[i]:
                flag=1
        if flag==0:
            break
        k_point=grade(point_tag,k_point,k,num,data,p_num,c_num)
    for i in range(0,k):
        print(k_point[i],'\n')
    return point_tag,k_point

def experiment(dataMatrix, k):

    mean_point = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    num = len(dataMatrix[0])
    coord_num=len(dataMatrix)

    old_dataMatrix = list(map(list, zip(*dataMatrix)))
    orderedNames =list(range(num))
    new_dataMatrix = np.array([old_dataMatrix[i] for i in orderedNames])

    kmeans(new_dataMatrix,coord_num,num,k)
    point_tag,k_point=kmeans(dataMatrix,coord_num,num,k)

    # 画两条（0-11）的坐标轴并设置轴标签x，y
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(xmax=11, xmin=0)
    plt.ylim(ymax=11, ymin=0)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x={i: [] for i in range(k)}
    y={i: [] for i in range(k)}
    colors=['b','c','g','y','r']
    labels=['类别A','类别B','类别C','类别D','类别E']
    area = np.pi * 4**2
    # 点面积
    r={i: -1 for i in range(k)}
    #类半径

    for i in range(0,num):
        d = sqrt(pow((dataMatrix[i][0] - k_point[point_tag[i]][0]),2) + pow((dataMatrix[i][1] - k_point[point_tag[i]][1]),2))
        if d > r[point_tag[i]]:
            r[point_tag[i]] = d

        x[point_tag[i]].append(dataMatrix[i][0])
        y[point_tag[i]].append(dataMatrix[i][1])

    theta = np.arange(0, 2 * np.pi, 0.01)

    for i in range(0,k):
        plt.scatter(x[i],y[i], s=area, c=colors[i], alpha=0.4, label=labels[i])
        plt.scatter(k_point[i][0], k_point[i][1], s=np.pi * 2**2, c=colors[i], alpha=1, label=labels[i]+'聚类中心')
        plt.plot(k_point[i][0] + r[i] * np.cos(theta), k_point[i][1] + r[i] * np.sin(theta),c=colors[i])

    # 第二题
    test_x = [3.45, 1.76, 4.29, 3.35, 3.17, 3.68, 2.11, 2.58, 3.45, 6.17, 4.20, 5.87, 5.47, 5.97, 6.24, 6.89, 5.38,
              5.13, 7.26, 6.32]
    test_y = [7.08, 7.24, 9.55, 6.65, 6.41, 5.99, 4.08, 7.10, 7.88, 5.40, 6.46, 3.87, 2.21, 3.62, 3.06, 2.41, 2.32,
              2.73, 4.19, 3.62]
    dataMatrix = list(zip(test_x, test_y))
    num = len(test_y)
    coord_num = len(dataMatrix[0])

    plt.plot([0,9.5],[9.5,0],linewidth = '0.5',color='#000000')
    plt.legend()
    plt.show()
    testpoint=[]
    for x in range(0,k):
        testpoint.append(sqrt((2-k_point[x][0])**2+(6-k_point[x][1])**2))
    ans={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    for y in range(0,k):
        if testpoint[y]<r[y]:
            print('点（2，6）属于%c类'%(ans[y]))

if __name__ == '__main__':
    _file = open('F:/z-scoreData.txt', 'rb')
    data = pickle.load(_file)

    for k in (2, 3, 4, 5):
        print("当聚类数为%d时" % (k))
        experiment(data, k)
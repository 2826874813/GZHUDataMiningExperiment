import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings


# sigmoid函数，映射值到概率
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 绘画sigmoid函数
def paint_sigmoid():
    # 绘图sigmoid函数
    nums = np.arange(-10, 10, step=1)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(nums, sigmoid(nums), 'r')
    plt.show()

'''
# 题目1
# 学习并画出sigmoid函数
paint_sigmoid()
'''

# 题目2
# 设计梯度下降算法，实现逻辑回归模型的学习过程。

# 题目3
# 根据给定数据（实验三.2），用梯度下降算法进行数据拟合，并用学习好的模型对(2,6)分类。

# 读取数据
data = pd.read_csv('./traindata.txt', sep=',')

# 数据在实验3分好类了，现在进行训练
x = data.iloc[:, 0:2]
y = data.iloc[:, 2:]
f = LogisticRegression()
f.fit(x, y)
y_hat = f.predict([[2, 6]])
print(y_hat)
# y_hat==1,(2, 6 )是1类


# 读取球员数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
players = pd.read_csv(r'count.csv')
players.head()



# 数据标准化处理
X = (players[['year']])
# 将数组转换为数据框

dataframe =pd.DataFrame(X, columns=['year'])
centers = np.array(dataframe)
c=1
yy=1921
result=[]
for i in range(len(centers)):
    if yy==centers[i+1]:
        c=c+1
    else:
        result.append([yy,c])
        c=1
        yy=centers[i+1]

result.to_csv("test.csv",index=False,sep=',')

# 读取球员数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
players = pd.read_csv(r'music_after_merge.csv')
players.head()

from sklearn import preprocessing
# 数据标准化处理
X = (players[['id','year']])
# 将数组转换为数据框
X = pd.DataFrame(X, columns=['id','year'])

result=[]
centers = np.array(X)
year=1932
c=0
list7=np.ones((100,2))
#print(list7)
#print(list7[1])
x=0
t=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
g=[0,0]
idd=189644

flag=0
for i in range(len(centers)):
    if centers[i][0]==idd:
        flag=1
        if centers[i][-1]==year:
            c=c+1
        else:
            g[0]=c
            g[1]=year
            #print(x)
            #print(c)
            #print(year)
            list7[x]=g
            result.append(list7[x])
            x=x+1
            year=centers[i][-1]
            c=1
    elif flag==1:
        g[0]=c
        g[1]=year
            #print(g)
        list7[x]=g
        result.append(list7[x])
        break
#print(result)
#result = preprocessing.minmax_scale(result)
dataframe =pd.DataFrame(result)

  

#将DataFrame存储为csv,index表示是否显示行名，default=True

dataframe.to_csv("189644.csv",index=False,sep=',')

#Latin

#Avant-Garde

#Blues
'''

def count(key):
    a=[]
    for i in range(100):
        a.append(0)
    for i in range(len(centers)):
        if centers[i][1]==key:
            t=centers[i][0]-1921
            a[t]=a[t]+1
    print(key)
    for i in range(100):
        print(a[i])

count('Latin')
count('Avant-Garde')
count('Blues')
count('Children\'s')
count('Classical')
count('Comedy/Spoken')
count('Country')
count('Easy Listening')
count('Electronic')
count('Folk')
count('International')
count('Jazz')
count('New Age')
count('R&B;')
count('Reggae')
count('Religious')
count('Stage & Screen')
count('Unknown')
count('Vocal')
count('')
'''

def get_cossimi(x,y):
    myx=np.array(x)
    myy=np.array(y)
    cos1=np.sum(myx*myy)
    return cos1
    #cos21=np.sqrt(sum(myy*myy))
    #cos22=np.sqrt(sum(myx*myx))
    #return (cos1/float(cos22*cos21))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
players = pd.read_csv(r'music_after_merge.csv')
players.head()

from sklearn import preprocessing
# 数据标准化处理
X = (players[['danceability','energy','acousticness','duration_ms','popularity']])
X = pd.DataFrame(X, columns=['danceability','energy','acousticness','duration_ms','popularity'])
X['danceability'] = X['danceability'].map(lambda x: x*0.095769)
X['energy'] = X['energy'].map(lambda x: x*0.093911)
X['acousticness'] = X['acousticness'].map(lambda x: x*0.118508)
X['duration_ms'] = X['duration_ms'].map(lambda x: x*0.088232)
X['popularity'] = X['popularity'].map(lambda x: x*0.102295)

X.to_csv("tes.csv",index=False,sep=',')
'''
X['id']=players[['id']]
centers = np.array(X)
print(centers[1])
result=[]
for i in range(300):
    for j in range(i+1,300):
        if centers[i][-1]==centers[j][-1]:
            #print(i)
            #print(j)
            #print(centers[i][-1])
            #print(centers[j][-1])
            result.append(get_cossimi(centers[i][:-2],centers[j][:-2]))
        else:
            break
result.sort()
print(result[(int)(1*len(result)/10)])
X['genre']=players[['genre']]
centers = np.array(X)
t=result[(int)(1*len(result)/10)]
def test1(i,key):
    g=0
    for k in range(300):
        if k==i:
            continue
        hh=get_cossimi(centers[k][:-3],centers[i][:-3])
        if (hh<key) & (centers[k][-1]!=centers[i][-1]):
            g=g+1
        if (hh>=key) & (centers[k][-1]==centers[i][-1]):
            g=g+1
    return g/299


ff=0
for k in range(300):
    ff = ff + test1(k,t)
print(ff/300)
'''

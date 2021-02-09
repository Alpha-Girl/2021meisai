def get_cossimi(x,y):
    myx=np.array(x)
    myy=np.array(y)
    cos1=np.sum(myx*myy)
    #return cos1
    cos21=np.sqrt(sum(myy*myy))
    cos22=np.sqrt(sum(myx*myx))
    if float(cos22*cos21)==0:
        return 1
    return (cos1/float(cos22*cos21))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
players = pd.read_csv(r'music_after_merge.csv')
players.head()

from sklearn import preprocessing
# 数据标准化处理
#X =preprocessing.minmax_scale(players[['danceability','energy','acousticness']])
X = preprocessing.minmax_scale(players[['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity']])
# 将数组转换为数据框
#X = pd.DataFrame(X, columns=['danceability','energy','acousticness'])
X = pd.DataFrame(X, columns=['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity'])
X['id']=players[['id']]
centers = np.array(X)
print(centers[1])
result=[]
a=90000
mm=0
for i in range(a):
    for j in range(i+1,a):
        mm=j
        if centers[i][-1]==centers[j][-1]:
            #print(i)
            #print(j)
            #print(centers[i][-1])
            #print(centers[j][-1])
            t=get_cossimi(centers[i][:-2],centers[j][:-2])
            #print(t)
            result.append(t)
        else:
            break
result.sort()
print(result[(int)(3*len(result)/10)])
X['genre']=players[['genre']]
centers = np.array(X)
t=result[(int)(3*len(result)/10)]

print("ss:")
for j in range(1,10):
    print(j)
    t=result[(int)(j*len(result)/10)]
    print(t)

'''
def test1(i,key):
    g=0
    for k in range(a):
        if k==i:
            continue
        hh=get_cossimi(centers[k][:-3],centers[i][:-3])
        if (hh<key) & (centers[k][-1]!=centers[i][-1]):
            g=g+1
        if (hh>=key) & (centers[k][-1]==centers[i][-1]):
            g=g+1
    return g/(a-1)

for j in range(1,10):
    print(j)
    ff=0
    t=result[(int)(j*len(result)/10)]
    for k in range(a):
        ff = ff + test1(k,t)
    print(ff/a)

'''

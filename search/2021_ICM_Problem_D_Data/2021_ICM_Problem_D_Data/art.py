kk=[0.7065777912592474,0.7646301332643743,0.804874228259362,0.8389113266482301,0.8728239646620105,0.9040447691568555,0.9296739138080857,0.9516945336727675,0.9716846842589397]
key=0.9433262814979388
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
players = pd.read_csv(r'artist-genre.csv')
players.head()

from sklearn import preprocessing
# 数据标准化处理
X = preprocessing.minmax_scale(players[['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity']])
# 将数组转换为数据框
X = pd.DataFrame(X, columns=['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity'])
X['genre']=players[['genre']]
centers = np.array(X)
print(centers[1])
def ggg(k):
    print(k)
#similarity-s
#t yes f no
    s_t=0
    s_f=0
#not_-n
    n_t=0
    n_f=0
    for i in range(300):
        for j in range(i+1,300):
            if get_cossimi(centers[i][:-2],centers[j][:-2])>=k:
                s=1
            else:
                s=0
            if centers[i][-1]==centers[j][-1]:
                r=1
            else:
                r=0
            if s & r:
                s_t=s_t+1
            elif s & ~r:
                s_f=s_f+1
            elif ~s & r:
                n_f=n_f+1
            else:
                n_t=n_t+1
    print(s_t)
    print(s_f)
    print(n_t)
    print(n_f)
            
for m in range(9):
    ggg(kk[m])

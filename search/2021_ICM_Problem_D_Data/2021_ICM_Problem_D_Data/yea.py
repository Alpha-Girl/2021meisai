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
players = pd.read_csv(r'data_by_year.csv')
players.head()

from sklearn import preprocessing
# 数据标准化处理
X =preprocessing.minmax_scale(players[['danceability','energy','acousticness','duration_ms','popularity']])
#X = preprocessing.minmax_scale(players[['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity']])
# 将数组转换为数据框
X = pd.DataFrame(X, columns=['danceability','energy','acousticness','duration_ms','popularity'])
#X = pd.DataFrame(X, columns=['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity'])
X['year']=players[['year']]
centers = np.array(X)
print(centers[1])

for i in range(99):
    if get_cossimi(centers[i][:-2],centers[i+1][:-2])<key:
        print(centers[i][-1])


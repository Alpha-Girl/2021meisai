# 读取球员数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##用sklearn的PCA
from sklearn.decomposition import PCA


players = pd.read_csv(r'F_tj.csv')

players.head()
from sklearn import preprocessing
X = preprocessing.minmax_scale(players[['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms']])
 



dataframe =pd.DataFrame(X, columns=['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms'])

  

#将DataFrame存储为csv,index表示是否显示行名，default=True

dataframe.to_csv("ffff.csv",index=False,sep=',')


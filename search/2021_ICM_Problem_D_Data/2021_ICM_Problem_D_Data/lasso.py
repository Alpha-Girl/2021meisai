# 读取球员数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##用sklearn的PCA
from sklearn.decomposition import PCA


players = pd.read_csv(r'full_music_data.csv')

players.head()
# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
def pca(X,k):#k is the components you want
  #mean of each feature
  n_samples, n_features = X.shape
  mean=np.array([np.mean(X[:,i]) for i in range(n_features)])
  #normalization
  norm_X=X-mean
  #scatter matrix
  scatter_matrix=np.dot(np.transpose(norm_X),norm_X)
  #Calculate the eigenvectors and eigenvalues
  eig_val, eig_vec = np.linalg.eig(scatter_matrix)
  eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(n_features)]
  # sort eig_vec based on eig_val from highest to lowest
  eig_pairs.sort(reverse=True)
  # select the top k eig_vec
  feature=np.array([ele[1] for ele in eig_pairs[:k]])
  #get new data
  data=np.dot(norm_X,np.transpose(feature))
  return data
from sklearn import preprocessing
X = preprocessing.minmax_scale(players[['danceability','energy','valence','tempo','loudness','mode','key','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity']])
 
print(pca(X,3))


dataframe =pd.DataFrame(pca(X,3), columns=['x1','x2','x3'])

  

#将DataFrame存储为csv,index表示是否显示行名，default=True

dataframe.to_csv("test.csv",index=False,sep=',')


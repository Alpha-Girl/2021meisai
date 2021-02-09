# 读取球员数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
players = pd.read_csv(r'music_after_merge.csv')
players.head()

from sklearn import preprocessing
# 数据标准化处理
X = (players[['year','genre']])
# 将数组转换为数据框
X = pd.DataFrame(X, columns=['year','genre'])


centers = np.array(X)

#Latin

#Avant-Garde

#Blues

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


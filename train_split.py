import os
import shutil
import pandas as pd
import numpy as np


data_train_path = 'ISIC_2019_Training_GroundTruth.csv'

data_train =  pd.read_csv(data_train_path)

train_path = './train'



train_base = '/datat'

for label in data_train:
    if label != 'image':
        if not os.path.exists('./train/' + label):
        # Nếu chưa tồn tại, tạo mới
            os.makedirs('./train/' + label)

        if not os.path.exists('./val/' + label):
        # Nếu chưa tồn tại, tạo mới
            os.makedirs('./val/' + label)

        if not os.path.exists('./test/' + label):
        # Nếu chưa tồn tại, tạo mới
            os.makedirs('./test/' + label)
      

# for label in data_train:
#     count = 0
#     for t in data_train[label]:
#         if t == 1:
#             count+=1
#     print(f'{label}: {count}')

for label in data_train:
    for i in range(len(data_train)):
        if data_train[label][i] == 1:
            file_path = train_base + data_train['image'][i] + '.jpg'
            shutil.copy(file_path, f'./train/{label}/')

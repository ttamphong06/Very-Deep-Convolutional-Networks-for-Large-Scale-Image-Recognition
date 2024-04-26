import os
import shutil
import pandas as pd
import random

data_train_path = 'ISIC_2019_Training_GroundTruth.csv'
data_train =  pd.read_csv(data_train_path)

train_label_path = []
test_label_path = []
imgs_label = []
for label in data_train:
    if label != 'image':
        train_label_path.append(f'./train/{label}')
        test_label_path.append(f'./test/{label}')
        imgs_label.append(os.listdir(f'./train/{label}/'))
print(train_label_path)
print(test_label_path)
print(imgs_label[1][1])

# for label in data_train:
#     if not os.path.exists('./test/' + label):
#     # Nếu chưa tồn tại, tạo mới
#         os.makedirs('./test/' + label)

for i in range(len(imgs_label)):
    random.shuffle(imgs_label[i])

for i in range(len(train_label_path)):
    if label != 'image':
        for j in range(int(len(imgs_label[i])*0.1)):
            file_path = train_label_path[i] + '/' + imgs_label[i][j]
            if os.path.exists(file_path):
                shutil.move(file_path, test_label_path[i])

# for i in range(int(len(mal_imgs)*0.2)):
#     file_path = malignant_path + '/' + mal_imgs[i]
#     shutil.move(file_path, malignant_des_path)
#     os.remove(file_path)

# for i in range(int(len(benign_imgs)*0.2)):
#     file_path = benign_path + '/' + benign_imgs[i]
#     shutil.move(file_path, benign_des_path)
#     os.remove(file_path)
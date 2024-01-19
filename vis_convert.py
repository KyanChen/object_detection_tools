import glob
import os
import random

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tqdm
import cv2
import skimage

# folder = r'H:\optimal\Airbus Ship Detection Challenge\slices512'
# csv_files = glob.glob(folder+'/*.csv')


# for csv_file in tqdm.tqdm(csv_files):
#     try:
#         df = pd.read_csv(csv_file)
#     except:
#         df = pd.read_excel(csv_file)
#     df.to_csv(csv_file, index=False)

# for csv_file in tqdm.tqdm(csv_files):
#     df = pd.read_csv(csv_file)
#     box_list = []
#     for idx, row in df.iterrows():
#         box = row['box']
#         box = box.replace(';', ',')
#         box = box.replace('[', '')
#         box = box.replace(']', '')
#         box = box.split(',')
#         box = [float(x) for x in box]
#         box_list.append(box)
#     box = np.array(box_list)
#     if len(box.shape) == 2:
#         df.loc[:, 'box'] = pd.Series(box.tolist())
#     elif len(box.shape) == 1:
#         df.loc[:, 'box'] = box.tolist()
#     df.to_csv(csv_file, index=False)

# for csv_file in tqdm.tqdm(csv_files):
#     df = pd.read_csv(csv_file)
#     if (df['class1'] == 0).all():
#         df['class1'] = 'ship'
#         df.to_csv(csv_file, index=False)
#     else:
#         print(csv_file)

# for csv_file in tqdm.tqdm(csv_files):
#     df = pd.read_csv(csv_file)
#     box = df['box']
#     box = np.array([eval(x) for x in box])
#     # box[:, 2:] = box[:, :2] + box[:, 2:]
#     box = box.tolist()
#     df['box'] = box
#     df.to_csv(csv_file, index=False)


# folder = r'F:\中船\labled'
# csv_files = glob.glob(folder+'/*.csv')
# csv_files = random.sample(csv_files, 10)
# for idx, csv_file in enumerate(csv_files):
#     img_file = csv_file.replace('.csv', '.jpg')
#     df = pd.read_csv(csv_file)
#     img = skimage.io.imread(img_file).copy()
#     # assert len(img.shape) == 3
#     if len(img.shape) == 2:
#         img = np.expand_dims(img, axis=-1)
#         img = np.concatenate([img, img, img], axis=-1)
#     for index, data in tqdm.tqdm(df.iterrows()):
#         cls = data['class1']
#         box = data['box']
#         box = np.array(eval(box))
#
#         box = np.clip(box, 0, 1024000)
#         img = cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 3)
#         img = cv2.putText(img, cls, (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     print(img_file)
#     plt.imshow(img)
#     plt.show()





# folder = r'F:\中船\labled'
# imgfiles = glob.glob(folder+'/*.tif')
# for imgfile in imgfiles:
#     csv_file = imgfile.replace('.tif', '.csv')
#     if not os.path.exists(csv_file):
#         open(csv_file, 'w').close()

folder = r'H:\optimal\军事港口'
csv_files = glob.glob(folder+'/*.csv')
for idx, csv_file in enumerate(csv_files):
    img_file = csv_file.replace('.csv', '.tif')
    df = pd.read_csv(csv_file).copy()
    img = skimage.io.imread(img_file)
    # assert len(img.shape) == 3
    if len(img.shape) == 2:
        img = np.expand_dims(img, axis=-1)
        img = np.concatenate([img, img, img], axis=-1)
    for index, data in tqdm.tqdm(df.iterrows()):
        cls = data['class1']
        box = data['box']
        box = np.array(eval(box))

        box = np.clip(box, 0, 1024000)
        img = cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 3)
        img = cv2.putText(img, cls, (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    print(img_file)
    img = cv2.resize(img, (16*150, 9*150))
    cv2.imshow('1', img)

    cv2.waitKey(0)
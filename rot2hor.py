import glob

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tqdm
from skimage import io

cvs_files = glob.glob(r'H:\SAR\SRSDD-v1.0\images\*.csv')
for cvs_file in tqdm.tqdm(cvs_files):
    data = pd.read_csv(cvs_file)
    # img_file = cvs_file.replace('.csv', '.png')
    # img = io.imread(img_file)
    try:
        hor_box = []
        for idx, row in data.iterrows():
            box = row['box [x1, y1, x2, y2, x3, y3, x4, y4]']
            box = eval(box)

            # # draw the rotated box
            # cv2.line(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 3)
            # cv2.line(img, (int(box[2]), int(box[3])), (int(box[4]), int(box[5])), (255, 0, 0), 3)
            # cv2.line(img, (int(box[4]), int(box[5])), (int(box[6]), int(box[7])), (255, 0, 0), 3)
            # cv2.line(img, (int(box[6]), int(box[7])), (int(box[0]), int(box[1])), (255, 0, 0), 3)

            box = np.array(box).reshape(-1, 2).astype(np.float32)
            horizontal_box = cv2.boundingRect(box)
            x, y, w, h = horizontal_box
            x1, y1, x2, y2 = x, y, x+w, y+h
            hor_box.append([x1, y1, x2, y2])
            # # draw the horizontal box
            # cv2.line(img, (int(x1), int(y1)), (int(x2), int(y1)), (0, 255, 0), 3)
            # cv2.line(img, (int(x2), int(y1)), (int(x2), int(y2)), (0, 255, 0), 3)
            # cv2.line(img, (int(x2), int(y2)), (int(x1), int(y2)), (0, 255, 0), 3)
            # cv2.line(img, (int(x1), int(y2)), (int(x1), int(y1)), (0, 255, 0), 3)

        # plt.imshow(img)
        # plt.show()
        hor_box = pd.Series(hor_box)
        data.loc[:, 'box'] = hor_box
        data.loc[:, 'rotated_box'] = data['box [x1, y1, x2, y2, x3, y3, x4, y4]']
        data = data.drop(columns='box [x1, y1, x2, y2, x3, y3, x4, y4]')
        data.to_csv(cvs_file, index=False)
    except:
        print(cvs_file)
        continue



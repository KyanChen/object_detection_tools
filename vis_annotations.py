import glob
import random

import mmcv
import numpy as np
import pandas as pd

folder = r'G:\SAR数据\part14'
files = glob.glob(folder + '/*.csv')
files = random.sample(files, 10)
for file in files:
    df = pd.read_csv(file)
    boxes = df['box']
    boxes = np.array([eval(x) for x in boxes])

    img = mmcv.imread(file.replace('.csv', '.jpg'))
    mmcv.imshow_bboxes(img, boxes, show=True, colors='red')


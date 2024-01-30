import glob

import cv2
import pandas as pd
import numpy as np
import tqdm
from skimage import io

# files = glob.glob(r'H:\SAR\DSSDD\originalTIF\train/*.tif')
# for file in tqdm.tqdm(files):
#     img = io.imread(file)
#     re = img[:, :, 0]
#     im = img[:, :, 1]
#     img = np.sqrt(re**2+im**2)
#     img = (img - np.min(img)) / (np.max(img) - np.min(img))*255
#     img = img.astype(np.uint8)
#     io.imsave(file.replace('.tif', '.png'), img)

files = glob.glob(r'H:\SAR\SSDD_coco\images/*.jpg')
# covert RGB to gray
for file in tqdm.tqdm(files):
    img = io.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    io.imsave(file, img)
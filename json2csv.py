import glob
import json
import os
import uuid
import pandas as pd
import cv2
import numpy as np
import skimage
from matplotlib import pyplot as plt
from tqdm import tqdm

# folder = r'H:\optimal\CASIA_Ship_Recognition\images\*.jpg'
# save_folder = r'H:\optimal\CASIA_Ship_Recognition\save_images'
# os.makedirs(save_folder, exist_ok=True)
# files = glob.glob(folder)
# for file in tqdm(files):
#     json_data = file.replace('.jpg', '.json')
#     json_data = json.load(open(json_data))
#     img = skimage.io.imread(file)
#     for object in json_data['shapes']:
#         unique_id = uuid.uuid4()
#         csv_data = {'class1': object['label']}
#         points = object['points']
#         points = np.array(points, dtype=np.int32)
#         x,y,w,h = cv2.boundingRect(points)
#         w = int(w*1.5)
#         h = int(h*1.5)
#         x = int(x - (w - w/1.5)/2)
#         y = int(y - (h - h/1.5)/2)
#         x1,y1,x2,y2 = x,y,x+w,y+h
#         x1 = max(0, x1)
#         y1 = max(0, y1)
#         x2 = min(img.shape[1], x2)
#         y2 = min(img.shape[0], y2)
#         crop_img = img[y1:y2, x1:x2]
#         skimage.io.imsave(os.path.join(save_folder, f'{unique_id}.jpg'), crop_img)
#         csv_data = pd.DataFrame(csv_data, index=[0])
#         csv_data.to_csv(os.path.join(save_folder, f'{unique_id}.csv'), index=False)
#     #     plt.imshow(crop_img)
#     #     plt.show()
#     # print()




folder = r'F:\中船\典型地区\*\*15.tif'
files = glob.glob(folder)
for file in tqdm(files):
    json_data = file.replace('.tif', '.json')
    if not os.path.exists(json_data):
        continue
    json_data = json.load(open(json_data))
    # img = skimage.io.imread(file)
    csv_data = {'class1': [], 'box': [], 'resolution': [], 'source': [], 'harbor': []}
    # harbor, resolution = os.path.basename(os.path.dirname(file)).split('-')
    harbor = os.path.basename(os.path.dirname(file))
    for object in json_data['shapes']:
        csv_data['harbor'].append(harbor)
        csv_data['resolution'].append('4')
        csv_data['source'].append('google earth')
        # unique_id = uuid.uuid4()
        csv_data['class1'].append(object['label'])
        points = object['points']
        points = np.array(points, dtype=np.int32)
        x,y,w,h = cv2.boundingRect(points)
        x1,y1,x2,y2 = x,y,x+w,y+h
        # x1 = max(0, x1)
        # y1 = max(0, y1)
        # x2 = min(img.shape[1], x2)
        # y2 = min(img.shape[0], y2)
        csv_data['box'].append(np.array([x1, y1, x2, y2]).tolist())
        # cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    csv_data = pd.DataFrame(csv_data)
    csv_data.to_csv(file.replace('.tif', '.csv'), index=False)
    # plt.imshow(img)
    # plt.show()
    # print()

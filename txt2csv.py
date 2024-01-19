import glob

import pandas as pd
import numpy as np
import tqdm

files = glob.glob(r'H:\optimal\Airbus Ship Detection Challenge\slices512\*.txt')
for file in tqdm.tqdm(files):
    data = np.loadtxt(file, dtype=str, delimiter=' ').reshape(-1, 4)
    # class1 = data[:, 0]
    boxes = data[:, :]
    boxes = boxes.astype(np.float32)
    csv_data = {'class1': [], 'box': [], 'resolution': [], 'source': []}
    for i in range(len(boxes)):
        csv_data['resolution'].append('none')
        csv_data['source'].append('none')
        csv_data['class1'].append('ship')
        box = boxes[i]
        x1 = box[0]
        y1 = box[1]
        x2 = box[2]
        y2 = box[3]
        csv_data['box'].append(np.array([x1, y1, x2, y2]).tolist())
    df = pd.DataFrame(csv_data)
    df.to_csv(file.replace('.txt', '.csv'), index=False)


# files = glob.glob(r'I:\Downloads\imageWithLabel\train\*.txt')
# save_dir = r''
# for file in tqdm.tqdm(files):
#     data = np.loadtxt(file, dtype=str, delimiter=' ').reshape(-1, 4)
#     # class1 = data[:, 0]
#     boxes = data[:, :]
#     boxes = boxes.astype(np.float32)
#     csv_data = {'class1': [], 'box': [], 'resolution': [], 'source': []}
#     for i in range(len(boxes)):
#         csv_data['resolution'].append('none')
#         csv_data['source'].append('none')
#         csv_data['class1'].append('ship')
#         box = boxes[i]
#         x1 = box[0]
#         y1 = box[1]
#         x2 = box[2]
#         y2 = box[3]
#         csv_data['box'].append(np.array([x1, y1, x2, y2]).tolist())
#     df = pd.DataFrame(csv_data)
#     df.to_csv(file.replace('.txt', '.csv'), index=False)

import glob
import os
import shutil

import pandas as pd
import tqdm

# # cp files from subfolders to a new folder
# files = glob.glob(r'H:\SAR\AIR-SARShip-1.0\*\*', recursive=True)
# save_path = r'H:\SAR\AIR-SARShip-1.0\images'
# os.makedirs(save_path, exist_ok=True)
# for file in tqdm.tqdm(files):
#     shutil.copy(file, save_path)


# # cp files from subfolders to a new folder
# files = glob.glob(r'H:\SAR\分类\FUSAR-Ship Dataset\*\*\*.tiff', recursive=True)
# save_path = r'H:\SAR\分类\FUSAR-Ship Dataset\images'
# os.makedirs(save_path, exist_ok=True)
# for file in tqdm.tqdm(files):
#     shutil.copy(file, save_path)
#     csv_file = file.replace('.tiff', '.csv')
#     data = pd.read_csv(csv_file)
#     class1 = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
#     data['class1'] = pd.Series([class1])
#     class2 = os.path.basename(os.path.dirname(csv_file))
#     data['class2'] = pd.Series([class2])
#     data.to_csv(csv_file, index=False)
#     shutil.copy(csv_file, save_path)


# # cp files from subfolders to a new folder
# files = glob.glob(r'H:\光学\Airbus Ship Detection Challenge\train_v2\*.csv', recursive=True)
# save_path = r'H:\光学\Airbus Ship Detection Challenge\images'
# os.makedirs(save_path, exist_ok=True)
# for file in tqdm.tqdm(files):
#     try:
#         shutil.move(file, save_path)
#     except:
#         pass
#     img_file = file.replace('.csv', '.jpg')
#     try:
#         shutil.move(img_file, save_path)
#     except:
#         pass


# cp files from subfolders to a new folder
files = glob.glob(r'F:\中船\典型地区\*\*15.tif')
save_path = r'F:\中船\labled'
os.makedirs(save_path, exist_ok=True)
for file in tqdm.tqdm(files):
    new_filename = os.path.basename(os.path.dirname(file)) + '_' + os.path.basename(file)
    shutil.copy(file, save_path+'/'+new_filename)
    csv_file = file.replace('.tif', '.csv')
    if os.path.exists(csv_file):
        shutil.copy(csv_file, save_path+'/'+new_filename.replace('.tif', '.csv'))

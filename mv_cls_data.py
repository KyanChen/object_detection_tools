import glob
import os
import shutil

import pandas as pd
from tqdm import tqdm

# label_dict = {'0':'non-ship',
# '1':'air carrier',
# '2':'destroyer',
# '3':'landing craft',
# '4':'frigate',
# '5':'amphibious transport dock',
# '6':'cruiser',
# '7':'Tarawa-class amphibious assault ship',
# '8':'amphibious assault ship',
# '9':'command ship',
# '10':'submarine',
# '11':'medical ship',
# '12':'combat boat',
# '13':'auxiliary ship',
# '14':'container ship',
# '15':'car carrier',
# '16':'hovercraft',
# '17':'bulk carrier',
# '18':'oil tanker',
# '19':'fishing boat',
# '20':'passenger ship',
# '21':'liquefied gas ship',
# '22':'barge'}
# # cp files from subfolders to a new folder
# files = glob.glob(r'H:\光学\FGSC-23\train\*\*.jpg', recursive=True)
# save_path = r'H:\光学\FGSC-23\images'
# os.makedirs(save_path, exist_ok=True)
#
# for file in tqdm(files):
#     data = {'class1': []}
#     shutil.copy(file, save_path)
#     csv_file = file.replace('.jpg', '.csv')
#     # data = pd.read_csv(csv_file)
#     # class1 = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
#     # data['class1'] = pd.Series([class1])
#     class1 = os.path.basename(os.path.dirname(csv_file))
#     class1 = label_dict[class1]
#
#     data['class1'].append(class1)
#     data = pd.DataFrame(data)
#     data.to_csv(csv_file, index=False)
#     shutil.copy(csv_file, save_path)


# cp files from subfolders to a new folder
files = glob.glob(r'H:\光学\FGSCR-42\*\*.bmp', recursive=True)
save_path = r'H:\光学\FGSCR-42\images'
os.makedirs(save_path, exist_ok=True)

for file in tqdm(files):
    data = {'class1': []}
    shutil.copy(file, save_path)
    csv_file = file.replace('.bmp', '.csv')
    # data = pd.read_csv(csv_file)
    # class1 = os.path.basename(os.path.dirname(os.path.dirname(csv_file)))
    # data['class1'] = pd.Series([class1])
    class1 = os.path.basename(os.path.dirname(csv_file)).split('.')[-1]

    data['class1'].append(class1)
    data = pd.DataFrame(data)
    data.to_csv(csv_file, index=False)
    shutil.copy(csv_file, save_path)
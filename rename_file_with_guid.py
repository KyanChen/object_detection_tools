import glob
import os
from tqdm import tqdm
import uuid

folder = "G:\check_folder"
img_format = '.jpg'
dataset_type = 0

csv_files = glob.glob(os.path.join(folder, '*.csv'))
for file in tqdm(csv_files):
    if not os.path.exists(file.replace('.csv', img_format)):
        print(file)
        raise ValueError
    new_file_name = f'{dataset_type}_{uuid.uuid4()}.csv'
    os.rename(file, os.path.join(folder, new_file_name))
    os.rename(file.replace('.csv', img_format), os.path.join(folder, new_file_name.replace('.csv', img_format)))
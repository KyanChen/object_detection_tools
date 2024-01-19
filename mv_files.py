import glob
import os
import shutil

from tqdm import tqdm

folder = r'H:\optimal\Airbus Ship Detection Challenge\20211110_Slice\images\*.txt'
save_folder = r'H:\optimal\Airbus Ship Detection Challenge\slices512'
os.makedirs(save_folder, exist_ok=True)
files = glob.glob(folder)
for file in tqdm(files):
    if os.path.getsize(file) > 0:
        shutil.copy(file, save_folder)
        img_file = file.replace('.txt', '.jpg')
        shutil.copy(img_file, save_folder)

# folder = r'H:\光学\S2Ships\dataset_tif\*\*'
# save_folder = r'H:\光学\S2Ships\images'
# os.makedirs(save_folder, exist_ok=True)
# files = glob.glob(folder)
# for file in tqdm(files):
#     shutil.move(file, save_folder)
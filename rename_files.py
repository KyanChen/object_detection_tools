import glob
import os

from tqdm import tqdm

# files = glob.glob(r'H:\SAR\AIR-SARShip-1.0\images/*')
# for file in tqdm(files):
#     file_name_new = file.replace('-label.', '.')
#     # rename
#     os.rename(file, file_name_new)

# files = glob.glob(r'H:\光学\S2Ships\dataset_tif\*\*')
# for file in tqdm(files):
#     dir_name, file_name = os.path.dirname(file), os.path.basename(file)
#     file_name_new = os.path.join(dir_name, os.path.basename(dir_name)+'_'+file_name)
#     # rename
#     os.rename(file, file_name_new)

files = glob.glob(r'H:\光学\S2Ships\*.csv')
for file in tqdm(files):
    dir_name, file_name = os.path.dirname(file), os.path.basename(file)
    file_name_new = os.path.join(dir_name, file_name.split('_')[0]+'_'+file_name)
    # rename
    os.rename(file, file_name_new)
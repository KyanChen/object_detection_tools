import glob
import os

from tqdm import tqdm
import uuid

img_format = '.tif'
files = glob.glob(r'H:\示例数据2\光学\*.csv')
for file in tqdm(files):
    dir_name = os.path.dirname(file)
    file_name = os.path.basename(file)

    if not os.path.exists(file.replace('.csv', img_format)):
        print(file)
        continue
    harbor_name = file_name.split('_')[1]
    file_name_new = os.path.join(dir_name, harbor_name+'_'+str(uuid.uuid4())+'.csv')
    os.rename(file, file_name_new)
    file_name_new = file_name_new.replace('.csv', img_format)
    os.rename(file.replace('.csv', img_format), file_name_new)

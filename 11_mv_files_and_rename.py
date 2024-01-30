import glob
import os
import uuid
import pandas as pd
from tqdm import tqdm
import mmengine


def move_file(item):
    file, save_folder, img_format, dataset_type = item
    # rename file
    new_file_name = f'{dataset_type}_{uuid.uuid4()}{img_format}'
    # move csv
    csv_file = file.replace(img_format, '.csv')
    if os.path.exists(csv_file):
        os.rename(file, os.path.join(save_folder, new_file_name))
        os.rename(csv_file, os.path.join(save_folder, new_file_name.replace(img_format, '.csv')))
        # os.rename(file.replace(img_format, '.tif'), os.path.join(save_folder, new_file_name.replace(img_format, '.tif')))
    else:
        # infos = os.path.basename(file).split('_')
        # infos = infos[:-1]
        # loc = infos[0]
        # cls_name = ' '.join(infos[:-1])
        # source = infos[-1]
        csv_data = {
            'source': [f'红外目标-仿真-IRShip'],
            'task_type': ['cls'],
            'class_name': ['ship'],
        }
        os.rename(file, os.path.join(save_folder, new_file_name))
        df = pd.DataFrame(csv_data)
        df.to_csv(os.path.join(save_folder, new_file_name.replace(img_format, '.csv')), index=False)


if __name__ == '__main__':
    folder = r'G:\红外数据\part1\images'
    # folder = r'G:\光学数据\part1'
    save_folder = r'G:\红外数据\part16'
    dataset_type = 13
    img_format = '.png'
    max_num = 16000
    nproc = 16
    os.makedirs(save_folder, exist_ok=True)
    files = glob.glob(folder + '/*' + img_format)[:max_num]
    files = [(file, save_folder, img_format, dataset_type) for file in files]
    if nproc == 0:
        mmengine.track_progress(move_file, files)
    mmengine.track_parallel_progress(move_file, files, nproc=nproc)


import glob
import os
import uuid

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
    else:
        print(f'{csv_file} not exists')


if __name__ == '__main__':
    folder = r'G:\SAR数据\part14'
    # folder = r'G:\光学数据\part1'
    save_folder = r'G:\SAR数据\part14'
    dataset_type = 10
    img_format = '.jpg'
    max_num = 16000
    nproc = 16
    os.makedirs(save_folder, exist_ok=True)
    files = glob.glob(folder + '/*' + img_format)[:max_num]
    files = [(file, save_folder, img_format, dataset_type) for file in files]
    mmengine.track_parallel_progress(move_file, files, nproc=nproc)


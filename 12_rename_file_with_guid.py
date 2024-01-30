import glob
import os
from tqdm import tqdm
import uuid
import mmengine

def rename_file(item):
    file, img_format, dataset_type = item
    if not os.path.exists(file.replace('.csv', img_format)):
        print(file)
        raise ValueError
    new_file_name = f'{dataset_type}_{uuid.uuid4()}.csv'
    os.rename(file, os.path.join(os.path.dirname(file), new_file_name))
    os.rename(file.replace('.csv', img_format), os.path.join(os.path.dirname(file), new_file_name.replace('.csv', img_format)))


if __name__ == '__main__':
    # for i in range(3, 6):
    #     folder = f"G:\光学数据\part{i}"
    folder = "G:\红外数据\part7"
    img_format = '.png'
    dataset_type = 6
    nproc = 16
    csv_files = glob.glob(os.path.join(folder, '*.csv'))
    files = [(file, img_format, dataset_type) for file in csv_files]
    mmengine.track_parallel_progress(rename_file, files, nproc=nproc)

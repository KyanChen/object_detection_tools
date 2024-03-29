import glob

import mmcv
import mmengine
import numpy as np
import pandas as pd
import os
try:
    from global_land_mask import globe
except ImportError:
    os.system('pip install global-land-mask')
    from global_land_mask import globe

def add_info(file):
    try:
        ori_data = pd.read_csv(file)
    except:
        print(file)
        return None
    task_type = 'det'  # cls, det
    dataset_type = 13
    img_format = '.png'
    class_name = None
    source = '红外目标-仿真-IRShip'  # google, GF1/6,

    # random a resolution between 0.5 and 10
    # resolution = np.random.rand() * 9.5 + 0.5
    # 1m到3m
    # 100m
    resolution = np.random.rand() * 2 + 1
    resolution = 100
    resolution = round(resolution, 2)

    # # generate a location in the sea
    # # 东经正，西经负，北纬正，南纬负
    # while True:
    #     random_lat = np.random.rand() * 150 - 75
    #     random_lon = np.random.rand() * 360 - 180
    #     # round to 5 decimal place
    #     random_lat = round(random_lat, 5)
    #     random_lon = round(random_lon, 5)
    #     if globe.is_ocean(random_lat, random_lon):
    #         break
    # location = f'{random_lat},{random_lon}'
    # if 'HV' in file:
    #     polarization = 'HV'
    # elif 'VH' in file:
    #     polarization = 'HV'
    # elif 'VV' in file:
    #     polarization = 'VV'
    # else:
    #     polarization = 'HH'

    save_data = dict(
        task_type=[],
        img_name=[],
        img_size=[],
        dataset_type=[],
        class_name=[],
        box=[],
        obj_description=[],
        source=[],
        resolution=[],
        material=[],
    )
    img_name = os.path.basename(file).replace('.csv', img_format)
    img_size = mmcv.imread(file.replace('.csv', img_format)).shape[:2]

    # 名称、宽高、分辨率、材质、目标类别、位置、目标特征、检测框
    for idx, row in ori_data.iterrows():
        if 'box' in row:
            return None
        save_data['task_type'].append(task_type)
        save_data['dataset_type'].append(dataset_type)
        save_data['img_name'].append(img_name)
        save_data['img_size'].append(img_size)

        material = np.random.choice(['金属', '非金属', '复合材料'], p=[0.6, 0.1, 0.3])
        save_data['material'].append(material)
        if source is None:
            source = row['source']
        save_data['source'].append(source)
        save_data['resolution'].append(resolution)

        try:
            xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
            save_data['box'].append([xmin, ymin, xmax, ymax])
        except:
            save_data['box'].append([])
        if class_name is None:
            if 'class_name' in row:
                class_name = row['class_name']
            elif 'class' in row:
                class_name = row['class']
            else:
                raise ValueError

        if task_type == 'cls':
            obj_description = f'a {class_name}'
        else:
            try:
                obj_description = f'a {class_name} with width {xmax - xmin} and height {ymax - ymin}, its area is {(xmax - xmin) * (ymax - ymin)}'
            except:
                obj_description = f'a {class_name}'
        save_data['obj_description'].append(obj_description)
        save_data['class_name'].append(class_name)

        if 'location' in row:
            location = row['location']
            if 'location' not in save_data:
                save_data['location'] = []
            save_data['location'].append(location)


    df = pd.DataFrame(save_data)
    df.to_csv(file, index=False)


if __name__ == '__main__':
    # for i in range(1, 6):
    #     folder = f'G:\\光学数据\\part{i}'
    folder = r'G:\红外数据\part15'
    files = glob.glob(folder + '/*.csv')
    nproc = 16
    if nproc == 0:
        mmengine.track_progress(add_info, files)
    else:
        mmengine.track_parallel_progress(add_info, files, nproc=nproc)
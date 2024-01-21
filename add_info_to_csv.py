import glob
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
    dataset_type = 10
    source = 'RadarSat-2、TerraSAR-X、 Sentinel-1'  # google, GF1/6,

    # random a resolution between 0.5 and 10
    # resolution = np.random.rand() * 9.5 + 0.5
    resolution = np.random.rand() * 2 + 0.1
    resolution = 1
    # round to 2 decimal place
    resolution = round(resolution, 2)

    # generate a location in the sea
    # 东经正，西经负，北纬正，南纬负
    while True:
        random_lat = np.random.rand() * 150 - 75
        random_lon = np.random.rand() * 360 - 180
        # round to 5 decimal place
        random_lat = round(random_lat, 5)
        random_lon = round(random_lon, 5)
        if globe.is_ocean(random_lat, random_lon):
            break
    location = f'{random_lat},{random_lon}'
    if 'HV' in file:
        polarization = 'HV'
    elif 'VH' in file:
        polarization = 'HV'
    elif 'VV' in file:
        polarization = 'VV'
    else:
        polarization = 'HH'

    save_data = dict(
        task_type=[],
        dataset_type=[],
        class_name=[],
        box=[],
        source=[],
        resolution=[],
        location=[],
        polarization=[],
    )

    for row in ori_data.iterrows():
        row = row[1]
        save_data['task_type'].append(task_type)
        save_data['dataset_type'].append(dataset_type)
        if 'class_name' in row:
            cls_name = row['class_name']
            save_data['class_name'].append(cls_name)
        else:
            cls_name = row['class1']
            cls_name = 'ship' if cls_name == 'shiip' else cls_name
            save_data['class_name'].append(cls_name)
        if task_type == 'cls':
            save_data['box'].append([])
        else:
            save_data['box'].append(row['box'])
        save_data['source'].append(source)
        save_data['resolution'].append(resolution)
        save_data['location'].append(location)
        save_data['polarization'].append(polarization)

    df = pd.DataFrame(save_data)
    df.to_csv(file, index=False)


if __name__ == '__main__':
    # for i in range(1, 6):
    #     folder = f'G:\\光学数据\\part{i}'
    folder = r'G:\SAR数据\part14'
    files = glob.glob(folder + '/*.csv')
    nproc = 16
    if nproc == 0:
        mmengine.track_progress(add_info, files)
    else:
        mmengine.track_parallel_progress(add_info, files, nproc=nproc)
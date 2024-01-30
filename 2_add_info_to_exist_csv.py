import glob

import mmcv
import mmengine
import numpy as np
import pandas as pd
import os
import imagesize
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
    img_format = '.tiff'
    ori_data = ori_data.to_dict(orient='list')
    if 'box' not in ori_data:
        ori_data['box'] = ['[]']
    adding_keys = ['img_name', 'img_size', 'obj_description', 'harbor', 'class_name', 'location', 'resolution', 'source', 'material', 'size',
                   'polarization'
                   ]

    num_boxes = len(ori_data['box'])

    img_name = os.path.basename(file).replace('.csv', img_format)
    img_size = imagesize.get(file.replace('.csv', img_format))
    if img_size[0] < 2:
        img_size = mmcv.imread(file.replace('.csv', img_format)).shape[:2]

    # random a resolution between 0.5 and 10
    # resolution = np.random.rand() * 9.5 + 0.5
    resolution_gen = np.random.rand() * 7 + 15
    resolution_gen = 20
    # round to 2 decimal place
    resolution_gen = round(resolution_gen, 2)

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
    location_gen = f'{random_lat},{random_lon}'
    source = 'RadarSat-2、GF'

    adding_data = {key: [] for key in adding_keys}
    materials = ['复合金属材料', '金属材料', '非金属材料']
    for idx in range(num_boxes):
        adding_data['img_name'].append(img_name)
        adding_data['img_size'].append(img_size)
        adding_data['material'].append(np.random.choice(materials, p=[0.7, 0.2, 0.1]))
        adding_data['size'].append(img_size)

        if 'class_name' not in ori_data:
            if 'class3' in ori_data:
                class_name = f'{ori_data["class1"][idx]}#{ori_data["class2"][idx]}#{ori_data["class3"][idx]}'
            elif 'class2' in ori_data:
                class_name = f'{ori_data["class1"][idx]}#{ori_data["class2"][idx]}'
            else:
                class_name = ori_data["class1"][idx]
        else:
            class_name = ori_data["class_name"][idx]
        adding_data['class_name'].append(class_name)

        if 'img_location' in ori_data:
            location = ori_data['img_location'][idx]
        else:
            try:
                location = ori_data['location'][idx]
            except:
                location = location_gen
        adding_data['location'].append(location)

        if 'resolution' in ori_data and ori_data['resolution'][idx] != 'none':
            resolution = ori_data['resolution'][idx]
        else:
            resolution = resolution_gen
        # resolution = resolution_gen
        adding_data['resolution'].append(resolution)

        if 'source' in ori_data and ori_data['source'][idx] != 'none':
            source = ori_data['source'][idx]
        adding_data['source'].append(source)

        box = ori_data['box'][idx]
        if box == '[]':
            obj_description = f'A {class_name} in {location}'
        else:
            l, b, r, t = eval(box)
            obj_description = f'A {class_name} in {location} with width {r - l} and height {t - b}, and the area is {(r - l) * (t - b)}'
        adding_data['obj_description'].append(obj_description)

        if 'place_id' in ori_data:
            place_id = ori_data['place_id'][idx]
            harbor = place_id
        elif 'ship location' in ori_data:
            harbor = ori_data['ship location'][idx]
        else:
            harbor = 'none'
        adding_data['harbor'].append(harbor)

        if 'polarization' not in ori_data and 'polarMode' in ori_data:
            polarization = ori_data['polarMode'][idx]
        elif 'polarization' not in ori_data:
            polarization = 'HH'
        else:
            polarization = ori_data['polarization'][idx]
        adding_data['polarization'].append(polarization)

    ori_data.update(adding_data)

    df = pd.DataFrame(ori_data)
    df.to_csv(file, index=False)


if __name__ == '__main__':
    # for i in range(0, 6):
    #     folder = f'G:\\光学数据\\part{i}'
    folder = r'G:\红外数据\part2'
    files = glob.glob(folder + '/*.csv')
    nproc = 8
    if nproc == 0:
        mmengine.track_progress(add_info, files)
    else:
        mmengine.track_parallel_progress(add_info, files, nproc=nproc)
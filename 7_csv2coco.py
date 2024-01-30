import glob
import os
import os.path as osp
import pandas as pd
from mmengine.fileio import dump
from mmengine.utils import (Timer, mkdir_or_exist, track_parallel_progress,
                            track_progress)

def load_img_info(csv_file):
    try:
        csv_data = pd.read_csv(csv_file)
    except:
        print(f'error in {csv_file}')
        return None
    num_annotations = 0
    if 'box' in csv_data.columns:
        num_annotations = len(csv_data['box'])
    if num_annotations == 1:
        if 'task_type' in csv_data.columns and csv_data['task_type'][0] == 'cls':
            return None
        if csv_data['box'][0] == '[]':
            num_annotations = 0

    anno_info = []
    category_id = 1
    for ann_id in range(num_annotations):
        l, b, r, t = eval(csv_data['box'][ann_id])
        anno = dict(
            iscrowd=0,
            category_id=category_id,
            bbox=[l, b, r - l, t - b],
            area=(r - l) * (t - b),
        )
        anno_info.append(anno)
    try:
        file_name = os.path.basename(os.path.dirname(csv_file)) + '/' + csv_data['img_name'][0]
    except:
        return None
    height, width = eval(csv_data['img_size'][0])
    img_info = dict(
        file_name=file_name,
        height=height,
        width=width,
        anno_info=anno_info
    )
    return img_info


def cvt_annotations(image_infos, out_json_name):
    out_json = dict()
    img_id = 0
    ann_id = 0
    out_json['images'] = []
    out_json['categories'] = []
    out_json['annotations'] = []
    for image_info in image_infos:
        image_info['id'] = img_id
        anno_infos = image_info.pop('anno_info')
        out_json['images'].append(image_info)
        for anno_info in anno_infos:
            anno_info['image_id'] = img_id
            anno_info['id'] = ann_id
            out_json['annotations'].append(anno_info)
            ann_id += 1
        img_id += 1

    cat = dict(id=1, name='ship')
    out_json['categories'].append(cat)

    if len(out_json['annotations']) == 0:
        out_json.pop('annotations')

    dump(out_json, out_json_name)
    return out_json


if __name__ == '__main__':
    folder = r'H:\红外XX数据\红外数据\part1'
    json_name = r'H:\红外XX数据\code\annotations.json'
    nproc = 32
    csv_files = []

    if 'part' in folder:
        csv_files += glob.glob(os.path.join(folder, '*.csv'))
    else:
        for i in range(1, 16):
            csv_files += glob.glob(os.path.join(folder, f'part{i}/*.csv'))

    if nproc > 1:
        image_infos = track_parallel_progress(load_img_info, csv_files, nproc=nproc)
    else:
        image_infos = track_progress(load_img_info, csv_files)
    print(f'load {len(image_infos)} images')
    image_infos = [img_info for img_info in image_infos if img_info is not None]
    print(f'after filter, {len(image_infos)} images')
    if not os.path.isabs(json_name):
        json_name = osp.join(folder, json_name)
    cvt_annotations(image_infos, json_name)

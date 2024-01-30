# Script to convert yolo annotations to voc format

# Sample format
# <annotation>
#     <folder>_image_fashion</folder>
#     <filename>brooke-cagle-39574.jpg</filename>
#     <size>
#         <width>1200</width>
#         <height>800</height>
#         <depth>3</depth>
#     </size>
#     <segmented>0</segmented>
#     <object>
#         <name>head</name>
#         <pose>Unspecified</pose>
#         <truncated>0</truncated>
#         <difficult>0</difficult>
#         <bndbox>
#             <xmin>549</xmin>
#             <ymin>251</ymin>
#             <xmax>625</xmax>
#             <ymax>335</ymax>
#         </bndbox>
#     </object>
# <annotation>
import os
import xml.etree.cElementTree as ET
from xml.dom import minidom

import mmcv
import pandas as pd
from PIL import Image
import glob
from mmengine import track_parallel_progress, track_progress


def create_file(voc_labels, save_path):

    # img tag
    root = ET.Element("annotations")
    ET.SubElement(root, "filename").text = voc_labels['img_name']
    ET.SubElement(root, "folder").text = voc_labels['img_dir']
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(voc_labels['width'])
    ET.SubElement(size, "height").text = str(voc_labels['height'])
    ET.SubElement(size, "depth").text = str(3)
    ET.SubElement(size, "area").text = str(voc_labels['width'] * voc_labels['height'])
    ET.SubElement(root, "segmented").text = str(0)
    ET.SubElement(root, "task_type").text = voc_labels['task_type']

    # box tag
    for voc_label in voc_labels['annotations']:
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = voc_label['name']
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = str(0)
        ET.SubElement(obj, "difficult").text = str(0)
        bbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bbox, "xmin").text = str(voc_label['box'][0])  # 'xmin', 'ymin', 'xmax', 'ymax
        ET.SubElement(bbox, "ymin").text = str(voc_label['box'][1])
        ET.SubElement(bbox, "xmax").text = str(voc_label['box'][2])
        ET.SubElement(bbox, "ymax").text = str(voc_label['box'][3])
        ET.SubElement(obj, "area").text = str((voc_label['box'][2] - voc_label['box'][0]) * (voc_label['box'][3] - voc_label['box'][1]))

    # 得到美化后的字符串，使用utf-8编码
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t", encoding='utf-8')
    xml_str = xml_str.decode('utf-8')
    # 保存xml文件
    with open(save_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_str)


def cvt_annotations(csv_file):
    try:
        csv_data = pd.read_csv(csv_file)
    except:
        print(f'{csv_file} is empty')
        return None

    try:
        img_path = os.path.join(os.path.dirname(csv_file), csv_data['img_name'][0])
    except Exception as e:
        print(e)
        img_path = csv_file.replace('.csv', '.jpg')
        if not os.path.exists(img_path):
            img_path = csv_file.replace('.csv', '.png')
        if not os.path.exists(img_path):
            img_path = csv_file.replace('.csv', '.jpeg')
        if not os.path.exists(img_path):
            img_path = csv_file.replace('.csv', '.bmp')
        if not os.path.exists(img_path):
            img_path = csv_file.replace('.csv', '.tif')
        if not os.path.exists(img_path):
            img_path = csv_file.replace('.csv', '.tiff')

    try:
        h, w = eval(csv_data['img_size'][0])
    except:
        h, w = mmcv.imread(img_path).shape[:2]

    voc_labels = {
        'img_dir': os.path.basename(os.path.dirname(csv_file)),
        'img_name': os.path.basename(img_path),
        'height': h,
        'width': w,
        'task_type': 'det',
        'annotations': []
    }

    if 'task_type' in csv_data.columns:
        try:
            if csv_data['task_type'][0] == 'cls':
                voc_labels['task_type'] = 'cls'
        except:
            pass
    for ann_id in range(len(csv_data['box'])):
        voc_ann = {
            'name': 'ship',
            'box': [],
        }
        if csv_data['box'][ann_id] == '[]':
            continue
        l, b, r, t = eval(csv_data['box'][ann_id])
        voc_ann['box'] = [l, b, r, t]
        voc_labels['annotations'].append(voc_ann)
    create_file(voc_labels, csv_file.replace('.csv', '.xml'))


if __name__ == "__main__":
    folder = r'G:\红外数据'
    nproc = 16
    csv_files = []
    for i in range(1, 16):
        csv_files += glob.glob(os.path.join(folder, f'part{i}/*.csv'))
    # csv_files += glob.glob(os.path.join(folder, f'*.csv'))
    print(f'load {len(csv_files)} images')
    # csv_files = csv_files[160000:]
    if nproc > 1:
        image_infos = track_parallel_progress(cvt_annotations, csv_files, nproc=nproc)
    else:
        image_infos = track_progress(cvt_annotations, csv_files)
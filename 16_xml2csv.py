import glob

import bs4
import pandas as pd
import tqdm

folder = r'H:\光学\hrsc2016\images'
files = glob.glob(folder+'/*.xml')

# place_dict = {
#     '100000001': 'Russia Murmansk(摩尔曼斯克港口)',
#     '100000002': 'America Everett(埃弗雷特)',
#     '100000003': 'America Newport-Rhode Island(罗德岛新港)',
#     '100000004': 'America Mayport Naval Base(梅波特海军基地)',
#     '100000005': 'America Norfolk Naval Base(诺福克海军基地)',
#     '100000006': 'America Naval Base San Diego(圣地亚哥海军基地)'
# }
#
# l2_dict = {
#     '100000001': 'ship',
#     '100000002': 'aircraft carrier',
#     '100000003': 'warcraft',
#     '100000004': 'merchant ship'
# }
# l32l2_dict = {'100000001': '', '100000002': '100000001', '100000003': '100000001', '100000004': '100000001', '100000005': '100000002', '100000006': '100000002', '100000007': '100000003', '100000008': '100000003', '100000009': '100000003', '100000010': '100000003', '100000011': '100000003', '100000012': '100000002', '100000013': '100000002', '100000014': '100000003', '100000015': '100000003', '100000016': '100000002', '100000017': '100000003', '100000018': '100000004', '100000019': '100000003', '100000020': '100000004', '100000022': '100000004', '100000024': '100000004', '100000025': '100000004', '100000026': '100000004', '100000027': '100000001', '100000028': '100000003', '100000029': '100000003', '100000030': '100000004', '100000031': '100000002', '100000032': '100000002', '100000033': '100000002'}
#
# l3_dict = {
#     '100000005': 'Nimitz class aircraft carrier',
#     '100000006': 'Enterprise class aircraft carrier',
#     '100000007': 'Arleigh Burke class destroyers',
#     '100000008': 'WhidbeyIsland class landing craft',
#     '100000009': 'Perry class frigate',
#     '100000010': 'Sanantonio class amphibious transport dock',
#     '100000011': 'Ticonderoga class cruiser',
#     '100000012': 'Kitty Hawk class aircraft carrier',
#     '100000013': 'Admiral Kuznetsov aircraft carrier',
#     '100000014': 'Abukuma-class destroyer escort',
#     '100000015': 'Austen class amphibious transport dock',
#     '100000016': 'Tarawa-class amphibious assault ship',
#     '100000017': 'USS Blue Ridge (LCC-19)',
#     '100000018': 'Container ship',
#     '100000019': 'OXo',
#     '100000020': 'Car carrier',
#     '100000022': 'Hovercraft',
#     '100000024': 'yacht',
#     '100000025': 'Container ship',
#     '100000026': 'Cruise ship',
#     '100000027': 'submarine',
#     '100000028': 'lute',
#     '100000029': 'Medical ship',
#     '100000030': 'Car carrier',
#     '100000031': 'Ford-class aircraft carriers',
#     '100000032': 'Midway-class aircraft carrier',
#     '100000033': 'Invincible-class aircraft carrier'
# }
# for file in tqdm.tqdm(files):
#     csv_data = {
#         'class1': [],
#         'class2': [],
#         'class3': [],
#         'box': [],
#         'place_id': [],
#         'img_date': [],
#         'img_location': [],
#         'resolution': [],
#         'img_custype': [],
#         'rotate_box_xywhtheta': [],
#     }
#     data = bs4.BeautifulSoup(open(file, encoding='utf-8'), 'xml')
#     objects = data.find_all('HRSC_Object')
#     for object in objects:
#         csv_data['place_id'].append(place_dict[data.find('Place_ID').text])
#         csv_data['img_date'].append(data.find('Img_Date').text)
#         csv_data['img_location'].append(data.find('Img_Location').text)
#         csv_data['resolution'].append(data.find('Img_Resolution').text)
#         csv_data['img_custype'].append(data.find('Img_CusType').text)
#         csv_data['class1'].append('ship')
#         cls_id = object.find('Class_ID').text
#         l3_cls = l3_dict.get(cls_id)
#         l2_cls = l2_dict.get(l32l2_dict.get(cls_id))
#         csv_data['class2'].append(l2_cls)
#         csv_data['class3'].append(l3_cls)
#         box = [object.find('box_xmin').text, object.find('box_ymin').text, object.find('box_xmax').text, object.find('box_ymax').text]
#         box = [float(i) for i in box]
#         csv_data['box'].append(box)
#         rotate_box = [object.find('mbox_cx').text, object.find('mbox_cy').text, object.find('mbox_w').text, object.find('mbox_h').text, object.find('mbox_ang').text]
#         rotate_box = [float(i) for i in rotate_box]
#         csv_data['rotate_box_xywhtheta'].append(rotate_box)
#
#     df = pd.DataFrame(csv_data)
#     df.to_csv(file.replace('.xml', '.csv'), index=False)







folder = r'H:\示例数据2\红外\真实'
files = glob.glob(folder+'/*.xml')

for file in tqdm.tqdm(files):
    csv_data = {
        'class1': [],
        'box': []
    }
    data = bs4.BeautifulSoup(open(file, encoding='utf-8'), 'xml')
    objects = data.find_all('object')
    for object in objects:
        csv_data['class1'].append('ship')
        box = [object.find('xmin').text, object.find('ymin').text, object.find('xmax').text, object.find('ymax').text]
        box = [float(i) for i in box]
        csv_data['box'].append(box)

    df = pd.DataFrame(csv_data)
    df.to_csv(file.replace('.xml', '.csv'), index=False)
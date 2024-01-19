import glob

import skimage
import tqdm

folder = r'H:\SAR\AIR-SARShip-1.0\images'
img_files = glob.glob(folder+'/*.tiff')
area_list = []
for img_file in tqdm.tqdm(img_files):
    img = skimage.io.imread(img_file)
    area = img.shape[0] * img.shape[1]
    area_list.append(area)
print('min area:', min(area_list))
print('max area:', max(area_list))
print ('min length:', min(area_list)**0.5)
print ('max length:', max(area_list)**0.5)
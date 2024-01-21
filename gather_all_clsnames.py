import glob
import pandas as pd
import tqdm

folder = r'G:\SAR数据\part15'
files = glob.glob(folder + '/*.csv')
cls_names = set()
for file in tqdm.tqdm(files):
    df = pd.read_csv(file)
    try:
        names = df['class2'].unique()
    except:
        continue
    # remove nan
    names = [x for x in names if x == x]
    cls_names.update(set(names))
print(cls_names)

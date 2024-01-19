import glob

import pandas as pd
import tqdm

def add_shipname(csv_file, ship_names, class_name='class1'):
    for file in tqdm.tqdm(files):
        data = pd.read_csv(file)
        for idx, row in data.iterrows():
            ship_name = row[class_name]
            ship_names.add(ship_name)
    return ship_names

ship_names = set()
folder = r'H:\optimal\FGSC-23\images\*.csv'
files = glob.glob(folder)
ship_names = add_shipname(files, ship_names)
folder = r'H:\optimal\FGSCR-42\images\*.csv'
files = glob.glob(folder)
ship_names = add_shipname(files, ship_names)
folder = r'H:\optimal\hrsc2016\images\*.csv'
files = glob.glob(folder)
ship_names = add_shipname(files, ship_names, 'class3')
folder = r'H:\optimal\ShipRSImageNet\images\*.csv'
files = glob.glob(folder)
ship_names = add_shipname(files, ship_names)
[print(x) for x in ship_names]




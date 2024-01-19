import pandas as pd

csv_file = r"H:\xviews\validation.csv"
data = pd.read_csv(csv_file)
split_data = dict()
for idx, row in data.iterrows():
    img_name = row['detect_id'].split('_')[0]
    row['class1'] = 'ship'

    split_data[img_name] = row

    if img_name not in split_data:
        split_data[img_name] = []
    split_data[img_name].append(row)
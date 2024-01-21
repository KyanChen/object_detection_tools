import glob
import os

import mmengine
import numpy as np
import pandas as pd

def check_and_delete(file):
    try:
        ori_data = pd.read_csv(file)
    except:
        print(file)
        # remove csv
        os.remove(file)
        # remove jpg
        os.remove(file.replace('.csv', '.jpg'))



if __name__ == '__main__':
    for i in range(2, 4):
        folder = f'G:\\光学数据\\part{i}'
        files = glob.glob(folder + '/*.csv')
        nproc = 16
        if nproc == 0:
            mmengine.track_progress(check_and_delete, files)
        else:
            mmengine.track_parallel_progress(check_and_delete, files, nproc=nproc)
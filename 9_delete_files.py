import glob
import os
import tqdm
import mmengine

def delete_file(file):
    os.remove(file)

if __name__ == '__main__':
    folder = r'G:\红外数据\完整数据\*\*\*\*'
    files = folder + '/.*'
    nproc = 16
    files = glob.glob(files)
    mmengine.track_parallel_progress(delete_file, files, nproc=nproc)


import glob
import os
import tqdm
import mmengine

def delete_file(file):
    os.remove(file)

if __name__ == '__main__':
    folder = r'G:\SAR数据\part13'
    files = folder + '/*' + '.txt'
    nproc = 16
    files = glob.glob(files)
    mmengine.track_parallel_progress(delete_file, files, nproc=nproc)


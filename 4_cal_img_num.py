import glob

folder = r'G:\红外数据'
files = glob.glob(folder + '/*/*.csv')
print(len(files))
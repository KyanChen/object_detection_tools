import glob

folder = r'G:\SAR数据'
files = glob.glob(folder + '/*/*.csv')
print(len(files))
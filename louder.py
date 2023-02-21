import os
import re
from glob import glob

SUFFIX_LIST = ['.mkv', '.mp4', '.mov']

if __name__ == '__main__':
    tmp = input("Type video directory:")
    if tmp == '':
        OUTPUT_DIR = '/project/ta-shared-ii/video-handel-compress/out_louder'
    else:
        OUTPUT_DIR = tmp
    tmp = input('New volume: (standard volume is 256)')
    if tmp == '':
        VOL = 2048
    else:
        VOL = tmp


    print('-----List all files from DATA_DIR with suffix in SUFFIX_LIST')
    SUFFIX_LIST = ['.mkv', '.mp4', '.mov']
    all_files = glob(OUTPUT_DIR+'/*.*')
    vfiles = []
    for f in all_files:
        if re.findall(fr'{"|".join(SUFFIX_LIST)}',f):
            vfiles.append(f)
    
    chapters = list(
        map(
            lambda x: x.split('/')[-1][:-4],
            vfiles
        )
    )

    print('Producing start:')
    for vfname, ch in zip(vfiles, chapters):
        os.system(f'ffmpeg -i {vfname} -vol {VOL} {OUTPUT_DIR}/{ch}_louder{vfname[-4:]}')

import os
import re
from glob import glob

import moviepy.editor as mpy  # for title clip
import ffmpeg  # watermark, concatenate (w/ for fade-in, out), produce output

SUFFIX_LIST = ['.mkv', '.mp4', '.mov']

if __name__ == '__main__':
    tmp = input("Type video directory:")
    if tmp == '':
        DATA_DIR = '/project/ta-shared-ii/video-handel-compress/data'
    else:
        DATA_DIR = tmp

    tmp = input("Type output directory:")
    if tmp == '':
        OUTPUT_DIR = '/project/ta-shared-ii/video-handel-compress/output'
    else:
        OUTPUT_DIR = tmp

    print('-----Create temperary folder and output folder')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs('tmp',exist_ok=True)
    TMP_DIR = 'tmp'

    print('-----List all files from DATA_DIR with suffix in SUFFIX_LIST, find their title picture in ".png" format')
    SUFFIX_LIST = ['.mkv', '.mp4', '.mov']
    all_files = glob(DATA_DIR+'/*.*')
    vfiles = []
    for f in all_files:
        if re.findall(fr'{"|".join(SUFFIX_LIST)}',f):
            vfiles.append(f)
    tfiles = list(
        map(
            lambda x: re.sub(f'{"|".join(SUFFIX_LIST)}', '.png', x),
            vfiles
        )
    )

    chapters = list(
        map(
            lambda x: x.split('/')[-1][:-4],
            vfiles
        )
    )

    print('Create title films')
    # Prepare dummy audio file
    make_frame = lambda t: 0.0
    dummy_audio = mpy.AudioClip(make_frame, duration=3.5, fps=44100) 
    # Start making title films
    tmp_filename = []
    for f, ch in zip(tfiles, chapters):
        # Title clip
        tmp_filename.append(f'{TMP_DIR}/{ch}_title.mkv')
        if not os.path.exists(tmp_filename[-1]):
            tclip = mpy.ImageClip(f, duration=3.5)
            tclip = tclip.set_audio(dummy_audio)
            tclip.write_videofile(tmp_filename[-1], codec='libx264', fps=30, bitrate='2500K')

    print('Producing start:')
    for tfanme, vfname, ch in zip(tmp_filename, vfiles, chapters):
        # Set input files
        t_in = ffmpeg.input(tfanme)
        v_in = ffmpeg.input(vfname)
        wm_in = ffmpeg.input(DATA_DIR+'/watermark.png')

        # Add water mark to main video
        fused = ffmpeg.overlay(v_in.video, wm_in)

        # Add title clip
        joined = ffmpeg.concat(t_in.video.filter_('fade', t='out', st=3.0, d=0.5),
                               t_in.audio,
                               fused.filter_('fade', t='in', st=0, d=0.5),
                               v_in.audio,
                               v=1, a=1)
        # Run Production
        out = ffmpeg.output(joined, f'{OUTPUT_DIR}/{ch}.mp4',r=30)
        out.run()
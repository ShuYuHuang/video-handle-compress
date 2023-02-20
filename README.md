# video-handle-compress
Video batch editing for AIA courses clips: add watermark, add title, compress

AIAers, this is your blessing~~

Lets automate the process of your course video:

1. Add watermark to the clip (ffmpeg-python)
2. Add title page to the front (MoviePy)
3. Compress and export to mp4 with framerate = 30 fps (ffmpeg-python)

## Installation
Star, fork and git clone this repo:
> ```git clone https://github.com/ShuYuHuang/video-handle-compress.git```

Install requirements with the following command:
> ```pip install -r requirements.txt```

## Usage
Please proceed your batch production with the folloings:
1. Start the main program:
> ```python produce.py```
2. Enter the file path, e.g. ```data```
```
Please have the folder organized like this
root/
    - XXX.mkv(/.mov/.mp4/..., the recorded clip)
    - XXX.png (the corresponding title picture, please follow the template we made)
    - YYY.mkv
    - YYY.png
    - watermark.png (the watermark file to print on each frame)
```
3. Enter the output path, e.g. ```out```
4. Wait for 10 minutes for each file
5. Get your files in the output path and put that to youtube
6. You can further transcribe the films by [Whisper-Subtitle](https://github.com/ShuYuHuang/whisper-subtitle)

All the tryout notebooks are in ```experiments```

## References
* PyMovie: https://zulko.github.io/moviepy/getting_started/videoclips.html
* FFMPEG-python: https://github.com/kkroening/ffmpeg-python
* FFMPEG fade-in: https://dev.to/dak425/add-fade-in-and-fade-out-effects-with-ffmpeg-2bj7#:~:text=Using%20ffmpeg%2C%20you%20can%20apply,to%20achieve%20a%20similar%20effect.&text=This%20will%20start%20the%20video,full%20view%20over%203%20seconds.
* https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md
* https://dev.to/dak425/add-fade-in-and-fade-out-effects-with-ffmpeg-2bj7

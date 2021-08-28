FROM_YOUTUBE_DOCS = '''
downloads the video from the given YouTube `url` \
and uses frames from that video to create a photo mosaic \
of the given `image_path` image
'''


FROM_VIDEO_DOCS = '''
uses frames from the given `video_path` video \
to create a photo mosaic of the given `image_path` image
'''


FROM_FOLDER_DOCS = '''
uses images from the `folder_path` folder to create a photo mosaic \
of the given `image_path` image
'''


RICKROLL_DOCS = '''
funny shortcut for\n

```py
mozaiku.from_youtube(
    url = 'https://youtu.be/dQw4w9WgXcQ',
    *args
)
```
'''

doc = '''
## Required Parameters

- `url`:\n
    - the url of the YouTube video to download
- `image_path`:\n
    - the path of the input image, which will become a mosaic
- `output_file_name`:\n
    - the path where the mosaic output will be saved
- `image_max_size`:\n
    - the number of small images \
that will be on the longest side of the input image
- `frames_size`:\n
    - the size of the small images in pixel

## Optional Parameters

- `folder_path`:\n
    - how the folder containing the frames will be called
- `fps`:\n
    - how many frames of each second of the video will be extracted
- `log`:\n
    - whether the program will print when each step starts and finishes or not
- `compression_level`:\n
    - the level of compression used when saving the final image
- `show_progress_bar`:\n
    - whether a progress bar is shown for the last three steps or not. \
    this can affect the speed of the program
- `clear`:\n
    - whether temporary files will be deleted or not
'''
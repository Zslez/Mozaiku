from shutil         import rmtree
from PIL            import Image
from subprocess     import run

from .mosaic        import MOSAIC

from .speed         import *
from .utils         import *

from . import utils

import os



__all__ = [
    'from_youtube',
    'from_video',
    'from_folder',
    'rickroll',
    'MOSAIC',

    'utils'
]



## =============== VARIABLES =============== ##



supports_transparency = [
    'png',
    'gif' # add others, idk
]



## =============== FUNCTIONS =============== ##



def from_youtube(
        url: str,
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        folder_path: str = 'frames',
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0)
    ) -> Image:
    '''
    downloads the video from the given YouTube `url` \
    and uses frames from that video to create a photo mosaic \
    of the given `image_path` image

    ## Required Parameters

    - `url`:\n
      - the url of the YouTube video to download
    - `image_path`:\n
      - the path of the input image, \
    which will become a mosaic
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
      - whether the program will print when each step \
    starts and finishes or not
    - `compression_level`:\n
      - the level of compression used when saving the final image
    - `show_progress_bar`:\n
      - whether a progress bar is shown for the last three steps or not. \
        this can affect the speed of the program
    - `clear`:\n
      - whether temporary files will be deleted or not. \
    those files include the video downloaded and the folder of frames
    '''

    mosaic = MOSAIC(
        url = url,
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        folder_path = folder_path,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_youtube()



def from_video(
        video_path: str,
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        folder_path: str = 'frames',
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0)
    ) -> Image:
    '''
    uses frames from the given `video_path` video \
    to create a photo mosaic of the given `image_path` image

    ## Required Parameters

    - `url`:\n
      - the url of the YouTube video to download
    - `image_path`:\n
      - the path of the input image, \
    which will become a mosaic
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
      - whether the program will print when each step \
    starts and finishes or not
    - `compression_level`:\n
      - the level of compression used when saving the final image
    - `show_progress_bar`:\n
      - whether a progress bar is shown for the last three steps or not. \
        this can affect the speed of the program
    - `clear`:\n
      - whether temporary files will be deleted or not, \
        such as the downloaded video
    '''

    mosaic = MOSAIC(
        video_path = video_path,
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        folder_path = folder_path,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_video()



def from_folder(
        folder_path: str,
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0),
        frames_are_already_squares: bool = False
    ) -> Image:
    '''
    uses images from the `folder_path` folder to create a photo mosaic \
    of the given `image_path` image

    ## Required Parameters

    - `folder_path`:\n
      - how the folder containing the frames will be called
    - `image_path`:\n
      - the path of the input image, \
    which will become a mosaic
    - `output_file_name`:\n
      - the path where the mosaic output will be saved
    - `image_max_size`:\n
      - the number of small images \
    that will be on the longest side of the input image
    - `frames_size`:\n
      - the size of the small images in pixel

    ## Optional Parameters

    - `fps`:\n
      - how many frames of each second of the video will be extracted
    - `log`:\n
      - whether the program will print when each step \
    starts and finishes or not
    - `compression_level`:\n
      - the level of compression used when saving the final image
    - `show_progress_bar`:\n
      - whether a progress bar is shown for the last three steps or not. \
        this can affect the speed of the program
    - `clear`:\n
      - whether temporary files will be deleted or not
    '''

    mosaic = MOSAIC(
        folder_path = folder_path,
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_folder(frames_are_already_squares)



def rickroll(
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        folder_path: str = 'frames',
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0)
    ) -> Image:
    '''
    funny shortcut for\n

    ```py
    mozaiku.from_youtube(
        url = 'https://youtu.be/dQw4w9WgXcQ',
        *args
    )
    ```

    ## Required Parameters

    - `url`:\n
      - the url of the YouTube video to download
    - `image_path`:\n
      - the path of the input image, \
    which will become a mosaic
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
      - whether the program will print when each step \
    starts and finishes or not
    - `compression_level`:\n
      - the level of compression used when saving the final image
    - `show_progress_bar`:\n
      - whether a progress bar is shown for the last three steps or not. \
        this can affect the speed of the program
    - `clear`:\n
      - whether temporary files will be deleted or not. \
    those files include the video downloaded and the folder of frames
    '''

    mosaic = MOSAIC(
        url = 'https://youtu.be/dQw4w9WgXcQ',
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        folder_path = folder_path,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_youtube()



## ================= CLEAR ================= ##



del os
del run
del rmtree

del Image

for i in utils.__all__:
    del globals()[i]

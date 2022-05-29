from PIL        import Image

from .mosaic    import MOSAIC

from .utils     import *
from .__doc     import *

from .          import utils



__all__ = [
    'from_youtube',
    'from_video',
    'from_folder',
    'rickroll',
    'MOSAIC',

    'utils'
]



## =============== DOC FUNC =============== ##



def __docs(string_before):
    def deco(func):
        func.__doc__ = string_before + doc
        return func

    return deco



## =============== FUNCTIONS =============== ##



@__docs(FROM_YOUTUBE_DOCS)
def from_youtube(
        url: str,
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        folder: str = 'frames',
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0)
    ) -> Image:

    mosaic = MOSAIC(
        url = url,
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        folder = folder,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_youtube()



@__docs(FROM_VIDEO_DOCS)
def from_video(
        video_path: str,
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        folder: str = 'frames',
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0)
    ) -> Image:

    mosaic = MOSAIC(
        video_path = video_path,
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        folder = folder,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_video()



@__docs(FROM_FOLDER_DOCS)
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



@__docs(RICKROLL_DOCS)
def rickroll(
        image_path: str,
        output_file_name: str,
        image_max_size: int,
        frames_size: int,

        fps: int = 3,
        log: bool = True,
        clear: bool = True,
        folder: str = 'frames',
        compression_level: int = 6,
        show_progress_bar: bool = False,
        replace_transparent: tuple = (0, 0, 0, 0)
    ) -> Image:

    mosaic = MOSAIC(
        url = 'https://youtu.be/dQw4w9WgXcQ',
        image_path = image_path,
        output_file_name = output_file_name,
        image_max_size = image_max_size,
        frames_size = frames_size,

        fps = fps,
        log = log,
        clear = clear,
        folder = folder,
        compression_level = compression_level,
        show_progress_bar = show_progress_bar,
        replace_transparent = replace_transparent
    )

    return mosaic.from_youtube()



@__docs(SAMPLE_DOCS)
def sample(
        image_path: str,
        output_file_name: str,
        sample_image: str,

        log: bool = True,
        clear: bool = True,
        folder: str = 'frames',
        compression_level: int = 6,
        replace_transparent: tuple = (0, 0, 0, 0)
    ):
    import os

    if not os.path.exists(image_path):
        print(f'No such file or directory: \'{image_path}\'')
        raise FileNotFoundError

    im = Image.open(image_path)
    image_max_size = max(im.size)
    im.close()

    mosaic = MOSAIC(
        image_path = image_path,
        output_file_name = output_file_name,
        sample_image = sample_image,
        image_max_size = image_max_size,
        frames_size = 1,

        log = log,
        clear = clear,
        folder = folder,
        compression_level = compression_level,
        replace_transparent = replace_transparent
    )

    del os

    return mosaic.from_image()



## ================= CLEAR ================= ##



for i in utils.__all__:
    del globals()[i]

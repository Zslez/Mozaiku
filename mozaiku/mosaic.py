from distutils.dir_util import copy_tree
from subprocess         import run
from PIL                import Image

from .utils              import *

import shutil
import os



__all__ = [
    "MOSAIC"
]



## =============== MAIN CLASS =============== ##



class MOSAIC:
    def __init__(
            self,
            image_path: str,
            output_file_name: str,
            image_max_size: int,
            frames_size: int,

            url: str = None,
            video_path: str = None,
            folder_path: str = 'frames',

            fps: int = 3,
            log: bool = True,
            clear: bool = True,
            compression_level: int = 6,
            show_progress_bar: bool = False,
            replace_transparent: tuple = (0, 0, 0, 0)
        ) -> None:

        # Required Parameters

        self.image_path = image_path
        self.output_file_name = output_file_name
        self.image_max_size = image_max_size
        self.frames_size = frames_size

        # Optional Parameters

        self.url = url
        self.video_path = video_path
        self.folder_path = folder_path

        self.fps = fps
        self.log = log
        self.clear = clear
        self.compression_level = compression_level
        self.show_progress_bar = show_progress_bar

        # Other Variables

        self.size = None
        self.result = None
        self.new_size = None
        self.list_of_colours = None
        self.new_image_colours = None

        self.to_clear = [] if clear else None

        self.type = ['RGB', 'RGBA'][
            len(replace_transparent) == 4 and
            self.image_path.split('.')[-1] in ['png', 'gif']
        ]

        self.replace_transparent = replace_transparent[:len(self.type)]



    def from_youtube(self) -> Image:
        '''
        downloads the video from the given YouTube `self.url` \
        and uses frames from that video to create a photo mosaic \
        of the given `image_path` image
        '''

        self.video_path = self.get_first_available('video', 'mp4')

        if self.clear:
            self.to_clear.append(self.video_path)

        log_func(self, self.download_video, 'Downloading video...')

        return self.from_video()



    def from_video(self) -> Image:
        '''
        uses frames from the given `video_path` video \
        to create a photo mosaic of the given `image_path` image
        '''

        self.folder_path = self.get_first_available(self.folder_path, '')
        os.mkdir(self.folder_path)

        if self.clear:
            self.to_clear.append(self.folder_path)

        log_func(self, self.extract_frames, 'Extracting frames...')

        return self.from_folder()



    def from_folder(self, frames_are_already_squares: bool = False) -> Image:
        '''
        uses images from the `self.folder_path` folder to create \
        a photo mosaic of the `self.image_path` image

        ## Optional Parameter
        - `frames_are_already_squares`:\n
          - skip the step of cropping all frames to square
        '''

        log_func(self, self.get_frames, 'Selecting valid frames...', frames_are_already_squares)

        log_func(self, self.generate_new_image, 'Generating list of images...')

        img = log_func(self, self.create_mosaic, 'Creating mosaic...')

        if self.clear:
            self.clear_files(self.to_clear + [self.folder_path])

        return img



    def extract_frames(self) -> None:
        '''
        uses `ffmpeg` to extract frames from the `self.video_path` video
        '''

        run(
            f'ffmpeg -hide_banner -loglevel error' + \
            ['', ' -stats'][self.log] + \
            f' -i {self.video_path}' \
            f' -r {self.fps} {self.folder_path}/out-%06d.jpg',
            shell = True,
            check = True
        )



    def download_video(self) -> None:
        run(
            f'youtube-dl -o "{self.video_path}" -f best {self.url}',
            shell = True,
            check = True
        )



    def get_frames(self, frames_are_already_squares: bool = False) -> None:
        '''
        saves the average color of all frames in `self.folder_path` \
        skipping duplicates, and resizes and crop the frames

        ## Optional Parameter
        - `frames_are_already_squares`:\n
          - skip the step of cropping all frames to square
        '''

        count = 1

        result = {0: self.replace_transparent}
        values = [self.replace_transparent]

        new_folder = self.get_first_available(self.folder_path, '')
        os.mkdir(new_folder)

        frames = os.listdir(self.folder_path)

        progress_bar = progress_bar_func(len(frames), self.show_progress_bar)

        for i in frames:
            with Image.open(self.folder_path + '/' + i) as image:
                width, height = image.size
                new = min(width, height)

                left    = (width  - new) / 2
                top     = (height - new) / 2
                right   = (width  + new) / 2
                bottom  = (height + new) / 2

                if not frames_are_already_squares:
                    image = image.crop(
                        (left, top, right, bottom)
                    ).resize(
                        (self.frames_size, self.frames_size)
                    )

                    image.save(new_folder + '/' + i)
                else:
                    copy_tree(self.folder_path, new_folder)

                res = image.resize((1, 1)).getdata()[0]

                if len(res) == 3 and self.type == 'RGBA':
                    res += (255,)

                if res not in values:
                    values.append(res)
                    result[count] = res

                count += 1
            progress_bar.update()

        progress_bar.end()

        self.size = image.size[0]
        self.result = result
        self.list_of_colours = result.values()

        self.folder_path = new_folder



    def generate_new_image(self) -> None:
        '''
        something
        '''

        image = Image.open(self.image_path).convert(self.type)

        max_size = self.image_max_size / max(image.size)

        self.new_size = (int(image.size[0] * max_size), int(image.size[1] * max_size))

        image = image.resize(self.new_size)

        data = image.getdata()
        closest = {}

        self.new_image_colours = []

        progress_bar = progress_bar_func(len(data), self.show_progress_bar)

        for i in data:
            if i[-1] == 0:
                self.new_image_colours.append(self.replace_transparent)
            else:
                if i not in closest:
                    closest[i] = self.get_closest_colour(self.list_of_colours, i)

                self.new_image_colours.append(closest[i])

            progress_bar.update()

        progress_bar.end()



    def get_closest_colour(
            self,
            colours: list,
            colour: tuple
        ) -> tuple:
        '''
        returns an `(r, g, b)` tuple of the closests colour \
        to the given `colour` from a given list of `colours`
        '''

        min_diff = 1000000
        final_colour = 0

        red, green, blue = colour[:3]

        for i in colours:
            i_red, i_green, i_blue = i[:3]

            diff_1, diff_2, diff_3 = red - i_red, green - i_green, blue - i_blue
            colour_diff = diff_1 * diff_1 + diff_2 * diff_2 + diff_3 * diff_3

            if colour_diff < min_diff:
                min_diff = colour_diff
                final_colour = i

        return final_colour



    def get_first_available(
            self,
            file_name: str,
            ext: str,

            sep: str = '_',
            start_num: int = 1,
            format_digits: int = 1,
            check_without: bool = True
        ) -> str:
        '''
        something
        '''

        ext = '.' + ext if ext else ext

        *folder, file_name = file_name.replace('\\', '/').split('/')
        folder = '/'.join(folder)

        if folder:
            folder += '/'
            files = os.listdir(folder)
        else:
            files = os.listdir()

        if check_without:
            if file_name + ext not in files:
                return folder + file_name + ext

        count = start_num
        num = str(count).zfill(format_digits)
        file_name_count = file_name + sep + num + ext

        while file_name_count in files:
            count += 1
            num = str(count).zfill(format_digits)
            file_name_count = file_name + sep + num + ext

        return folder + file_name_count



    def create_mosaic(self) -> Image:
        '''
        creates the final image pasting all \
        the valid frames from `self.new_image_colours`
        '''

        key, val = list(self.result), list(self.result.values())
        files = os.listdir(self.folder_path)

        new_im = Image.new(
            self.type,
            self.get_output_size(),
            self.replace_transparent
        )


        used_images = [self.replace_transparent]

        progress_bar = progress_bar_func(
            len(self.new_image_colours),
            self.show_progress_bar
        )

        for i in self.new_image_colours:
            if i not in used_images:
                used_images.append(i)

                # I use .index because I know all values are different

                img = Image.open(f'{self.folder_path}/{files[key[val.index(i) - 1]]}').convert(self.type)

                places = [j for j in range(len(self.new_image_colours)) if self.new_image_colours[j] == i]

                for k in places:
                    new_im.paste(
                        img,
                        (
                            (k % self.new_size[0]) * self.size,
                            (k // self.new_size[0]) * self.size
                        )
                    )

                img.close()

            progress_bar.update()

        new_im.save(
            self.get_first_available(
                '.'.join(self.output_file_name.split('.')[:-1]),
                self.output_file_name.split('.')[-1]
            ),
            compression_level = self.compression_level
        )

        progress_bar.end()

        return new_im



    def clear_files(self, files: list):
        for i in files:
            try:
                os.remove(i)
            except PermissionError:
                shutil.rmtree(i, ignore_errors = True)



    def get_output_size(self):
        return (self.size * self.new_size[0], self.size * self.new_size[1])

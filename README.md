# Za Mozaiku - ザ・モザイク

![Logo](https://raw.githubusercontent.com/Zslez/Mozaiku/master/images/logo_preview.png)

## About

`Za Mozaiku` can create a **photo mosaic** of an image, using a **YouTube url**, a **video** or a **folder of images**.  
Although it may be slow depending on various things, such as the size of the output image, the number of steps or the length of the video, it’s really easy to use.

## Installation

to install only the `mozaiku` package run in your terminal

```bash
pip install mozaiku
```

if you need also `youtube-dl` features install it running the command

```bash
pip install -U youtube-dl
```

To install `ffmpeg` you can go to [this page](https://ffmpeg.org/download.html) and download it there, however if you're **not** on Windows, you should be able to install it using your package manager in your terminal.

## How the program works

**NOTE**:

* `mozaiku.from_video()` skips step 1
* `mozaiku.from_folder()` skips step 1 and 2

**STEPS**:

1. **DOWNLOAD VIDEO**

> using `youtube-dl`, it downloads the video from the given YouTube url

2. **EXTRACT FRAMES**

> using `ffmpeg`, it splits the video from `step 1` into all its frames, using the given `fps` value as frame rate, and saves those frames in a folder

3. **GET NEEDED FRAMES**

> it loops through all the frames in the folder, resizes them according to the `frames_size` value, crops them to square, and saves their average color in a dictionary removing duplicates

4. **GENERATE NEW IMAGE STRUCTURE**

> it opens the input image and resizes it according to the `image_max_size` value, then it loops through each pixel and gets the closest color to the pixel color, among those saved in the dict from `step 4`, and save those color in a list

5. **CREATE MOSAIC**

> it gets, from the folder of frames, the frames corresponding to the colours saved in the list from `step 5`, and places those frames in a new big image

## Example

> The only purpose of this example is to make you note how the result may vary depending on the dominant colours of the video, as probably, using this kind of super-colourful images is not the best thing to do with this program.  
In fact, you can see that the logo mosaic at the top of this file is so similar to the original image that the difference between the colours is irrelevant.

![Logo Comparison](https://raw.githubusercontent.com/Zslez/Mozaiku/master/images/comparison.png)

Now the example.

INPUT IMAGE

[![Colours](https://raw.githubusercontent.com/Zslez/Mozaiku/master/images/colours_small.jpg)](https://raw.githubusercontent.com/Zslez/Mozaiku/master/images/colours.jpg)

CODE 1

```py
import mozaiku

mozaiku.from_youtube(
    'https://www.youtube.com/watch?v=iCnbgXyU09c',
    'colours.jpg',
    'colours_mosaic_1.jpg',
    image_max_size = 200,
    frames_size = 200
)
```

> Assuming the frames are bigger than `200x200`, the output mosaic will have the biggest side equal to `image_max_size * frames_size`, in this example `40000`.  
So here the output image is `40000x24000`

> NOTE: I can't show the real image cause it's too big for GitHub, these are resized.

OUTPUT IMAGE 1

![Colours](https://raw.githubusercontent.com/Zslez/Mozaiku/master/images/colours_mosaic_small_1.jpg)

CODE 2

```py
import mozaiku

mozaiku.from_youtube(
    'https://www.youtube.com/watch?v=OMa9bTd2qi0',
    'colours.jpg',
    'colours_mosaic_2.jpg',
    200,
    200
)
```

OUTPUT IMAGE 2

![Colours](https://raw.githubusercontent.com/Zslez/Mozaiku/master/images/colours_mosaic_small_2.jpg)

## Checklist

I add inside `[]` two values between `0` and `5`.  
The first is how much I think the task is difficul, whereas the second is the level of priority of the task.

This is also to help those who wants to contribute choose what to do.

* **Additional Tools**
  * [ ] `[4.0, 3.5]` Mozaiku **CLI**
  * [ ] `[2.5, 0.5]` Mozaiku **Telegram Bot**
* **Tests**
  * [ ] `[1.5, 4.0]` [Test](#tests) the program on a **Linux** system
  * [ ] `[1.5, 3.5]` [Test](#tests) the program on a **MacOS** system
* **Improvements**
  * [ ] `[2.5, 4.5]` Improve program efficiency using **threads** or **asynchronous functions**

## Tests

If you want to test this program on other operating systems or with other versions of Python, you have to make sure every function **works**, is able to **print log** and **progress bar**and is able to **delete temporary files**.  

Currently tested on:

* **Windows 10 Home 20H2**
  * Python Versions Tested
    * `3.8.6`

## Contributing

If you want to contribute to this project I’d recommend having a look at [open issues](https://github.com/Zslez/Mozaiku/issues) if there are any, or at the [checklist](#checklist).  
Otherwise **any kind** of improvement or suggestion is welcome, from **improving an entire algorithm** to **correcting even a typo**, **improving comprehensibility** of function docs or **this README file**.

## Sources

The idea of a video to mosaic project is completely mine* and so is also the main algorithm, however I had to look up some stuff, like [how to split a video into frames](https://stackoverflow.com/a/3917648), [how to get the closest color](https://stackoverflow.com/a/54242348) and [how to merge images](https://stackoverflow.com/a/30228308).  
Thanks to all of you random guys who faced these problems before me.

<sub><sup>\* I didn’t know whether a similar thing already existed or not, and I created it without looking at similar projects and without anyone asking for it</sup></sub>

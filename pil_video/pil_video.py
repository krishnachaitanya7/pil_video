"""The main use of this code is to play a numpy video. Someething quick that can be used in day to day life. 
But having a numpy array to play isn't enough. Usually people using many different formats, which I don't wanna get into
So I ask to input an PIL images list, which then I am gonna make a video out of. I will be working out of /tmp
directory, and I will be deleteing everything after I play a video for you. Finally I tried not to include any
opencv imports, as it has lot of problems with Py2.7 and Py3.7 and many weird errors. So tried to use pure
python imports as much as possible.
"""
import os
from PIL import Image  # noqa
import tempfile
import shutil
import imageio


def make_video(image_list: list, fps: int, delete_folder=True, play_video=True):
    """The main def for creating a temporary video out of the 
    PIL Image list passed, according to the FPS passed
    Parameters
    ----------
    image_list : list
        A list of PIL Images in sequential order you want the video to be generated
    fps : int
        The FPS of the video
    delete_folder : bool, optional
        If set to False, this will not delete the temporary folder where images and video are saved, by default True
    play_video : bool, optional
        If set to false, the video generated will not be played, by default True
    """
    # Make an empty directort in temp, which we are gonna delete later
    dirpath = tempfile.mkdtemp()  # Example: '/tmp/tmpacxadh7t'
    video_filenames = []
    for i, each_image in enumerate(image_list):
        # TODO: Correct the below snippet
        # if not isinstance(each_image, type(Image)):
        #     raise Exception("The element is not an PIL Image instance")
        filename = "{}/{}.png".format(dirpath, i)
        video_filenames.append(filename)
        each_image.save("{}".format(filename))
    writer = imageio.get_writer("{}/test.mp4".format(dirpath), fps=fps)
    for each_image in video_filenames:
        writer.append_data(imageio.imread(each_image))
    writer.close()
    if play_video:
        os.system("vlc {}/test.mp4 vlc://quit".format(dirpath))
    if delete_folder:
        shutil.rmtree(dirpath)
    else:
        print("Find your images and video at {}".format(dirpath))

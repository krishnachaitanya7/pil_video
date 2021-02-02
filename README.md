# pil_video
![PyPi](https://github.com/krishnachaitanya7/pil_video/workflows/PyPi/badge.svg)
![PyPi](https://github.com/krishnachaitanya7/pil_video/workflows/Flake8%20Status/badge.svg)

This is a python package. 

The main use of this code is to play a numpy video. Something quick that can be used in day to day life as a 
Deep learning and robotics researcher.

But having a numpy array to play isn't enough. Usually, people using many different formats, which I don't wanna get into.

So I ask to input a PIL images list, which then I am gonna make a video out of. I will be working out of /tmp
directory, and I will be deleting everything after I play a video for you. Finally I tried not to include any
opencv imports, as it has lots of problems with Py2.7 and Py3.7 and many weird errors. So I tried to use pure
python imports as much as possible so that this can be run out of virtual environments.

Finally, please don't forget to install VLC media player for this to work.

## Advantages of using this in place of Matplotlib
When you have to loop through 2K images, it's usually not possible with Matplotlib. It's usually slow. At that time usually you have to save the images and then make a video out of it. Problem is if you want to do it multiple times,
it can be a hassle. Matplotlib is good if you wanna loop through 50 images, but anything more than that can be an issue. But if you use this Python package, it will show you the video at a specific FPS you want and also give a temporary path if needed. That way there is no hassle of saving anything and once you visualize whatever you want it will be discarded or kept if the user wants to.

## Installation
From 

> pip install pil-video

From Github: 

> pip install --upgrade git+https://github.com/krishnachaitanya7/pil_video.git

Also, you need to have VLC media player installed beforehand. You can do that by:

> sudo apt-get install vlc

## Notes for myself
when you do pip show PACKAGE_NAME, it will show you the exact location of your package from where it's importing
But many times that might not be enough. So go to python console, and import the package and enter package_name.__file__, this will output exact path. Sometimes it might be an egg file, so you might wanna consider looking into that egg file. If it's just a directory then also it's good to go. When I was testing and I wanted to uninstall and 
I wasn't sure where it was, this helped me. My package was in egg format, so I was unable to find the folder, because it was in an egg. Be careful.

## Usage
```python
from pil_video import make_video
"""
Make a list of PIL Images in the sequence you want to make a video, let's say 
you made a list named test
"""
# First argument is the list comprising of PIL images
# second argument is the FPS of the video you want generated
# if there are more images and you specify less FPS, the video will be longer
# The below API will generate the video, play it. In the process it will use your /tmp directory
# to create some temporary files, and they will be deleted after playing the video. 
make_video(test, fps=20)
# there is a third optional argument delete_folder, which is default True, but if you wanna have the video as well as 
# images for your reference, you can pass this as false, so that it's not deleted automatically
make_video(test, fps=20, delete_folder=False)
# There is fourth optional argument play_video which is True by default. If that's passed as False, then the video will not be played. Used in scenarios where you are working in a remote terminal and you don't X forwarding to your PC
make_video(test, fps=20, delete_folder=False, play_video=False)
```
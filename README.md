# pil_video
This is a python package. 

The main use of this code is to play a numpy video. Something quick that can be used in day to day life as a 
Deep learning and robotics researcher.

But having a numpy array to play isn't enough. Usually, people using many different formats, which I don't wanna get into.

So I ask to input a PIL images list, which then I am gonna make a video out of. I will be working out of /tmp
directory, and I will be deleting everything after I play a video for you. Finally I tried not to include any
opencv imports, as it has lots of problems with Py2.7 and Py3.7 and many weird errors. So I tried to use pure
python imports as much as possible so that this can be run out of virtual environments.

Finally, please don't forget to install VLC media player for this to work.

## Installation
> pip install --upgrade git+https://github.com/krishnachaitanya7/pil_video.git

Also, you need to have VLC media player installed beforehand. You can do that by:

> sudo apt-get install vlc

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
```
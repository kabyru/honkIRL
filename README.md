# honkIRL
An extension of Untitled Goose Game that lets you control honks with your mouth. Webcam required. Enthusiasm necessary.

##Yes, with your mouuth.
honkIRL allows you to control the horrible goose's honks by simplying imitating a honk through opening your mouth. This program makes use of OpenCV's facial recognition technology to determine two states of facial activity: when the mouth is closed, and when it is open. This is done through a threshold value that specifies *when* the mouth is open or closed.

There is an EXE release that should work out of the box, check out the Releases tab of this repo for more details.

Should you want to run this from source, you will need to install the following softwares and PyPI packages.

##Software Required
-Python 3
-CMake (must be installed before attempting to install dlib)

##PyPI Packages Required
-opencv-python
-imutils
-dlib

NOTE: Make sure to add Python 3, its Scripts subfolder, and the BIN subfolder of CMake to your PATH environment variable.

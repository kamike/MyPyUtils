#!/usr/bin/env python
# -*- coding:utf8 -*-

import cv2


# 读图片
image = cv2.LoadImage('G:/python/opencv_dir/wx.jpg', cv2.CV_LOAD_IMAGE_COLOR)  # Load the image
# Or just: image=cv.LoadImage('img/image.png')

cv2.NamedWindow('a_window', cv2.CV_WINDOW_AUTOSIZE)  # Facultative
cv2.ShowImage('a_window', image)  # Show the image

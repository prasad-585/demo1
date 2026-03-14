# install libraries
# import library


# read image 

# import numpy as np
# import cv2
# inp1=cv2.imread('amn.jpeg')
# print(inp1)
# cv2.imshow("my image",inp1)
# cv2.waitKey(0)

# resize image

# inpr=cv2.resize(inp1,(1600,700))
# # cv2.imshow('resize image',inpr)
# print(inpr.shape)
# cv2.waitKey(0)

# image conversion

# inpgray=cv2.cvtColor(inpr,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray image',inpgray)
# cv2.waitKey(0)
# inprgb = cv2.cvtColor(inpr,cv2.COLOR_BGR2RGB)
# # cv2.imshow('rgb image',inprgb)
# cv2.waitKey(0)

# example for video

import cv2
import numpy as np
cap=cv2.VideoCapture("video.mp4")
# cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('input video',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#     # resize video

#     inpr=cv2.resize(frame,(600,500))
#     cv2.imshow('Resize image',inpr)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


    
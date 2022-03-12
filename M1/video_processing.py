import cv2
import os
import sys
import math


rows=224
cols=224

keepProcessing=True
windowName='fire'

video = cv2.VideoCapture('test.mp4')
print("Loaded video ...")

cv2.namedWindow(windowName, cv2.WINDOW_NORMAL);

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH));
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = video.get(cv2.CAP_PROP_FPS)
frame_time = round(1000/fps);

while (keepProcessing):

    start_t = cv2.getTickCount();        
    ret, frame = video.read()
    if not ret:
        print("... end of video file reached");
        break;
       
    small_frame = cv2.resize(frame, (rows, cols), cv2.INTER_AREA)
    stop_t = ((cv2.getTickCount() - start_t)/cv2.getTickFrequency()) * 1000;
    cv2.imshow(windowName, frame);

    key = cv2.waitKey(max(2, frame_time - int(math.ceil(stop_t)))) & 0xFF;
    
    if (key == ord('x')):
        keepProcessing = False;
        
    elif (key == ord('f')):
        cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN); 


    else:
        print("usage: python firenet.py videofile.ext");
 

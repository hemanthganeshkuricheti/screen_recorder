#Packeges required for this project
from PIL import ImageGrab
import cv2
import numpy as np
from win32api import GetSystemMetrics
import datetime

#know your screen resolution to capture the entire screen
height= GetSystemMetrics(1)
width= GetSystemMetrics(0)

#use unique file name each time for new recording files
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v' )
capture = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height) )

while True:
    cap= ImageGrab.grab(bbox=(0,0,width, height))
    cap_np= np.array(cap)
#convert it to actual colors
    screen_rec= cv2.cvtColor(cap_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Record', cap_np)
#Saving the captured video
    capture.write(screen_rec)
    if cv2.waitKey(10) == ord ('q'):
        break


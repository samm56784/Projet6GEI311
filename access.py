#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
import numpy as np
from PIL import Image,ImageFilter,ImageEnhance
cap = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
while(True):
    ret, frame = cap.read()
    #cv2.imshow('frame',frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(frame)
    pil_im.sh

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
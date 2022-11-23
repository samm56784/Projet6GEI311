#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
import numpy as np

cap = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#ne fait que faire l'acquisition des images de la caméra ip dont l'adresse est "hardcodées" pour le moment

#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
from queue import Queue
#from main import *

queue = Queue()
queue2 = Queue()
def acquisition_images(queue, queue2, event):
    cap = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
    cap2 = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
    while True:
        if event.is_set():
            break
        _, frame2 = cap.read()
        _, frame1 = cap2.read()
        queue.put(frame2)
        queue2.put(frame1)

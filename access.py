#ne fait que faire l'acquisition des images de la caméra ip dont l'adresse est "hardcodées" pour le moment

#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
from queue import Queue
#from main import *

#queue = Queue()
#queue2 = Queue()


def acquisition_images(queue, queue2, event, event2, event3, queue9):
    cap = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
    #cap = cv2.VideoCapture('http://38.81.159.248/mjpg/video.mjpg')
    cap2 = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
    #cap2 = cv2.VideoCapture('http://38.81.159.248/mjpg/video.mjpg')
    while True:
        ip='http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812'
        if event.is_set():
            print("finito ac")
            exit()
        if event2.is_set():
            ip = queue9.get()
            cap = cv2.VideoCapture(ip)
            cap2 = cv2.VideoCapture(ip)
            event2.clear()
        if event3.is_set():
            with queue.mutex:
                queue.queue.clear()
            with queue2.mutex:
                queue2.queue.clear()
        else:
            print(ip)
            print("acq")
            _, frame2 = cap.read()
            _, frame1 = cap2.read()
            queue.put(frame2)
            queue2.put(frame1)

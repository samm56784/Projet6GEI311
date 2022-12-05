#ne fait que faire l'acquisition des images de la caméra ip dont l'adresse est "hardcodées" pour le moment

#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
#from main import *


def acquisition_images(queue, queue2):
    cap = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
    while True:
        _, frame2 = cap.read()
        queue.put(frame2)
        queue2.put(frame2)

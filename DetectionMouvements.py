from access import *
import numpy as np
from fonctions_utiles import *
from PIL import Image
import os


def DetectionMouvement(queue1, queue2, queue3, event):
    while True:
        if event.is_set():
            print("finito det")
            exit()
        else:
            im1 = queue1.get()
            im2 = queue2.get()
            im3 = np.subtract(im1, im2)
            im3 = Image.fromarray(im3, mode="RGB")
            im4 = conversion_image_PIL_vers_cv2(im3)
            queue3.put(im4)


    #pil or cv to np
    #2 queues soustraction
    #resulats ajustements de certaines
    #soustraction de matrices np
    #vérif différences NOTABLES dans addition(soustraction?)
    #définition threshold détection
    #stockage info mouvement détecté


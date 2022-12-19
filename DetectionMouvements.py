from access import *
import numpy as np
from fonctions_utiles import *
from PIL import Image
from PIL import ImageEnhance, ImageFilter, ImageOps, ImageChops
import os


def DetectionMouvement(queue1, queue2, queue3, event, event3):
    while True:
        if event.is_set():
            exit()
            print("finito det")
            exit()
            break
        if event3.is_set():
            with queue1.mutex:
                queue1.queue.clear()
            with queue2.mutex:
                queue2.queue.clear()
            with queue3.mutex:
                queue3.queue.clear()
        else:
            im1 = queue1.get()
            im1 = Image.fromarray(im1, mode="RGB")
            im2 = queue2.get()
            im2 = Image.fromarray(im2, mode="RGB")
            im3 = ImageChops.multiply(im1, im2)
            im4 = ImageChops.difference(im1, im2)
            im4 = im4.convert("L")
            im4 = ImageOps.colorize(im4, black="white", white="red", mid="white")
            #im5 = ImageChops.difference(im4, im3)

            #im3 = np.subtract(im1, im2)
            #im3 = np.subtract(im1, im2)
            #im3 = Image.fromarray(im3, mode="RGB")
            im9 = ImageEnhance.Brightness(im4).enhance(1.04)
            #im7 = conversion_image_PIL_vers_cv2(im9)
            queue3.put(im9)


    #pil or cv to np
    #2 queues soustraction
    #resulats ajustements de certaines
    #soustraction de matrices np
    #vérif différences NOTABLES dans addition(soustraction?)
    #définition threshold détection
    #stockage info mouvement détecté


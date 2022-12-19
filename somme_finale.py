from PIL import Image
from PIL import ImageEnhance, ImageFilter, ImageOps, ImageChops
from fonctions_utiles import *

def somme_finale(queue1, queue2, queue3, event):

    while True:
        if event.is_set():
            print("finito somme")
            exit()
        else:
            im1 = queue1.get()
            im3 = conversion_image_cv2_vers_PIL(im1)
            im2 = queue2.get()
            im4 = ImageChops.multiply(im3, im2)
            im5 = conversion_image_PIL_vers_cv2(im4)
            queue3.put(im5)

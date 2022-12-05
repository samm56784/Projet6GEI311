# reçoit l'image (feed) depuis access.py et modifie les images à l'aide des filtres
from access import *
from fonctions_utiles import *
#from main import *
import os
import shutil


def processing(queue1, queue2, path):

    i = 0
    while True:
        frame2 = queue1.get()
        pil_im = conversion_image_cv2_vers_PIL(frame2)
        im = pil_im.convert("L")
        enh = filtres_images(im)
        open_cv_image2 = conversion_image_PIL_vers_cv2(enh)
        queue1.task_done()
        queue2.put(open_cv_image2)
        path2 = os.path.join(path, str(i) + r".jpeg")
        enh.save(path2)
        i = i + 1
        #if cv2.waitKey(1) & 0xFF == ord('q'):
           # break



# reçoit l'image (feed) depuis access.py et modifie les images à l'aide des filtres
from access import *
from fonctions_utiles import *
import os
import shutil


def processing(queue1, queue2, queue3, queue4, queue5, path, event, event3, event4):
    i = 0
    while True:
        if event.is_set():
            print("finito proc")
            exit()
        if event3.is_set():
            with queue1.mutex:
                queue1.queue.clear()
            with queue2.mutex:
                queue2.queue.clear()
            with queue3.mutex:
                queue3.queue.clear()
            with queue4.mutex:
                queue4.queue.clear()

        else:
            print("proc")
            frame2 = queue1.get()
            pil_im = conversion_image_cv2_vers_PIL(frame2)
            im = pil_im.convert("L")
            if event4.is_set():
                enh = filtres_images2(im)
            else:
                enh = filtres_images(im)
            open_cv_image2 = conversion_image_PIL_vers_cv2(enh)
            #open_cv_image3 =conversion_image_PIL_vers_cv2(im)
            queue1.task_done()
            if i % 2 == 0:
                queue3.put(np.array(enh))
            else:
                queue4.put(np.array(enh))

            queue2.put(open_cv_image2)
            queue5.put(open_cv_image2)
            #path2 = os.path.join(path, str(i) + r".jpeg")
            #enh.save(path2)
            i = i + 1




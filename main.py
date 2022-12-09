# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
import threading
from queue import Queue

from access import *
from processing import *
from threading import Thread
from fonctions_utiles import *
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

queueT1 = Queue()
queueT2 = Queue()
queueT3 = Queue()
queueT5 = Queue()
queueT6 = Queue()

event = threading.Event()
event.clear()

def main():
    global event
    global queueT1
    global queueT2
    global queueT3
    global queueT5
    global queueT6
    continuer = ''
    pathdir = os.path.join(os.getcwd(), r"TempDump")
    print(pathdir)
    if not os.path.exists(pathdir):
        os.mkdir(pathdir)

    # définition des threads du programme (accès aux images de la caméra, processing(filtres), algo de détection de mouvement
    t1 = Thread(target=acquisition_images, args=(queueT1, queueT6, event, ))
    t1.start()
    t2 = Thread(target=processing, args=(queueT1, queueT2, pathdir, event,))
    t2.start()
    #t6 = Thread(target=image_display, args=(queueT2, event, ))
  #  t6.start()
    #t1.join()
    #t2.join()
  #  t6.join()
    while True:
        image = queueT2.get()  # Added
        if image is None:
            break  # Added
        cv2.imshow('image_display', image)  # Added
        #cv2.waitKey(10)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            event.set()
            shutil.rmtree(pathdir)
            os.mkdir(pathdir)
            cv2.destroyAllWindows()
            break
        # Added
        continue


    # See PyCharm help at https://www.jetbrains.com/help/pycharm/


main()

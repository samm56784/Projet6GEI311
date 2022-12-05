# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
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


def main():

   # global queueT1
 #   global queueT2
   # global queueT3
    #global queueT5
   # global queueT6
    continuer = True
    pathdir = os.path.join(os.getcwd(), r"TempDump")
    print(pathdir)
    if not os.path.exists(pathdir):
        os.mkdir(pathdir)

    # définition des threads du programme (accès aux images de la caméra, processing(filtres), algo de détection de mouvement
    t1 = Thread(target=acquisition_images, args=(queueT1, queueT6, ))
    t1.start()
    t2 = Thread(target=processing, args=(queueT1, queueT2, pathdir))
    t2.start()
    t6 = Thread(target=lecture_video, args=(queueT6,))
    t6.start()
    t1.join()
    t2.join()
    t6.join()



    '''while continuer:
        key = input()
        key = key.upper()
        if key == 'Q':
            continuer = False
            shutil.rmtree(pathdir)
            os.mkdir(pathdir)
            cv2.destroyAllWindows()
            print(os.getcwd())
            break'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


main()

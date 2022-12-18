# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
import threading
import time
from queue import Queue
from tkinter import NW, Tk, Canvas, PhotoImage
from access import *
from processing import *
from threading import Thread
from fonctions_utiles import *
import tkinter as tk
from tkinter import Button, RIGHT, LEFT
from DetectionMouvements import DetectionMouvement
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#ip = 'http://205.237.248.39/'
#ip = 'http://72.227.122.62:8081/'

queueT1 = Queue()
queueT2 = Queue()
queueT3 = Queue()
queueT4 = Queue()
queueT5 = Queue()
queueT6 = Queue()
queueT7 = Queue()
queueT8 = Queue()
queueT9 = Queue()
queueT10 = Queue()
queueT11 = Queue()

event = threading.Event()
event.clear()
event2 = threading.Event()
event2.clear()
event3 = threading.Event()
event3.clear()
event4 = threading.Event()
event4.clear()
ip = 'http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812'
def entrer_adresse_camera():
    global ip
    app = Tk()
    app.title("Choix adresse camera")
    canvas1 = tk.Canvas(app, width=400, height=300)
    canvas1.pack()
    entry1 = tk.Entry(app)
    canvas1.create_window(200,140,window=entry1)

    def default_ip():
        ip = 'http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812'
        queueT9.put(ip)
        event2.set()
        event3.set()
        time.sleep(1)
        event3.clear()
        app.destroy()
        print(ip)
    def get_input():
        global ip
        ip = entry1.get()
        if ip == "":
            ip = 'http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812'
        queueT9.put(ip)
        #label1 = tk.Label(app, text=x1)
        #canvas1.create_window(200, 230, window=label1)
        event2.set()
        event3.set()
        time.sleep(1)
        event3.clear()
        app.destroy()
        print(ip)

    button1 = Button(app, text="get input", command=get_input)
    button1.pack(side=BOTTOM)
    button1 = Button(app, text="adresse par défaut", command=default_ip)
    button1.pack(side=BOTTOM)
    app.mainloop()
def changer_mode_filtre(num):
    global event4
    if num == 1:
        event4.set()
    else:
        event4.clear()


def affichage_image(queue):
    app2 = Tk()
    app2.title("Affichage")
    canvas2 = tk.Canvas(app2, width=400, height=300)
    canvas2.pack()
    update(root1=app2, canvas1=canvas2, queue1=queue)
    button1 = Button(app2, text="Quitter", state=tk.NORMAL, command=app2.destroy)
    button1.pack(side=RIGHT)
    app2.mainloop()

def main():
    global event
    global event2
    global event3
    global event4
    global queueT1
    global queueT2#cv2
    global queueT3
    global queueT4 #
    global queueT5
    global queueT6
    global queueT7 #
    global queueT8
    global queueT9
    global queueT10
    global queueT11
    global ip
    continuer = ''
    pathdir = os.path.join(os.getcwd(), r"TempDump")
    print(pathdir)
    if not os.path.exists(pathdir):
        os.mkdir(pathdir)

    # définition des threads du programme (accès aux images de la caméra, processing(filtres), algo de détection de mouvement
    t1 = Thread(target=acquisition_images, args=(queueT1, queueT6, event, event2, event3, queueT9, ))
    t1.start()
    t2 = Thread(target=processing, args=(queueT1, queueT2, queueT4, queueT7, pathdir, event, event3, event4,  ))
    t2.start()
    t3 = Thread(target=DetectionMouvement, args=(queueT4, queueT7, queueT8, event, event3))
    t3.start()

    #t6 = Thread(target=image_display, args=(queueT2, event, ))
  #  t6.start()
    #t1.join()
    #t2.join()
  #  t6.join()

    root = Tk()
    root.title("Video")
    #cap = cv2.VideoCapture("video.mp4")

    canvas = Canvas(root, width=636, height=476)
    canvas.pack()
    update(root1=root, canvas1=canvas, queue1=queueT8)
    button1 = Button(root, text="Quitter", state=tk.NORMAL, command=lambda: quitter(event, root))
    button1.pack(side=RIGHT)
    button2 = Button(root, text="Entrer adresse", state=tk.NORMAL, command=entrer_adresse_camera)
    button2.pack(side=LEFT)
    button3 = Button(root, text="Mode jour", state=tk.NORMAL, command=lambda: changer_mode_filtre(1))
    button3.pack(side=LEFT)
    button4 = Button(root, text="Mode nuit", state=tk.NORMAL, command=lambda: changer_mode_filtre(0))
    button4.pack(side=LEFT)
    button5 = Button(root, text="Afficher image filtrée", state=tk.NORMAL, command=lambda: affichage_image(queueT2))
    button5.pack(side=BOTTOM)
    button6 = Button(root, text="Afficher image soustraite", state=tk.NORMAL, command=lambda: affichage_image(queueT8))
    button6.pack(side=BOTTOM)
    root.mainloop()
    t1.join()
    t2.join()
    t3.join()
    print("finished")
    shutil.rmtree(pathdir)
    os.mkdir(pathdir)
    #print(ip)
    #print(ip)
    exit()
    #cap.release()

''' while True:
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
        continue'''


    # See PyCharm help at https://www.jetbrains.com/help/pycharm/


main()

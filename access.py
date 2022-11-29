#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
import numpy as np
import shutil
from PIL import Image,ImageFilter,ImageEnhance
import os
import os.path
cap = cv2.VideoCapture('http://205.237.248.39/axis-cgi/mjpg/video.cgi?resolution=635x476&dummy=1603113452812')
i = 0
pathdir = os.path.join(os.getcwd(), r"TempDump" )
print(pathdir)
if not os.path.exists(pathdir):
    os.mkdir(pathdir)
while(True):
    ret, frame = cap.read()
    _, frame2 = cap.read()

    cv2.imshow('frame', frame)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(frame2)
    #im = pil_im.filter(ImageFilter.FIND_EDGES)
    im = pil_im.convert("L")

    enh = ImageEnhance.Brightness(im).enhance(5.0)
    enh = ImageEnhance.Contrast(enh).enhance(4.0)
    enh = enh.filter(ImageFilter.FIND_EDGES)
    enh = enh.filter(ImageFilter.GaussianBlur(radius=1))
    enh = enh.filter(ImageFilter.MedianFilter(size=1))
    im = im.filter(ImageFilter.CONTOUR)
    im = im.filter(ImageFilter.FIND_EDGES)
    im = im.filter(ImageFilter.GaussianBlur(radius=0))
    im = im.convert('RGB')
    enh = enh.convert(('RGB'))
    open_cv_image2 = np.array(enh)
    # Convert RGB to BGR
    open_cv_image2 = open_cv_image2[:, :, ::-1].copy()
    cv2.imshow('open_cv_image2',open_cv_image2)
    open_cv_image = np.array(im)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    cv2.imshow('open_cv_image',open_cv_image)
    #os.path.join(r"E:\TempDump",str(i),r".png")
    path = os.path.join(pathdir, str(i) + r".jpeg")
    #path = os.path.join(r"E:\TempDump", str(i) + r".jpeg" )
    im.save(path)
    #pil_im.show()
    i = i + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
shutil.rmtree(pathdir)
os.mkdir(pathdir)
cap.release()
cv2.destroyAllWindows()
print(os.getcwd())
#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
import cv2
import numpy as np
import shutil
from skimage.io import imread
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
from matplotlib import pyplot as plt
import os
import os.path
n = 2
size2 = 635, 476
size = 635*n, 476*n
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
    # im = pil_im.filter(ImageFilter.FIND_EDGES)
    im = pil_im.convert("L")

    # enh = ImageEnhance.Brightness(im).enhance(5.0)
    enh = im
    enh = enh.resize(size, resample=Image.Resampling.LANCZOS)
    #enh = ImageOps.autocontrast(enh, cutoff=2, ignore=None, mask=None, preserve_tone=False)
    enh = ImageEnhance.Brightness(enh).enhance(2.0)
    enh = ImageEnhance.Contrast(enh).enhance(1.0)
    enh = enh.filter(ImageFilter.MedianFilter(size=9))
    # enh = ImageEnhance.Sharpness(enh).enhance(10.0)
    # enh = enh.filter(ImageFilter.CONTOUR)
    enh = enh.filter(ImageFilter.FIND_EDGES)
    enh = ImageEnhance.Brightness(enh).enhance(8.0)
    enh = enh.filter(ImageFilter.GaussianBlur(radius=2))
    #enh = enh.filter(ImageFilter.MedianFilter(size=5))
    enh = ImageEnhance.Sharpness(enh).enhance(18.0)
    enh = enh.resize(size2, resample=Image.Resampling.LANCZOS)

    im = im.resize(size, resample=Image.Resampling.LANCZOS)
    #enh = enh.filter(ImageFilter.MedianFilter(size=13))
    #im = im.filter(ImageFilter.CONTOUR)
    im = im.filter(ImageFilter.FIND_EDGES)
    im = ImageEnhance.Brightness(im).enhance(2.0)
    im = im.filter(ImageFilter.GaussianBlur(radius=1))
    im = im.resize(size2, resample=Image.Resampling.LANCZOS)
    im = im.convert('RGB')
    enh = enh.convert(('RGB'))
    open_cv_image2 = np.array(enh)
    # Convert RGB to BGR
    open_cv_image2 = open_cv_image2[:, :, ::-1].copy()
    cv2.imshow('open_cv_image2',open_cv_image2)
    open_cv_image = np.array(im)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    cv2.imshow('nuit',open_cv_image)
    #os.path.join(r"E:\TempDump",str(i),r".png")
    path = os.path.join(pathdir, str(i) + r".jpeg")
    #path = os.path.join(r"E:\TempDump", str(i) + r".jpeg" )
    im.save(path)
    #pil_im.show()
    i = i + 1
    #photo = np.array(enh)
    #plt.imshow(photo, interpolation='nearest')
    #plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
shutil.rmtree(pathdir)
os.mkdir(pathdir)
cap.release()
cv2.destroyAllWindows()
print(os.getcwd())
#import cv2
#import PIL
import cv2
import numpy as np
from PIL import Image
from PIL import ImageEnhance, ImageFilter, ImageOps

n = 2
size2 = 635, 476
size = 635 * n, 476 * n


def conversion_image_cv2_vers_PIL(image_cv2):
    image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(image_cv2)
    return pil_im


def filtres_images(im):
    enh = im
    enh = enh.resize(size, resample=Image.Resampling.LANCZOS)
    enh = enh.filter(ImageFilter.FIND_EDGES)
    enh = enh.filter(ImageFilter.GaussianBlur(radius=1))
    enh = enh.filter(ImageFilter.MedianFilter(size=3))
    enh = ImageEnhance.Sharpness(enh).enhance(8.0)
    enh = ImageOps.colorize(enh, black="black", white="lime")
    enh = ImageEnhance.Brightness(enh).enhance(1.0)
    enh = enh.resize(size2, resample=Image.Resampling.LANCZOS)
    return enh


def conversion_image_PIL_vers_cv2(enh):

    enh = enh.convert('RGB')
    open_cv_image2 = np.array(enh)
    open_cv_image2 = open_cv_image2[:, :, ::-1].copy()

    return open_cv_image2


def lecture_video(queue_images):
    #time.sleep(1)
    while True:
        '''if queue_images.empty():
            time.sleep(1)
        else:'''
        image_actuelle = queue_images.get()
        cv2.imshow('video', image_actuelle)


#https://stackoverflow.com/questions/17053366/opencv-multiprocessing-in-python-queue-sync
def image_display(taskqueue, event):
   #cv2.namedWindow ('image_display', cv2.CV_WINDOW_AUTOSIZE)
   while True:
      if event.is_set():
           break
      image = taskqueue.get()              # Added
      if image is None:
       break             # Added
      cv2.imshow ('image_display', image)  # Added
      cv2.waitKey(10)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      # Added
      continue                             # Added

      '''if taskqueue.get()==None:
         continue
      else:
         image = taskqueue.get()
         im = Image.fromstring(image['mode'], image['size'], image['pixels'])
         num_im = np.asarray(im)
         cv2.imshow ('image_display', num_im)'''
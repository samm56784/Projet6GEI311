import cv2
import PIL
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

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

    while True:
        image_actuelle = queue_images.get()
        cv2.imshow('video', image_actuelle)


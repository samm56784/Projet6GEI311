
from PIL import Image,ImageFilter,ImageEnhance
#Read image
im = Image.open('C:/Users/samue/Downloads/lena.jpg')
#Display image
im.show()
enh = ImageEnhance.Contrast(im)
enh.enhance(2).show()
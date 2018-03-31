from Analyzer import Analyzer
from skimage import io, color
from PIL import Image
from pytesser import *

img = io.imread('testImage.png')
txt = image_to_string('testImage.png')
analyzer = Analyzer()

textOfImage = Image.open('testImage.png')
text = textOfImage.getextrema()
print(text)

analyzer.readImage(img)



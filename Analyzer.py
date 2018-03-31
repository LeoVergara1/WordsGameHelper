from skimage import io, color
import skimage.io as io
from skimage.color import rgb2gray 

class Analyzer(object):
  
  def readImage(self, image):
    print("Hola")
    dimensions = color.guess_spatial_dimensions(image)
    print(dimensions)
    print(image.shape)


  pass

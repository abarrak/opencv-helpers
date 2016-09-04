'''
' OpenCV Helpers
' ==============
'
' :summary: a set of utility functions for various opencv tasks.
'
' :package: opencv_helpers
' :module:  helpers
' :author:  Abdullah Barrak (abarrak).
' :license: No-License (public domain).
'
'''
from __future__ import print_function, division
import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


'''
'   Images I/O Functions
'''
def load(path, mode=cv.IMREAD_COLOR):
  '''
  load image for give path in cv object.
  :param mode: can be any of the following:
               cv.IMREAD_COLOR
               cv.IMREAD_GRAYSCALE
               cv.IMREAD_UNCHANGED (for 16-bit/32-bit image).
  '''
  img = cv.imread(path, mode)
  if img is None:
    raise Exception('Error: Image not found.')
  return img

def show(image, title='Image Viewer'):
  ''' reveal :image: object in opencv viewer. if path is given, load() first. '''
  if isinstance(image, str):
    image = load(str)

  cv.imshow(title, image)
  cv.waitKey(0)
  cv.destroyAllWindows()

def save(path, image):
  ''' persist :image: object to disk. '''
  cv.imwrite(path, image)

def plot(image):
  ''' show image in matplotlib viewer. '''
  if isinstance(image, str):
    image = load(str)

  plt.imshow(image)
  plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
  plt.show()  


'''
'   Images Manipulation Functions
'''
def resize(image, width, height):
  ''' sets :image: width and height to :width: and :height: parameters. '''
  return cv.resize(image, (width, height), interpolation=cv.INTER_LINEAR)

def scale(image, new_size, kind='width'):
  ''' resize :image: to :new_size: param while preserving aspect ratio. '''
  # obtain image height & width.
  h, w, channels = image.shape

  # aspect ratio = original width / original height.
  aspect_ratio =  w / h

  if kind == 'width':
    if w > new_size:
      # adjusted height.
      new_height = int(new_size // aspect_ratio)
      # inter_area for resizing algorithm parameter.
      return cv.resize(image, (new_size, new_height), interpolation=cv.INTER_AREA)
  elif kind == 'height':
      if h > new_size:
        # adjusted width.
        new_width = int(new_size // aspect_ratio)
        # inter_area for resizing algorithm parameter.
        return cv.resize(image, (new_width, new_size), interpolation=cv.INTER_AREA)
  else:
    raise Exception('not supported option.')


'''
'   Image Preprocessing Functions
'''


'''
'   Image Segmentation Functions
'''


'''
'   Image Filtering Functions
'''


'''
'   Feature Extraction Functions
'''


'''
'   CV Machine Learning Functions
'''


'''
'   Utilities
'''
def current_dir():
  ''' return the script current path. '''
  return os.curdir

def combine(directory, file):
  return os.path.join(directory, file)

def cobmine_with_current_path(filename):
  ''' construct a path of the given filename. Can be foldername too. '''
  current = LVHelpers.current_dir()
  path = LVHelpers.combine(current, filename)
  return path

def combine(filename, path=None):
  ''' construct a path of the given file/folder name with the current directory or given path. '''
  curr = path or current_dir()
  return os.path.join(curr, filename)


if __name__ == '__main__':
  pass

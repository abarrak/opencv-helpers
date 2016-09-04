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
    raise Exception("Error: Image not found in %s." % path)
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
    raise Exception('Not supported option.')

'''
'   Image Preprocessing Functions
'''
def grayscale():
  pass

def fixed_threshold(image, threshold_value=130):
  ''' :param fixed_threshold: the threshold constant. '''
  ret, thresholded = cv.threshold(image, fixed_threshold, 255, cv.THRESH_BINARY_INV)
  return thresholded

def adaptive_threshold(image, kind='mean', cell_size=35, c_param=17):
  '''
  :param kind: specifiy adaptive method, whether 'mean' or 'gaussian'.
  :param cell_size: n for the region size (n x n).
  :param c_param: substraction constant.
  :return: a binary version of the input image.
  '''
  if adaptive_type == 'mean':
    method = cv.ADAPTIVE_THRESH_MEAN_C
  elif adaptive_type == 'gaussian':
    method = cv.ADAPTIVE_THRESH_GAUSSIAN_C
  else:
    raise Exception('Unknown adaptive threshod method.')

  return cv.adaptiveThreshold(image, 255, method, cv.THRESH_BINARY_INV, cell_size, c_param)

def smooth():
  pass

def frame(image, top=2, bottom=2, left=2, right=2, borderType=cv.BORDER_CONSTANT, color=[0, 0, 255]):
  ''' 
  Add borders around :image: param. 
  Other options for borderType are:
  cv.BORDER_REFLECT, cv.BORDER_REFLECT_101, cv.BORDER_DEFAULT, cv2.BORDER_REPLICATE, cv2.BORDER_WRAP
  '''
  return cv.copyMakeBorder(image, top, bottom, left, right, borderType, value=color)


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

def combine(filename, path=None):
  ''' construct a path of given file/folder with the current directory or given path. '''
  curr = path or current_dir()
  return os.path.join(curr, filename)


if __name__ == '__main__':
  show(frame(load('images/1.jpg')))

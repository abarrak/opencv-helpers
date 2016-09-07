#-*- encoding: utf-8
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
import matplotlib
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

def save(path, image, jpg_quality=None, png_compression=None):
  '''
  persist :image: object to disk. if path is given, load() first.
  jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
  png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
                  Default is 3.
  '''
  if isinstance(image, str):
    image = load(str)

  if jpg_quality:
    cv.imwrite(path, image, [cv.IMWRITE_JPEG_QUALITY, jpg_quality])
  elif png_compression:
    cv.imwrite(path, image, [cv.IMWRITE_PNG_COMPRESSION, png_compression])
  else:
    cv.imwrite(path, image)

def plot(image, is_bgr=True, cmap=None, title='Image Viewer', disable_toolbar=True):
  ''' show image in matplotlib viewer. if path is given, load() first. '''
  if isinstance(image, str):
    image = load(str)

  if disable_toolbar:
    matplotlib.rcParams['toolbar'] = 'None'

  # opencv image are in BGR colormap while matplotlib in RGB.
  if is_bgr:
    image = convert_to_rgb(image)

  fig = plt.figure()
  fig.canvas.set_window_title(title)

  plt.imshow(image, cmap)
  # hide tick values on X and Y axis.
  plt.xticks([]), plt.yticks([])
  plt.show()

def plot_two_images(image_1, image_2, cmap_1=None, cmap_2=None, title='Image Viewer', disable_toolbar=True):
  '''
  plot :image1: and :image2: in a row.
  '''
  if disable_toolbar:
    matplotlib.rcParams['toolbar'] = 'None'

  fig = plt.figure(figsize=(13, 4))
  fig.canvas.set_window_title(title)

  a = fig.add_subplot(1, 2, 1)

  plt.imshow(image_1, cmap_1)
  plt.xticks([]), plt.yticks([])
  a.set_title('Before')

  a = fig.add_subplot(1, 2 ,2)
  plt.imshow(image_2, cmap_2)
  plt.xticks([]), plt.yticks([])
  a.set_title('After')

  plt.show()

def metadata(image):
  ''' return a hash with useful info about :image:. '''
  return {'pixels_number': image.size, 'structure': image.shape, 'date_type': image.dtype }


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
    raise ValueError('Not supported option.')

def crop(image, x_start, x_end, y_start, y_end):
  ''' cut q region of :image: by suppiled x, y pixel coordinates. '''
  range_check = lambda p, lim: p < 0 or p > lim
  side_error  = lambda name, val, lim: "Supplied %s(=%d) argument is out of bount 0 =< %s =< %d " % \
                                  (name, val, name, lim)

  x_lim, y_lim = image.shape[1], image.shape[0]

  if range_check(x_start, x_lim):
    raise IndexError(side_error("x_start", x_start, x_lim))
  if range_check(x_end, x_lim):
    raise IndexError(side_error("x_end", x_end, x_lim))
  if range_check(y_start, y_lim):
    raise IndexError(side_error("y_start", y_start, y_lim))
  if range_check(y_end, y_lim):
    raise IndexError(side_error("y_end", y_end, y_lim))

  if x_start > x_end:
    raise IndexError("x_start(=%d) index can't be greater than x_end(=%d)" % (x_start, x_end))
  if y_start > y_end:
    raise IndexError("y_start(=%d) index can't be greater than y_end(=%d)" % (y_start, y_end))

  if x_start == x_end:
    raise IndexError("x_start and x_end can't both have the same value (=%d)" % x_start)
  if y_start == y_end:
    raise IndexError("y_start and y_end can't both have the same value(=%d)" % y_start)

  return image[y_start:y_end, x_start:x_end]


'''
'   Image Preprocessing Functions
'''
def grayscale(image, is_rgb=False):
  # opencv image are in BGR colormap while matplotlib in RGB.
  if is_rgb:
    return cv.cvtColor(image, cv.COLOR_RGB2GRAY)
  else:
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def convert_to_rgb(image):
  return cv.cvtColor(image, cv.COLOR_BGR2RGB)

def fixed_threshold(image, thresh_value=120, above_thresh_assigned=255, thresh_style=cv.THRESH_BINARY_INV):
  '''
  :param thres_value: the threshold constant.
  :param thresh_style: can be any of the following.
                      cv.THRESH_BINARY
                      cv2.THRESH_BINARY_INV
                      cv2.THRESH_TRUNC
                      cv2.THRESH_TOZERO
                      cv2.THRESH_TOZERO_INV
   '''
  ret, thresholded = cv.threshold(image, thresh_value, above_thresh_assigned, thresh_style)
  return thresholded

def adaptive_threshold(image, above_thresh_assigned=255, kind='mean', cell_size=35, c_param=17,
                       thresh_style=cv.THRESH_BINARY_INV):
  '''
  :param kind: specify adaptive method, whether 'mean' or 'gaussian'.
  :param cell_size: n for the region size (n x n).
  :param c_param: subtraction constant.
  :return: a binary version of the input image.
  '''
  if kind == 'mean':
    method = cv.ADAPTIVE_THRESH_MEAN_C
  elif kind == 'gaussian':
    method = cv.ADAPTIVE_THRESH_GAUSSIAN_C
  else:
    raise ValueError('Unknown adaptive threshold method.')

  return cv.adaptiveThreshold(image, above_thresh_assigned, method, thresh_style, cell_size, c_param)

def otsu_threshold(image, above_thresh_assigned=255, thresh_style=cv.THRESH_BINARY_INV):
  ''' apply otsu's binarization algorithm to find optimal threshold value. '''
  ret, thresholded = cv.threshold(image, 0, above_thresh_assigned, thresh_style  + cv.THRESH_OTSU)
  return { 'otsu_thresh': ret, 'image': thresholded }

def smooth(image, method='gaussian', kernel=(5, 5)):
  ''' blur filter for noise removal. '''
  if method == 'blur':
    return cv.blur(image, kernel)
  elif method =='gaussian':
    return cv.GaussianBlur(image, kernel, 0)
  else:
    raise ValueError('Unknown smoothing method.')

def thin(image, kernel=(2, 2)):
  ''' reduce the shape line stroke. '''
  k = np.ones(kernel, np.uint8)
  return cv.erode(image, k, iterations=1)

def stress(image, kernel=(1, 1)):
  ''' increase the shape thickness. '''
  k = np.ones(kernel, np.uint8)
  return cv.dilate(image, k)

def remove_noise(image, kernel=(2, 2)):
  ''' removes noisy pixels in the area. '''
  return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)

def fill(image, kernel=(2, 2)):
  ''' fill gaps in shapes structure. '''
  return cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)

def frame(image, top=2, bottom=2, left=2, right=2, borderType=cv.BORDER_CONSTANT, color=[255, 0, 0]):
  '''
  Add borders around :image:
  :param image: has to be in RBG color scheme. Use `convert_to_rgb` if it's in opencv BGR scheme.
  :param color: array representing an RGB color.
  :param borderType: Other options are:
                                    cv.BORDER_REFLECT,
                                    cv.BORDER_REFLECT_101,
                                    cv.BORDER_DEFAULT,
                                    cv.BORDER_REPLICATE,
                                    cv.BORDER_WRAP
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
  ''' return script current path. '''
  return os.curdir

def combine(filename, path=None):
  ''' construct path of the given file/folder with current directory or a given path. '''
  curr = path or current_dir()
  return os.path.join(curr, filename)


if __name__ == '__main__':
  pass

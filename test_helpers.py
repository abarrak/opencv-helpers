'''
' OpenCV Helpers
' ==============
'
' :summary: a set of utility functions for various opencv tasks.
'
' :package: opencv_helpers
' :module:  test_helpers
' :author:  Abdullah Barrak (abarrak).
' :license: No-License (public domain).
'
'''
from __future__ import print_function, division
import os
import numpy as np
import cv2 as cv
import pytest
from helpers import *


sample_one = load("images/1.jpg")
sample_two = load("images/1.jpg")

def test_load():
  assert type(load("images/1.jpg")) == np.ndarray
  with pytest.raises(Exception):
    load('images/not-there.jpg')

def test_save():
  save('images/new_1.jpg', sample_one)
  assert os.path.isfile('images/new_1.jpg')
  save('images/new_2.jpg', sample_one, jpg_quality=50)
  assert os.path.isfile('images/new_2.jpg')

  assert os.path.getsize('images/new_1.jpg') > os.path.getsize('images/new_2.jpg')
  os.remove('images/new_1.jpg')
  os.remove('images/new_2.jpg')

def test_rsize():
  sized = resize(sample_one, 200, 200)
  assert sample_one != sized
  assert sample_one.shape[0:2] != sized.shape[0:2]

def test_scale():
  new_w = 200
  scaled = scale(sample_one, new_w, 'width')
  assert sample_one != scaled
  assert sample_one.shape[0:2] != scaled.shape[0:2]
  # enusre formula: new height = [new width / (aspect ratio = original width / original height)]
  assert scaled.shape[0] == int(new_w // (sample_one.shape[1] / sample_one.shape[0]))

  new_h = 300
  scaled = scale(sample_one, new_h, 'height')
  assert sample_one != scaled
  assert sample_one.shape[0:2] != scaled.shape[0:2]
  # enusre formula: new width = [new height / (aspect ratio = original width / original height)]
  assert scaled.shape[1] == int(new_h // (sample_one.shape[1] / sample_one.shape[0]))

  with pytest.raises(ValueError):
    scale(sample_one, 200, 'malform')

def test_crop():
  x_lim, y_lim = sample_one.shape[1], sample_one.shape[0]
  crop_pixels = 10
  valid_x, valid_y = x_lim - crop_pixels, y_lim - crop_pixels

  # check bounds of image.
  with pytest.raises(IndexError) as ex:
    crop(sample_one, -1, valid_x, 0, valid_y)
  assert 'x_start' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, x_lim + 1, valid_x, 0, valid_y)
  assert 'x_start' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, valid_x, -1, 0, valid_y)
  assert 'x_end' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, valid_x, x_lim + 1, 0, valid_y)
  assert 'x_end' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, 0, valid_x, -1, valid_y)
  assert 'y_start' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, 0, valid_x, y_lim + 1, valid_y)
  assert 'y_start' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, 0, valid_x, 0, -1)
  assert 'y_end' in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, 0, valid_x, 0, y_lim + 1)
  assert 'y_end' in str(ex.value)

  # check correct ordering.
  with pytest.raises(IndexError) as ex:
    crop(sample_one, 10, 5, 0, valid_y)
  for w in ['x_start', 'x_end', 'greater']:
    assert w in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, 0, valid_x, 10, 9)
  for w in ['y_start', 'y_end', 'greater']:
    assert w in str(ex.value)

  # check something to crop.
  with pytest.raises(IndexError) as ex:
    crop(sample_one, valid_x, valid_x, 0, valid_y)
  for w in ['x_start', 'x_end', 'same']:
    assert w in str(ex.value)

  with pytest.raises(IndexError) as ex:
    crop(sample_one, 0, valid_x, valid_y, valid_y)
  for w in ['y_start', 'y_end', 'same']:
    assert w in str(ex.value)

  # finally .. proper cropping :)
  cropped = crop(sample_one, 0, valid_x, 0, valid_y)
  assert cropped != sample_one
  assert cropped.shape[0:2] != sample_one.shape[0:2]
  assert sample_one.shape[0] - cropped.shape[0] == crop_pixels
  assert sample_one.shape[1] - cropped.shape[1] == crop_pixels

def test_grayscale():
  grayed = grayscale(sample_one)
  assert(grayed.shape == sample_one.shape[0:2])
  assert(len(grayed.shape) == 2)
  assert(grayed.ndim == 2)

def test_fixed_threshold():
  grayed = grayscale(sample_one)
  thresholded = fixed_threshold(grayed, 130)

  assert thresholded.ndim == 2
  assert thresholded.shape == grayed.shape[0:2]
  for row in thresholded:
    for pix in row:
      assert pix == 0 or pix == 255

def test_otsu_threshold():
  grayed = grayscale(sample_one)
  otsu_thresholded = otsu_threshold(grayed, 200, thresh_style=cv.THRESH_BINARY)

  assert type(otsu_thresholded['otsu_thresh']) == float
  assert otsu_thresholded['image'].ndim == 2
  assert otsu_thresholded['image'].shape == grayed.shape[0:2]
  for row in otsu_thresholded['image']:
    for pix in row:
      assert pix == 0 or pix == 200

def test_frame():
  framed = frame(sample_one)
  assert sample_one != framed
  assert sample_one.shape[0] < framed.shape[0] and sample_one.shape[1] < framed.shape[1]
  assert sample_one.shape[0] == framed.shape[0] - 4
  assert sample_one.shape[1] == framed.shape[1] - 4
  assert list(framed[0:1, 0:1].flatten()) == [255, 0, 0]

  framed = frame(sample_one, 1, 1, 3, 3, color=[150, 0, 0])
  assert sample_one != framed
  assert sample_one.shape[0] < framed.shape[0] and sample_one.shape[1] < framed.shape[1]
  assert sample_one.shape[0] == framed.shape[0] - 2
  assert sample_one.shape[1] == framed.shape[1] - 6
  assert list(framed[0:1, 0:1].flatten()) == [150, 0, 0]

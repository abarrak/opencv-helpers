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

IMG_SAMPLE = 'images/1.jpg'

def test_load():
  assert type(load(IMG_SAMPLE)) == np.ndarray
  with pytest.raises(Exception):
    load('images/not-there.jpg')

def test_rsize():
  img = load(IMG_SAMPLE)
  sized = resize(img, 200, 200)
  assert img != sized
  assert img.shape[0:2] != sized.shape[0:2]

def test_scale():
  img = load(IMG_SAMPLE)

  new_w = 200
  scaled = scale(img, new_w, 'width')
  assert img != scaled
  assert img.shape[0:2] != scaled.shape[0:2]
  # enusre formula: new height = [new width / (aspect ratio = original width / original height)]
  assert scaled.shape[0] == int(new_w // (img.shape[1] / img.shape[0]))
  
  new_h = 300
  scaled = scale(img, new_h, 'height')
  assert img != scaled
  assert img.shape[0:2] != scaled.shape[0:2]
  # enusre formula: new width = [new height / (aspect ratio = original width / original height)]
  assert scaled.shape[1] == int(new_h // (img.shape[1] / img.shape[0]))

  with pytest.raises(Exception):
    scale(img, 200, 'malform')

def test_frame():
  pass

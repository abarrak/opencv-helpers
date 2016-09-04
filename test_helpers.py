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

  with pytest.raises(Exception):
    scale(sample_one, 200, 'malform')

def test_frame():
  framed = frame(sample_one)
  assert sample_one != framed
  assert sample_one.shape[0] < framed.shape[0] and sample_one.shape[1] < framed.shape[1]
  assert sample_one.shape[0] == framed.shape[0] - 4
  assert sample_one.shape[1] == framed.shape[1] - 4

  framed = frame(sample_one, 1, 1, 3, 3)
  assert sample_one != framed
  assert sample_one.shape[0] < framed.shape[0] and sample_one.shape[1] < framed.shape[1]
  assert sample_one.shape[0] == framed.shape[0] - 2
  assert sample_one.shape[1] == framed.shape[1] - 6


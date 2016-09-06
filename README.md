# OpenCV Helpers
[![Build Status](https://travis-ci.org/abarrak/opencv-helpers.svg?branch=master)](https://travis-ci.org/abarrak/opencv-helpers)

## Summary



## Installing



## Usage Examples

#### Crop an image
```python
show(crop(load('images/1.jpg'), 200, 420, 100, 230))
```
#### Grayscale an image
```python
show(grayscale(load('images/1.jpg')))
```

#### Threshold an image based on fixed criteria
```python
gray = grayscale(load('images/1.jpg'))
show(fixed_threshold(gray, 40))
show(fixed_threshold(gray, 120, 255, cv.THRESH_BINARY))
```

#### Threshold an image based on adaptive criteria
```python
gray = grayscale(resize(load('images/2.jpg'), 900, 500))
show(adaptive_threshold(gray, 200))
show(adaptive_threshold(gray, 180, 'gaussian', 35, 15, cv.THRESH_BINARY))
```

#### Threshold an image using otsu's binarization
```python
gray = grayscale(resize(load('images/2.jpg'), 900, 500))
show(otsu_threshold(gray, 200)['image'])
```



## Contribute



## License
Unlicensed (public domain).

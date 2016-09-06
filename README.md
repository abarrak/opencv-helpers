# OpenCV Helpers
[![Build Status](https://travis-ci.org/abarrak/opencv-helpers.svg?branch=master)](https://travis-ci.org/abarrak/opencv-helpers)

## Summary



## Installing



## Usage Examples

#### Crop an image
```python
_1 = convert_to_rgb(load('images/1.jpg'))
_2 = crop(_1, 200, 420, 100, 230)
plot_two_images(_1, _2, title='Croping')
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/crop_1.png)

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/crop_2.png)

#### Grayscale an image
```python
  _1 = convert_to_rgb(load('images/1.jpg'))
  _2 = grayscale(_1, is_rgb=True)
  plot_two_images(_1, _2, cmap_2='gray', title='GrayScaling')
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/grayscale.png)


#### Threshold an image based on fixed criteria
```python
_1 = convert_to_rgb(load('images/1.jpg'))
gray = grayscale(_1, is_rgb=True)
_2 = fixed_threshold(gray, 40)

plot_two_images(_1, _2, cmap_2='Greys', title="Fixed Threshold")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/fixed_threshold_1.png)

```python
_1 = convert_to_rgb(load('images/1.jpg'))
gray = grayscale(_1, is_rgb=True)
_2 = fixed_threshold(gray, 120, 255, cv.THRESH_BINARY)

plot_two_images(_1, _2, cmap_2='Greys', title="Fixed Threshold")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/fixed_threshold_2.png)

#### Threshold an image based on adaptive criteria
```python
_1 = convert_to_rgb(load('images/2.jpg'))
gray = grayscale(_1, is_rgb=True)
_2 = adaptive_threshold(gray, 200)

plot_two_images(_1, _2, cmap_2='Greys', title="Adaptive Threshold")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/adaptive_threshold_1.png)

```python
_1 = convert_to_rgb(load('images/2.jpg'))
gray = grayscale(_1, is_rgb=True)
_2 = adaptive_threshold(gray, 180, 'gaussian', 35, 15, cv.THRESH_BINARY)

plot_two_images(_1, _2, cmap_2='Greys', title="Adaptive Threshold")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/adaptive_threshold_2.png)

#### Threshold an image using otsu's binarization
```python
_1 = convert_to_rgb(load('images/2.jpg'))
gray = grayscale(_1, is_rgb=True)
_2 = otsu_threshold(gray, 200)['image']

plot_two_images(_1, _2, cmap_2='Greys', title="Otsu Threshold")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/otsu_1.png)

```python
_1 = convert_to_rgb(load('images/1.jpg'))
gray = grayscale(_1, is_rgb=True)
_2 = otsu_threshold(gray, 200)['image']

plot_two_images(_1, _2, cmap_2='Greys', title="Otsu Threshold")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/otsu_2.png)

#### Thin and Stress Effects
```python
_1 = convert_to_rgb(load('images/2.jpg'))
_2 = thin(_1, (10, 10))
plot_two_images(_1, _2, title="Thin (Erode) Effect")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/thin.png)

```python
_1 = convert_to_rgb(load('images/2.jpg'))
_2 = stress(_1, (10, 10))
plot_two_images(_1, _2, title="Stress (Dilate) Effect")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/stress.png)


#### Smooth an Image
```python
_1 = convert_to_rgb(load('images/1.jpg'))
_2 = smooth(_1, kernel=(6, 6), method="blur")
plot_two_images(_1, _2, title="Blur Effect")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/blur_1.png)

```python
_1 = convert_to_rgb(load('images/2.jpg'))
_2 = smooth(_1, kernel=(51, 51), method="gaussian")
plot_two_images(_1, _2, title="Gaussian Blur Effect")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/blur_2.png)


#### Removing Noise and Filling Gaps
```python
gray = grayscale(load('images/1.jpg'))
_1 = fixed_threshold(gray, 40)
_2 = remove_noise(_1)
_2 = fill(_1, kernel=(100, 100))
plot_two_images(_1, _2, cmap_1='Greys', cmap_2='Greys', title="MorphologyEx Effect")
```

[screenshot](https://raw.githubusercontent.com/abarrak/opencv-helpers/master/docs/filling_gaps.png)


## Contribute
Once you've made your great commits:

    Fork The repository.
    Create a branch with a clear name.
    Make your changes (Please also add/change test, README if applicable).
    Push changes to the created branch
    Create an Pull Request
    That's it!

Please respect the indentation rules and code style. And use 2 spaces, not tabs.

## License
Unlicensed (public domain).

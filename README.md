# Digital Image Processing (CSE-3225, credit - 1.5)📷

Welcome to the **Digital Image Processing** repository! This repository contains a collection of Python programs that perform various image processing tasks using **Numpy**, **Pillow**, and **OpenCV** libraries. You can convert images, apply filters, manipulate pixel intensities, and more!

## Table of Contents 📚

1. [Image to Array](#image-to-array)
2. [Array to Image](#array-to-image)
3. [Blur an Image](#blur-an-image)
4. [Box Array for Specific Area](#box-array-for-specific-area)
5. [Color to Grayscale Conversion](#color-to-grayscale-conversion)
6. [Histogram Equalization](#histogram-equalization)
7. [Histogram Matching](#histogram-matching)
8. [Log Transformation](#log-transformation)
9. [Power-Law Transformation](#power-law-transformation)
10. [Negative Image](#negative-image)
11. [Sharpen an Image](#sharpen-an-image)
12. [Unsharpen Mask](#unsharpen-mask)
13. [Basic Pillow Library Programs](#basic-pillow-library-programs)

---

## 1. Image to Array 🌄

This program converts an image into a **NumPy array** using the `numpy.asarray()` method. It allows you to represent image pixels as an array, which is useful for various mathematical manipulations.

---

## 2. Array to Image 🖼️

Converts a **NumPy array** back to an image using the `Image.fromarray()` method. This is useful after performing operations on images in array form and converting them back to viewable images.

---

## 3. Blur an Image 🌫️

This program applies a **kernel** to blur an image. You can experiment with different kernels to apply varying levels of blur to an image.

---

## 4. Box Array for Specific Area 🔲

Extracts a specific portion of the image by converting only the selected area of the image into an array. Perfect for focusing on particular regions of interest in the image.

---

## 5. Color to Grayscale Conversion 🎨➡️⚫

Convert a **color image** to a **grayscale image** using the formula:


```
gray_array = 0.3 * red_channel + 0.59 * green_channel + 0.11 * blue_channel
```

- Red: 30%
- Green: 59%
- Blue: 11%

This gives a realistic representation of the grayscale equivalent of a color image.

---

## 6. Histogram Equalization 📊

This program manually applies **histogram equalization** to enhance the contrast of an image. It computes the cumulative distribution function (CDF) and normalizes the image intensity.

---

## 7. Histogram Matching 📈

Matches the histogram of a source image to that of a target image. This allows you to adjust the intensity distribution of one image to match another.

---

## 8. Log Transformation 🔢

Applies **logarithmic transformation** to an image, which can enhance the darker regions while compressing the brighter regions. It's useful for images with low contrast.

```python
def log_transform_uint8(image):
    c = 255 / np.log(1 + np.max(image))
    log_image = c * np.log(1 + image)
    log_image = np.clip(log_image, 0, 255).astype(np.uint8)
    return log_image
```

---

## 9. Power-Law Transformation ⚡

Performs **power-law transformation** (also known as gamma correction) on an image. By adjusting the `gamma` value, you can make the image lighter or darker.

```python
Array = numpy.array(Gray_image)
gamma_array = numpy.zeros_like(Array, dtype=numpy.float64)
for i in range(row):
    for j in range(column):
        gamma_array[i,j] = (c*(Array[i,j]))**gamma
```

---

## 10. Negative Image ⛔

Inverts the colors of the image by applying the **negative transformation**. The formula used is:

```
negative_image_array = 255 - image_array
```

This results in a visually "negative" version of the image.

---

## 11. Sharpen an Image 🔪

Applies a **sharpening mask** to enhance the edges and details of an image. The mask used is a **convolution kernel**, which is applied using `cv2.filter2D()`.

```python
mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, mask)
```

---

## 12. Unsharpen Mask 🔍

This program uses an **unsharp mask** to make an image sharper by subtracting a blurred version of the image from the original one. It enhances fine details and edges.

---

## 13. Basic Pillow Library Programs 🖌️

This section includes basic image manipulation programs using the **Pillow library** for tasks like resizing, cropping, rotating, and more.

---

## 📧 Contact

Have questions? Feel free to reach out via:

- **GitHub Issues**: [Submit an issue](../../issues)
- **Email**: [tasbi2116@cseku.ac.bd](mailto:tasbi2116@cseku.ac.bd)

---

### Contributions 🤝

Feel free to contribute by forking the repository, creating an issue, or submitting a pull request. Any suggestions or improvements are welcome!

---

Happy Coding! 🚀

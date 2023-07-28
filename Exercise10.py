import matplotlib.pyplot as plt
from skimage import color,io
from skimage.filters import threshold_otsu
from skimage import measure
import numpy as np
def show_image_contour(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
image1 = io.imread('image_dices.png')
image_dices = color.rgba2rgb(image1)
# Make the image grayscale
image_dices = color.rgb2gray(image_dices)
# Obtain the optimal thresh value
thresh = threshold_otsu(image_dices)
# Apply thresholding
thresholded_image = image_dices > thresh
contours = measure.find_contours(thresholded_image, level=0.8)
shape_contours = [cnt.shape[0] for cnt in contours]
# Set 90 as the maximum size of the dots shape
max_dots_shape = 50
# Count dots in contours excluding bigger than dots size
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0] < max_dots_shape]

# Shows all contours found
show_image_contour(thresholded_image, contours)
# Print the dice's number
print('Dice`s dots number: {}.'.format(len(dots_contours)))
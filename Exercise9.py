import matplotlib.pyplot as plt
from skimage import color,io
from skimage.filters import threshold_otsu
from skimage import measure

def show_image_contour(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

image1 = io.imread('xucxac.png')
image_dices = color.rgba2rgb(image1)
# Make the image grayscale
image_dices = color.rgb2gray(image_dices)
# Obtain the optimal thresh value
thresh = threshold_otsu(image_dices)
# Apply thresholding
thresholded_image = image_dices > thresh
# Find contours at a constant value of 0.8
contours = measure.find_contours(thresholded_image, level=0.8)
# Show the image
show_image_contour(image_dices, contours)
plt.show()
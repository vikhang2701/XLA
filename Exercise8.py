# Import the modules
from skimage import data, measure
import matplotlib.pyplot as plt
def show_image_contour(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Obtain the horse image
horse_image = data.horse()
# Find the contours with a constant level value of 0.8
contours = measure.find_contours(horse_image, 0.8)
# Shows the image with contours found
show_image_contour(horse_image, contours)
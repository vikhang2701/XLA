from skimage.io import imread
from skimage.restoration import inpaint
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load the image and display it
image_with_logo = imread('image_with_logo.jpg')
show_image(image_with_logo, 'Image with Logo')

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:2])

# Set the pixels where the logo is to 1
mask[210:272, 360:425] = 1

# Add an extra dimension to the mask to match the number of color channels in the image
mask = np.expand_dims(mask, axis=-1)
mask = np.tile(mask, (1, 1, 3))

# Apply inpainting to remove the logo
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo, mask)

# Display the resulting images
show_image(image_logo_removed, 'Image with Logo Removed')
import numpy as np
from skimage import io

# Load image
face_image = io.imread("face_image.jpg")

# Get image dimensions
height, width, _ = face_image.shape

# Calculate total number of pixels
total_pixels = np.prod(face_image.shape)

# Print the result
print(f"Total number of pixels in the image is {total_pixels}.")
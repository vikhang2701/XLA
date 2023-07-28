# Import the slic function from segmentation module
from skimage.segmentation import slic
# Import the label2rgb function from color module
from skimage.color import label2rgb
import matplotlib.pyplot as plt
face_image = plt.imread('face_image.jpg')
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
# Obtain the segmentation with 400 regions
segments = slic(face_image, n_segments=400)
# Put segments on top of original image to compare
segmented_image = label2rgb(segments, image=face_image, kind='avg')
# Show the segmented image
show_image(segmented_image, "Segmented image, 400 superpixels")
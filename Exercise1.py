from skimage.restoration import inpaint
import numpy as np
import matplotlib.pyplot as plt

def get_mask(image):
    mask = np.zeros(image.shape[:2])
    mask[101:106, 0:240] = 1
    mask[152:154, 0:60] = 1
    mask[153:155, 60:100] = 1
    mask[154:156, 100:120] = 1
    mask[155:156, 120:140] = 1
    mask[212:217, 0:150] = 1
    mask[217:222, 150:256] = 1
    return mask


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

defect_image = plt.imread('defect_image.png')

# Obtain the mask
mask = get_mask(defect_image)
print(defect_image.shape, mask.shape)

# Add an extra dimension to the mask to match the number of color channels in the image
mask = np.expand_dims(mask, axis=-1)
mask = np.tile(mask, (1, 1, 4))

# Apply inpainting to the damaged image using the mask
restored_image = inpaint.inpaint_biharmonic(defect_image, mask)

# Show the resulting image
show_image(defect_image, 'Image to restore')
show_image(restored_image, 'Image restored')
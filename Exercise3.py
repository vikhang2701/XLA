import matplotlib.pyplot as plt
from skimage import io, util
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
image = plt.imread('fruit_image.jpg')
noisy_image = util.random_noise(image, mode='gaussian', mean=0, var=0.08)
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4))
ax1.imshow(image)
ax1.set_title('Original Image')
ax2.imshow(noisy_image)
ax2.set_title('Noisy Image')
plt.show()

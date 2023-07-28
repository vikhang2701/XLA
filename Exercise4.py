import matplotlib.pyplot as plt
from skimage import restoration
from skimage import io, util
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
image = plt.imread('noisy_image.jpg')
noisy_image = util.random_noise(image, mode='gaussian', mean=0, var=0.01)
denoised_image = restoration.denoise_tv_chambolle(image, weight=0.00001)
fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original image')
ax[1].imshow(denoised_image, cmap='gray')
ax[1].set_title('Denoised image')
for a in ax:
    a.axis('off')
plt.show()
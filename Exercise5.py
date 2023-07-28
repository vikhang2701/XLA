from skimage.restoration import denoise_bilateral
import matplotlib.pyplot as plt

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load the image and display it
noisy_image = plt.imread('landscape_image.jpg')


# Apply bilateral filter denoising
denoised_image = denoise_bilateral(noisy_image, sigma_color=0.05, sigma_spatial=15,  channel_axis=-1)

fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
ax = axes.ravel()
ax[0].imshow(noisy_image, cmap='gray')
ax[0].set_title('noisy image')
ax[1].imshow(denoised_image, cmap='gray')
ax[1].set_title('denoised_image')
for a in ax:
    a.axis('off')
plt.show()
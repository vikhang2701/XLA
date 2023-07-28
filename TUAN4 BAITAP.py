import numpy as np
import matplotlib.pyplot as plt

img = np.array(plt.imread('nature.jpg'))

# hàm tự viết histogram
def histogram(gray_img):
    hist = np.zeros((256,), dtype=np.int32)
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            hist[gray_img[i][j]] += 1
    return hist

def equalize_hist_channel(channel):
    hist = histogram(channel)
    cum_hist = hist.cumsum()
    cum_hist_normalized = (cum_hist / cum_hist.max()) * 255
    equalized = cum_hist_normalized[channel]
    return equalized.astype(np.uint8)



# Chia ảnh thành từng kênh màu
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

# Cân bằng lược đồ màu cho từng kênh
r_equalized = equalize_hist_channel(r)
g_equalized = equalize_hist_channel(g)
b_equalized = equalize_hist_channel(b)

img_equalized = np.stack((r_equalized, g_equalized, b_equalized), axis=-1)

h, w, c = img.shape
# Khởi tạo các mảng để lưu giá trị histogram
hist_r, bins_r = np.histogram(r.flatten(), 256, [0, 256])
hist_g, bins_g = np.histogram(g.flatten(), 256, [0, 256])
hist_b, bins_b = np.histogram(b.flatten(), 256, [0, 256])

hist_r_e, bins_r_e = np.histogram(r_equalized.flatten(), 256, [0, 256])
hist_g_e, bins_g_e = np.histogram(g_equalized.flatten(), 256, [0, 256])
hist_b_e, bins_b_e = np.histogram(b_equalized.flatten(), 256, [0, 256])

 # Khởi tạo các mảng để lưu giá trị histogram


fig, axs = plt.subplots(3, 3, figsize=(8, 5))

# Hiển thị histogram của kênh đỏ ảnh gốc
axs[0, 0].bar(np.arange(256), hist_r, color='red')
axs[0, 0].set_title('Red Goc')

# Hiển thị histogram của kênh xanh da lá ảnh gốc
axs[0, 1].bar(np.arange(256), hist_g, color='green')
axs[0, 1].set_title('Green Goc')

# Hiển thị histogram của kênh xanh dương ảnh gốc
axs[0, 2].bar(np.arange(256), hist_b, color='blue')
axs[0, 2].set_title('Blue Goc')

# Hiển thị histogram của kênh đỏ ảnh đã được cân bằng
axs[1, 0].bar(np.arange(256), hist_r_e, color='red')
axs[1, 0].set_title('Red Sau CB')

# Hiển thị histogram của kênh xanh lá ảnh đã được cân bằng
axs[1, 1].bar(np.arange(256), hist_g_e, color='green')
axs[1, 1].set_title('Green Sau CB')

# Hiển thị histogram của kênh xanh dương ảnh đã được
axs[1, 2].bar(np.arange(256), hist_b_e, color='blue')
axs[1, 2].set_title('Blue Sau CB')

axs[2, 0].axis('off')
axs[2, 1].axis('off')
axs[2, 2].axis('off')
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(10, 7))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Anh goc')

# Hiển thị ảnh sau khi cân bằng histogram
plt.subplot(1, 2, 2)
plt.imshow(img_equalized)
plt.title('Anh sau khi CB histogram')
plt.show()
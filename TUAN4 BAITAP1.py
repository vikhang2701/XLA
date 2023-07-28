import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import color
def histogram_equalization(img):
    # Chuyển ảnh màu sang ảnh xám
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    abc = np.zeros((256,))
    # Tính toán histogram
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            pixel_value = gray_img[i,j]
            abc[pixel_value] += 1
    cdf = np.zeros((256,))
    # Tính toán histogram tích lũy
    cdf[0] = abc[0]
    for i in range(1,256):
        cdf[i] = cdf[i-1] + abc[i]

    # Tính toán hàm chuyển đổi mới
    new_cdf = np.zeros((256,))
    min_cdf = cdf[0]
    max_cdf = cdf[-1]
    for i in range(256):
        new_cdf[i] = np.round((cdf[i] - min_cdf) * 255 / (max_cdf - min_cdf))

    # Áp dụng hàm chuyển đổi mới
    equalized_img = np.zeros_like(gray_img)
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            pixel_value = gray_img[i,j]
            equalized_img[i,j] = new_cdf[pixel_value]

    # Chuyển đổi lại thành ảnh màu
    output_img = np.zeros_like(img)
    output_img[:, :, 0] = equalized_img
    output_img[:, :, 1] = equalized_img
    output_img[:, :, 2] = equalized_img

    # Vẽ histogram của ảnh đã được cân bằng
    equalized_hist = np.zeros((256,))
    for i in range(equalized_img.shape[0]):
        for j in range(equalized_img.shape[1]):
            pixel_value = equalized_img[i,j]
            equalized_hist[pixel_value] += 1
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10,5 ))

    # Vẽ biểu đồ histogram ảnh gốc
    axs[1, 0].bar(range(256), abc)
    axs[1, 0].set_title("Histogram ảnh gốc")

    # Vẽ biểu đồ histogram ảnh đã cân bằng
    axs[1, 1].bar(range(256), equalized_hist)
    axs[1, 1].set_title("Histogram ảnh cân bằng")

    # Hiển thị ảnh gốc
    axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title("Ảnh gốc")
    axs[0, 0].axis('off')

    # Hiển thị ảnh đã được cân bằng
    axs[0, 1].imshow(cv2.cvtColor(equalized_img, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title("Ảnh cân bằng")
    axs[0, 1].axis('off')

    # Xóa các khoảng trắng không cần thiết giữa các ô
    fig.tight_layout()

    # Hiển thị cửa sổ hiển thị ảnh
    plt.show()

    return output_img

image = plt.imread('nature.jpg')

# Áp dụng phép cân bằng histogram
equalized_img = histogram_equalization(image)
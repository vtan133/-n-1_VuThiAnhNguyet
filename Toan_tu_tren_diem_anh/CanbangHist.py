import cv2
import matplotlib.pyplot as plt

img = cv2.imread('keodan_dau.tif',0) # mở file ảnh
img_equalized = cv2.equalizeHist(img) # cân bằng hist cho ảnh img

fig = plt.figure(figsize=(16, 9))#Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2), (ax3,ax4) = fig.subplots(2, 2)#Tạo 4 vùng vẽ con, 2 cột 2 hàng

# Vẽ ảnh gốc trong vùng ax1
ax1.imshow(img, cmap='gray')
ax1.set_title("ảnh gốc")

# Vẽ hist của ảnh gốc trong vùng ax2
ax2.hist(img)
ax2.set_title("Histogram ảnh gốc")

# Vẽ ảnh sau khi cân bằng Hist trong vùng ax3
ax3.imshow(img_equalized, cmap='gray')
ax3.set_title("ảnh cân bằng histogram")

# Vẽ hist của ảnh cân bằng hist trong vùng ax4
ax4.hist(img_equalized)
ax4.set_title("Histogram ảnh cân bằng")

plt.show() # Hiển thị vùng vẽ
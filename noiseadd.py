import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread("8-bit-256-x-256-Grayscale-Lena-Image_W640.jpg",0)
print(img.shape)
gauss_noise=np.zeros((640,480),dtype=np.uint8)
cv2.randn(gauss_noise,128,20)
gauss_noise=(gauss_noise*0.5).astype(np.uint8)
gn_img=cv2.add(img,gauss_noise)
fig=plt.figure(dpi=300)

fig.add_subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.title("Original")

fig.add_subplot(1,3,2)
plt.imshow(gauss_noise,cmap='gray')
plt.axis("off")
plt.title("Gaussian Noise")

fig.add_subplot(1,3,3)
plt.imshow(gn_img,cmap='gray')
plt.axis("off")
plt.title("Combined")
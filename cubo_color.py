import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

#=================================================================
img = cv.imread('./Cubo/20221013_093334.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

# define range of blue color in HSV
lower_blue = np.array([100,50,50])
upper_blue = np.array([115,255,255])
lower_orange = np.array([5,100,100])
upper_orange = np.array([28,250,250])
lower_red = np.array([0,100,100])
upper_red = np.array([2,250,250])
lower_yellow = np.array([30,100,100])
upper_yellow = np.array([45,250,250])
lower_green= np.array([68,50,50])
upper_green = np.array([80,255,255])
# Threshold the HSV image to get only blue colors
mask1 = cv.inRange(hsv, lower_blue, upper_blue)
mask2 = cv.inRange(hsv, lower_orange, upper_orange)
mask3 = cv.inRange(hsv, lower_red, upper_red)
mask4 = cv.inRange(hsv, lower_yellow, upper_yellow)
mask5 = cv.inRange(hsv, lower_green, upper_green)



fig, axs = plt.subplots(1,6,figsize=(20,5))
axs[0].imshow(img)
axs[0].set_title('Imagen')
axs[1].imshow(mask1)
axs[1].set_title('azul')
axs[2].imshow(mask2)
axs[2].set_title('naranja')
axs[3].imshow(mask3)
axs[3].set_title('rojo')
axs[4].imshow(mask4)
axs[4].set_title('amarillo')
axs[5].imshow(mask5)
axs[5].set_title('verde')
